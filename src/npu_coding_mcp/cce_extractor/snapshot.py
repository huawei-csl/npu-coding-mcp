"""Manage a snapshot of relevant pto-isa header files for CCE extraction."""

from __future__ import annotations

import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

HEADER_PATHS = [
    "include/pto/common/pto_instr.hpp",
    "include/pto/common/pto_instr_impl.hpp",
    "include/pto/common/arch_cce_intrinsic.hpp",
]

NPU_DIRS = [
    "include/pto/npu/a2a3",
    "include/pto/npu/a5",
]

DATA_DIR = Path(__file__).parent.parent.parent.parent / "data"
SNAPSHOT_DIR = DATA_DIR / "pto_isa_headers"
COMMIT_FILE = DATA_DIR / "ptoisacommit.txt"


def _read_head_commit(repo_dir: Path) -> str:
    """Read the HEAD commit hash from a git repository."""
    import subprocess

    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=str(repo_dir),
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to read git HEAD: {result.stderr.strip()}")
    return result.stdout.strip()


def update_snapshot(repo_dir: str | Path) -> str:
    """Copy the full pto-isa include tree into data/pto_isa_headers/ and record commit hash.

    Args:
        repo_dir: Path to the root of the pto-isa repository.

    Returns:
        Current HEAD commit hash.
    """
    repo = Path(repo_dir)

    commit_hash = _read_head_commit(repo)
    logger.info("PTO-ISA snapshot: commit %s", commit_hash[:8])

    if SNAPSHOT_DIR.exists():
        shutil.rmtree(SNAPSHOT_DIR)
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)

    src_include = repo / "include"
    dst_include = SNAPSHOT_DIR / "include"
    if src_include.is_dir():
        shutil.copytree(src_include, dst_include)
        logger.info("Copied full include tree from %s", src_include)
    else:
        logger.warning("include/ directory not found at %s", repo)

    a2a3_count = len(list((SNAPSHOT_DIR / "include/pto/npu/a2a3").glob("*.hpp")))
    a5_count = len(list((SNAPSHOT_DIR / "include/pto/npu/a5").glob("*.hpp")))
    logger.info("Snapshot created: %d A2A3 headers, %d A5 headers", a2a3_count, a5_count)

    COMMIT_FILE.write_text(commit_hash + "\n")
    return commit_hash


def read_snapshot_commit() -> str | None:
    """Read the stored commit hash, or None if no snapshot exists."""
    if COMMIT_FILE.exists():
        return COMMIT_FILE.read_text().strip()
    return None
