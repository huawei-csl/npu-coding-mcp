"""Detect changed pto-isa NPU header files via git diff."""

from __future__ import annotations

import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)

UPSTREAM_FILES = [
    "include/pto/common/pto_instr.hpp",
    "include/pto/common/pto_instr_impl.hpp",
]

NPU_GLOBS = [
    "include/pto/npu/a2a3/*.hpp",
    "include/pto/npu/a5/*.hpp",
]


def find_changed_files(
    prev_commit: str,
    current_commit: str,
    repo_dir: str | Path,
) -> tuple[list[Path], bool]:
    """Find changed NPU header files between two commits.

    Args:
        prev_commit: Previous (stored) commit hash.
        current_commit: Current HEAD commit hash.
        repo_dir: Path to the pto-isa repository root.

    Returns:
        (changed_npu_files, force_full_rebuild) tuple.
        force_full_rebuild is True when upstream files (pto_instr.hpp,
        pto_instr_impl.hpp) changed, indicating the instruction set may have
        changed.
    """
    repo = Path(repo_dir)

    if prev_commit == current_commit:
        logger.info("No commit change detected (%s).", prev_commit[:8])
        return [], False

    logger.info("Diff: %s..%s", prev_commit[:8], current_commit[:8])

    changed_paths = _git_diff_names(prev_commit, current_commit, repo)

    force_full = any(any(f in p for f in UPSTREAM_FILES) for p in changed_paths)

    if force_full:
        logger.info("Upstream file changed — full rebuild required.")

    npu_files: list[Path] = []
    for glob in NPU_GLOBS:
        for p in changed_paths:
            if _matches_glob(p, glob):
                npu_files.append(repo / p)

    logger.info(
        "%d NPU headers changed (full_rebuild=%s)",
        len(npu_files),
        force_full,
    )
    return npu_files, force_full


def _git_diff_names(prev: str, curr: str, repo: Path) -> list[str]:
    """Run git diff --name-only between two commits."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"{prev}..{curr}"],
            cwd=str(repo),
            capture_output=True,
            text=True,
            timeout=30,
        )
    except FileNotFoundError:
        raise RuntimeError("git is not available on PATH. Cannot detect changed files.")
    except subprocess.TimeoutExpired:
        raise RuntimeError("git diff timed out.")

    if result.returncode != 0:
        raise RuntimeError(f"git diff failed: {result.stderr.strip()}")

    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def _matches_glob(path: str, glob: str) -> bool:
    """Simple glob match for git diff paths against our globs."""
    import fnmatch

    return fnmatch.fnmatch(path, glob)
