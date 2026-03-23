import shutil
import subprocess
import tempfile
from pathlib import Path

from . import mcp

_PTO_ISA_COMPILER = "pto-isa-compiler"  # expected on PATH


@mcp.tool()
def compile_pto_isa_kernel(
    kernel_source: str,
    target_core: str = "Ascend910B",
    extra_flags: str = "",
) -> str:
    """Compile a PTO-ISA kernel source string and return the compiler output.

    Args:
        kernel_source: The PTO-ISA kernel source code to compile.
        target_core: Target Ascend core variant (default: Ascend910B).
        extra_flags: Optional additional compiler flags (space-separated string).

    Returns:
        A string containing stdout, stderr, and exit status from the compiler.
    """
    compiler = shutil.which(_PTO_ISA_COMPILER)
    if compiler is None:
        return (
            f"Error: compiler '{_PTO_ISA_COMPILER}' not found on PATH. "
            "Please install the PTO-ISA toolchain and ensure the compiler binary is accessible."
        )

    with tempfile.TemporaryDirectory() as tmpdir:
        src_path = Path(tmpdir) / "kernel.isa"
        src_path.write_text(kernel_source, encoding="utf-8")

        cmd = [compiler, str(src_path), f"--target={target_core}"]
        if extra_flags.strip():
            cmd.extend(extra_flags.split())

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
        )

    lines = []
    if result.stdout:
        lines.append("=== stdout ===")
        lines.append(result.stdout.rstrip())
    if result.stderr:
        lines.append("=== stderr ===")
        lines.append(result.stderr.rstrip())
    lines.append(f"=== exit code: {result.returncode} ===")
    return "\n".join(lines)
