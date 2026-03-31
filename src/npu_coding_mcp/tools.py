import ctypes
import json
import logging
import os
from subprocess import CalledProcessError

from fastmcp import Context
from fastmcp.exceptions import ToolError
from pydantic import BaseModel

from . import mcp
from .kernel import FunctionSignature, extract_signatures, InputShapes
from .compile import jit_compile_pto_isa, CompilationResult

logger = logging.getLogger(__name__)


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
    try:
        lib_path, elapsed_ms, result = await jit_compile_pto_isa(
            kernel_source, npu_arch, define_membase, debug, timeout
        )

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
    except CalledProcessError as e:
        return CompilationResult(
            success=False,
            exit_code=e.returncode,
            stdout=e.stdout,
            stderr=e.stderr,
            duration_ms=-1,
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

    # TODO: infer the correct argtypes and restype for the call_kernel function instead of hardcoding void* and uint32

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
