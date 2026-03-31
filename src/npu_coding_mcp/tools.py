import ctypes
import json
import logging
import os
import subprocess
import tempfile
import time
from subprocess import CalledProcessError

import requests
from fastmcp import Context
from fastmcp.exceptions import ToolError
from pydantic import BaseModel

from . import mcp
from .kernel import FunctionSignature, extract_signatures, InputShapes

logger = logging.getLogger(__name__)


ASCEND_TOOLKIT_HOME = os.environ["ASCEND_TOOLKIT_HOME"]
PTO_LIB_PATH = os.environ.get("PTO_LIB_PATH", ASCEND_TOOLKIT_HOME)


class CompilationResult(BaseModel):
    success: bool
    exit_code: int
    stdout: str
    stderr: str
    duration_ms: float
    dylib_path: str | None = None  # None if compilation failed
    dylib_functions: dict[str, FunctionSignature] = {}
    input_shapes: InputShapes | None = (
        None  # Elicited input shapes from user after compilation
    )


def parse_tool_result(result, model: type[BaseModel] = CompilationResult):
    data = json.loads(result.content[0].text)
    return model(**data)


@mcp.tool()
async def compile_pto_isa(
    kernel_source: str,
    ctx: Context,
    npu_arch: str = "dav-2201",
    define_membase: bool = False,
    debug: bool = False,
    timeout: int = 120,
) -> CompilationResult:
    """Compile a PTO-ISA kernel source string and return the compiler output.

    Args:
        kernel_source: The PTO-ISA kernel source code to compile.
        npu_arch: Target NPU architecture (default: Ascend910B).
        define_membase: Whether to define MEMORY_BASE macro (default: False).
        debug: Whether to include debug symbols in the compiled output (default: False).
        timeout: Maximum time in seconds to wait for compilation to complete (default: 120).

    Returns:
        A string containing stdout, stderr, and exit status from the compiler.
    """
    print("compile_pto_isa_kernel is called.")

    flags = [
        "-fPIC",
        "-shared",
        "-xcce",
        "-O2",
        "-std=c++17",
        "-Wno-ignored-attributes",
        f"--npu-arch={npu_arch}",
        f"-I{PTO_LIB_PATH}/include",
    ]

    if debug:
        flags.append("-g")

    if define_membase:
        flags.append("-DMEMORY_BASE")

    if kernel_source.startswith("http"):
        print(f"Input CPP kernel is URL: {kernel_source}")
        kernel_source = requests.get(kernel_source).text

    src_path = None
    with tempfile.NamedTemporaryFile(suffix=".cpp", mode="w", delete=False) as src_file:
        src_file.write(kernel_source)
        src_path = src_file.name

    lib_path = src_path.replace(".cpp", ".so")

    elapsed_ms: int = 0
    result = None
    try:
        command = ["bisheng", *flags, src_path, "-o", lib_path]
        print(f"Running CMD: {command}")

        start = time.perf_counter()
        result = subprocess.run(
            command,
            timeout=timeout,
            check=True,
            capture_output=True,
            text=True,
        )
        elapsed_ms = (time.perf_counter() - start) * 1000
    except CalledProcessError as e:
        print(f"Compilation command failed: {e}")
        return CompilationResult(
            success=False,
            exit_code=e.returncode,
            stdout=e.stdout,
            stderr=e.stderr,
            duration_ms=elapsed_ms,
        )
    finally:
        os.unlink(src_path)

    sigs = extract_signatures(lib_path)
    elicited_shapes = await elicit_input_shapes(ctx, sigs)

    return CompilationResult(
        success=True,
        exit_code=result.returncode,
        stdout=result.stdout,
        stderr=result.stderr,
        duration_ms=elapsed_ms,
        dylib_path=lib_path,
        dylib_functions=sigs,
        input_shapes=elicited_shapes,
    )


async def elicit_input_shapes(
    ctx: Context, sigs: dict[str, FunctionSignature]
) -> InputShapes | None:
    # Build a human-readable summary of detected kernel signatures to
    # guide the user when answering the elicitation.
    if sigs:
        sig_lines = "\n".join(f"  • {sig}" for sig in sigs.values())
        elicit_message = (
            "Compilation succeeded. The following kernel functions were detected:\n"
            f"{sig_lines}\n\n"
            "Please provide the input tensor shapes you want to use for profiling or testing."
        )
    else:
        elicit_message = (
            "Compilation succeeded. Please provide the input tensor shapes "
            "you want to use for profiling or testing."
        )

    try:
        elicit_response = await ctx.elicit(elicit_message, response_type=InputShapes)
    except Exception as e:
        logger.warning(
            "Elicitation not supported by client, skipping input shapes: %s", e
        )
        return None

    if elicit_response.action == "accept":
        return elicit_response.data
    elif elicit_response.action == "decline":
        raise ToolError("User declined")
    elif elicit_response.action == "cancel":
        return None


def torch_to_ctypes(tensor):
    return ctypes.c_void_p(tensor.data_ptr())


@mcp.tool
def load_dylib(lib_path: str):

    lib_path = os.path.abspath(lib_path)
    try:
        lib = ctypes.CDLL(lib_path)

        # call_kernel(blockDim, stream, a, b, c, matrix_size)
        lib.call_kernel.argtypes = [
            ctypes.c_uint32,  # blockDim
            ctypes.c_void_p,  # stream
            ctypes.c_void_p,  # a
            ctypes.c_void_p,  # b
            ctypes.c_void_p,  # c
            ctypes.c_uint32,  # matrix_size
        ]
    except OSError as e:
        print(e)
        return None

    return lib

    """

    lib.call_kernel.argstypes.extend( [ctypes.c_void_p] * num_kernel_args)
    lib.call_kernel.argstypes.extend( [ctypes.c_uint32] * num_uint32_params)
    lib.call_kernel.restype = None

    def call_kernel_fnc(block_dim=block_dim, stream_ptr=None, *args):
        if stream_ptr is None:
            stream = torch.npu.current_stream()
            stream_ptr = getattr(  # pylint: disable=protected-access
                stream, "_as_parameter_", None
            )

        transformed_args = [torch_to_ctypes(arg) for arg in args]
        lib.call_kernel(
            block_dim,
            stream_ptr,
            *transformed_args,
        )
    """
