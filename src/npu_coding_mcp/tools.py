import json
import logging
import os
import subprocess
import tempfile
import time
from subprocess import CalledProcessError

import requests
from pwn import ELF  # Required for dylibs inspection
from pydantic import BaseModel

from . import mcp

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


def parse_tool_result(result, model: type[BaseModel] = CompilationResult):
    data = json.loads(result.content[0].text)
    return model(**data)


@mcp.tool()
def compile_pto_isa(
    kernel_source: str,
    npu_arch: str = "dav-2201",
    define_membase: bool = False,
    timeout: int = 120,
) -> CompilationResult:
    """Compile a PTO-ISA kernel source string and return the compiler output.

    Args:
        kernel_source: The PTO-ISA kernel source code to compile.
        npu_arch: Target NPU architecture (default: Ascend910B).
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

    elf = ELF(lib_path)
    print(elf.symbols)  # all symbols
    print(elf.functions)  # only functions
    print(elf.plt)  # PLT entries
    print(elf.got)  # GOT entries

    return CompilationResult(
        success=True,
        exit_code=result.returncode,
        stdout=result.stdout,
        stderr=result.stderr,
        duration_ms=elapsed_ms,
        dylib_path=lib_path,
    )
