"""Manage a local clone of the pto-isa repository for auto-fetching docs."""

from __future__ import annotations

import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)

REPO_URL = "https://gitcode.com/cann/pto-isa.git"
DEFAULT_CACHE_DIR = Path.home() / ".cache" / "npu-coding-mcp"
CLONE_DIR_NAME = "pto-isa"


def ensure_docs(cache_dir: Path | None = None) -> Path:
    """Ensure a local clone of pto-isa exists and is up to date.

    On first run, clones the repository. On subsequent runs, pulls latest changes.

    Args:
        cache_dir: Directory to store the clone.  Defaults to ``~/.cache/npu-coding-mcp/``.

    Returns:
        Path to the ``docs/`` directory inside the clone.

    Raises:
        RuntimeError: If git operations fail.
    """
    if cache_dir is None:
        cache_dir = DEFAULT_CACHE_DIR

    cache_dir.mkdir(parents=True, exist_ok=True)
    repo_dir = cache_dir / CLONE_DIR_NAME

    if not repo_dir.exists():
        logger.info("Cloning %s into %s ...", REPO_URL, repo_dir)
        _run_git(["git", "clone", "--depth", "1", REPO_URL, str(repo_dir)])
        logger.info("Clone complete.")
    else:
        logger.info("Pulling latest changes in %s ...", repo_dir)
        try:
            _run_git(["git", "pull", "--ff-only"], cwd=repo_dir)
            logger.info("Pull complete.")
        except RuntimeError as e:
            logger.warning("Pull failed, using existing clone: %s", e)

    docs_dir = repo_dir / "docs"
    if not docs_dir.is_dir():
        raise RuntimeError(
            f"Expected docs/ directory not found at {docs_dir}. The repository structure may have changed."
        )

    return docs_dir


def _run_git(cmd: list[str], cwd: Path | None = None) -> None:
    """Run a git command, raising RuntimeError on failure."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=120,
        )
    except FileNotFoundError:
        raise RuntimeError("git is not installed or not on PATH. Install git or provide an explicit --docs-path.")
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"git command timed out: {' '.join(cmd)}")

    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise RuntimeError(f"git command failed (exit {result.returncode}): {' '.join(cmd)}\n{stderr}")

    if result.stdout.strip():
        logger.debug("git output: %s", result.stdout.strip())
