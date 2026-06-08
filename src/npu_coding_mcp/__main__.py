"""CLI entry point for the PTO-ISA + AscendC + CCE MCP server.

Usage:
    python -m npu_coding_mcp                                        # auto-clone from gitcode
    python -m npu_coding_mcp /path/to/pto-isa/docs                  # explicit docs path
    python -m npu_coding_mcp --ascendc-docs data/ascendc_docs       # with AscendC docs
    python -m npu_coding_mcp --cce-docs data/cce_docs               # with CCE docs
    python -m npu_coding_mcp --stdio                                 # stdio mode
    python -m npu_coding_mcp build-ascendc-index                     # rebuild AscendC index
    python -m npu_coding_mcp build-cce-index                          # rebuild CCE index
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path


def _default_package_dir() -> Path:
    """Return the project root directory."""
    return Path(__file__).resolve().parent.parent.parent


def _default_ascendc_docs() -> Path:
    """Auto-detect AscendC docs directory."""
    candidates = [
        _default_package_dir() / "data" / "ascendc_docs",
        Path.cwd() / "data" / "ascendc_docs",
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


def _default_ascendc_index() -> Path:
    """Auto-detect AscendC index path."""
    candidates = [
        _default_package_dir() / "data" / "ascendc_index.db",
        Path.cwd() / "data" / "ascendc_index.db",
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


def _default_cce_docs() -> Path:
    """Auto-detect CCE docs directory."""
    candidates = [
        _default_package_dir() / "data" / "cce_docs",
        Path.cwd() / "data" / "cce_docs",
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


def _default_cce_index() -> Path:
    """Auto-detect CCE index path."""
    candidates = [
        _default_package_dir() / "data" / "cce_index.db",
        Path.cwd() / "data" / "cce_index.db",
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


def _default_runtime_docs() -> Path:
    """Auto-detect Runtime docs directory."""
    candidates = [
        _default_package_dir() / "data" / "runtime_docs",
        Path.cwd() / "data" / "runtime_docs",
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


def _default_runtime_index() -> Path:
    """Auto-detect Runtime index path."""
    candidates = [
        _default_package_dir() / "data" / "runtime_index.db",
        Path.cwd() / "data" / "runtime_index.db",
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


def _cmd_build_index(args: argparse.Namespace) -> None:
    from .ascendc.index_builder import build_index

    docs = Path(args.ascendc_docs or _default_ascendc_docs())
    index = Path(args.ascendc_index or _default_ascendc_index())

    if not docs.exists():
        print(f"Error: AscendC docs directory not found: {docs}")
        sys.exit(1)

    count = build_index(docs, index)
    size_mb = index.stat().st_size / (1024 * 1024)
    print(f"Index built: {count} documents -> {index} ({size_mb:.1f} MB)")


def _cmd_build_cce_index(args: argparse.Namespace) -> None:
    from .cce.index_builder import build_index

    docs = Path(args.cce_docs or _default_cce_docs())
    index = Path(args.cce_index or _default_cce_index())

    if not docs.exists():
        print(f"Error: CCE docs directory not found: {docs}")
        sys.exit(1)

    count = build_index(docs, index)
    size_mb = index.stat().st_size / (1024 * 1024)
    print(f"Index built: {count} documents -> {index} ({size_mb:.1f} MB)")


def _cmd_build_runtime_index(args: argparse.Namespace) -> None:
    from .runtime.index_builder import build_index

    docs = Path(args.runtime_docs or _default_runtime_docs())
    index = Path(args.runtime_index or _default_runtime_index())

    if not docs.exists():
        print(f"Error: Runtime docs directory not found: {docs}")
        sys.exit(1)

    count = build_index(docs, index)
    size_mb = index.stat().st_size / (1024 * 1024)
    print(f"Index built: {count} documents -> {index} ({size_mb:.1f} MB)")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="npu-coding-mcp",
        description=(
            "MCP server exposing PTO-ISA instruction documentation, "
            "CANN 9.0.0 AscendC operator development guide, CCE Intrinsic development guide, "
            "and CANN Runtime API reference."
        ),
    )
    sub = parser.add_subparsers(dest="command")

    # build-ascendc-index subcommand
    build_p = sub.add_parser("build-ascendc-index", help="Rebuild the AscendC FTS5 search index")
    build_p.add_argument("--ascendc-docs", help="Path to ascendc_docs/ directory")
    build_p.add_argument("--ascendc-index", help="Output path for index.db")

    # build-cce-index subcommand
    build_cce_p = sub.add_parser("build-cce-index", help="Rebuild the CCE FTS5 search index")
    build_cce_p.add_argument("--cce-docs", help="Path to cce_docs/ directory")
    build_cce_p.add_argument("--cce-index", help="Output path for index.db")

    # build-runtime-index subcommand
    build_runtime_p = sub.add_parser("build-runtime-index", help="Rebuild the Runtime FTS5 search index")
    build_runtime_p.add_argument("--runtime-docs", help="Path to runtime_docs/ directory")
    build_runtime_p.add_argument("--runtime-index", help="Output path for index.db")

    # serve (default)
    serve_p = sub.add_parser("serve", help="Start the MCP server")
    serve_p.add_argument(
        "docs_path",
        nargs="?",
        default=None,
        help="Path to the docs/ directory of the pto-isa repo. Auto-cloned if omitted.",
    )
    serve_p.add_argument("--cache-dir", help="Cache directory for auto-cloned pto-isa repo")
    serve_p.add_argument("--host", default="0.0.0.0", help="HTTP host (default: 0.0.0.0)")
    serve_p.add_argument("--port", type=int, default=8080, help="HTTP port (default: 8080)")
    serve_p.add_argument("--stdio", action="store_true", help="Run in stdio mode")
    serve_p.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    serve_p.add_argument("--ascendc-docs", help="Path to AscendC docs directory")
    serve_p.add_argument("--ascendc-index", help="Path to AscendC index.db")
    serve_p.add_argument("--cce-docs", help="Path to CCE docs directory")
    serve_p.add_argument("--cce-index", help="Path to CCE index.db")
    serve_p.add_argument("--runtime-docs", help="Path to Runtime docs directory")
    serve_p.add_argument("--runtime-index", help="Path to Runtime index.db")

    # Backward compat: accept positional args without subcommand
    args, unknown = parser.parse_known_args(argv)
    if args.command is None:
        # Reparse with serve as default
        serve_args = argv or sys.argv[1:]
        # If first arg looks like a path (not a flag), treat as serve
        if serve_args and not serve_args[0].startswith("-"):
            args = parser.parse_args(["serve"] + serve_args)
        else:
            args = parser.parse_args(["serve"] + serve_args)

    if args.command == "build-ascendc-index":
        _cmd_build_index(args)
        return

    if args.command == "build-cce-index":
        _cmd_build_cce_index(args)
        return

    if args.command == "build-runtime-index":
        _cmd_build_runtime_index(args)
        return

    # --- serve ---
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr,
    )
    log = logging.getLogger(__name__)

    # Resolve pto-isa docs_path
    if args.docs_path:
        docs_path = args.docs_path
    else:
        from .repo_manager import ensure_docs

        cache_dir = Path(args.cache_dir) if args.cache_dir else None
        log.info("Auto-fetching pto-isa repository ...")
        docs_path = str(ensure_docs(cache_dir=cache_dir))

    # Resolve AscendC paths
    ascendc_docs = Path(args.ascendc_docs) if args.ascendc_docs else None
    if ascendc_docs is None:
        ascendc_docs = _default_ascendc_docs()
        if not ascendc_docs.exists():
            ascendc_docs = None

    ascendc_index = Path(args.ascendc_index) if args.ascendc_index else None
    if ascendc_index is None:
        ascendc_index = _default_ascendc_index()

    if ascendc_docs:
        log.info("AscendC docs: %s", ascendc_docs)
        log.info("AscendC index: %s", ascendc_index)

    # Resolve CCE paths
    cce_docs = Path(args.cce_docs) if args.cce_docs else None
    if cce_docs is None:
        cce_docs = _default_cce_docs()
        if not cce_docs.exists():
            cce_docs = None

    cce_index = Path(args.cce_index) if args.cce_index else None
    if cce_index is None:
        cce_index = _default_cce_index()

    if cce_docs:
        log.info("CCE docs: %s", cce_docs)
        log.info("CCE index: %s", cce_index)

    # Resolve Runtime paths
    runtime_docs = Path(args.runtime_docs) if args.runtime_docs else None
    if runtime_docs is None:
        runtime_docs = _default_runtime_docs()
        if not runtime_docs.exists():
            runtime_docs = None

    runtime_index = Path(args.runtime_index) if args.runtime_index else None
    if runtime_index is None:
        runtime_index = _default_runtime_index()

    if runtime_docs:
        log.info("Runtime docs: %s", runtime_docs)
        log.info("Runtime index: %s", runtime_index)

    from .server import create_server

    mcp = create_server(docs_path, ascendc_docs, ascendc_index, cce_docs, cce_index, runtime_docs, runtime_index)

    if args.stdio:
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="streamable-http", host=args.host, port=args.port)


if __name__ == "__main__":
    main()
