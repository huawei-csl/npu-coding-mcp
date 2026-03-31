import subprocess
import tempfile
import time
import requests
import os

from npu_coding_mcp.kernel import InputShapes
from npu_coding_mcp.kernel import FunctionSignature
from pydantic import BaseModel
from subprocess import CalledProcessError

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


async def jit_compile_pto_isa(
    kernel_source: str,
    npu_arch: str = "dav-2201",
    define_membase: bool = False,
    debug: bool = False,
    timeout: int = 120,
) -> str:
    """Compile a PTO-ISA kernel source string and return the compiler output.

    Args:
        kernel_source: The PTO-ISA kernel source code to compile.
        npu_arch: Target NPU architecture (default: Ascend910B).
        define_membase: Whether to define MEMORY_BASE macro (default: False).
        debug: Whether to include debug symbols in the compiled output (default: False).
        timeout: Maximum time in seconds to wait for compilation to complete (default: 120).
     print("compile_pto_isa_kernel is called.")
    """

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
        print(f"Compilation command failed: {e}. {result}")
        raise
    finally:
        os.unlink(src_path)

    return lib_path, elapsed_ms, result
