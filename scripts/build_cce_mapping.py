#!/usr/bin/env python3
"""Build / update the CCE intrinsic mapping for all PTO-ISA instructions.

Compiles each NPU backend header via g++ -E to extract CCE intrinsics
and store the full preprocessed C++ source code. Optional LLM enrichment.

Usage:
    python scripts/build_cce_mapping.py                  # normal build
    python scripts/build_cce_mapping.py --force          # full rebuild
    python scripts/build_cce_mapping.py --no-llm         # skip LLM context
    python scripts/build_cce_mapping.py --api-key sk-xxx --delay 1
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from npu_coding_mcp.cce_extractor.agent import DEFAULT_MODEL, extract_intrinsics, resolve_api_key
from npu_coding_mcp.cce_extractor.models import CCEMapping, CCEMappingStore, InstructionCCEMapping
from npu_coding_mcp.cce_extractor.snapshot import DATA_DIR, NPU_DIRS, SNAPSHOT_DIR, update_snapshot

logger = logging.getLogger("build_cce_mapping")

OUTPUT_PATH = DATA_DIR / "cce_mapping.json"


def _save_store(store: CCEMappingStore, commit: str) -> None:
    store.ptoisa_commit = commit
    store.generated_at = datetime.now(timezone.utc).isoformat()
    OUTPUT_PATH.write_text(store.model_dump_json(indent=2))


def _load_existing() -> CCEMappingStore:
    if OUTPUT_PATH.exists():
        try:
            return CCEMappingStore.model_validate_json(OUTPUT_PATH.read_text())
        except Exception:
            logger.warning("Could not parse existing cce_mapping.json — starting fresh.")
    return CCEMappingStore()


def _backend_from_path(path: Path) -> str:
    return "a2a3" if "a2a3" in str(path) else "a5"


def _instruction_name(path: Path) -> str:
    stem = path.stem
    name_map = {
        "TFMod": "TFMOD",
        "TFModS": "TFMODS",
        "TLRelu": "TLRELU",
        "TAddS": "TADDS",
        "TSubS": "TSUBS",
        "TMulS": "TMULS",
        "TDivS": "TDIVS",
        "TMins": "TMINS",
        "TSels": "TSELS",
        "TMaxS": "TMAXS",
        "TSync": "TSYNC",
        "TTrans": "TTRANS",
        "TMov": "TMOV",
        "TCvt": "TCVT",
        "TMrgSort": "TMRGSORT",
        "TExtract": "TEXTRACT",
        "TCI": "TCI",
        "TExpandS": "TEXPANDS",
        "TAndS": "TANDS",
        "TOrS": "TORS",
        "TXorS": "TXORS",
        "TShlS": "TSHLS",
        "TShrS": "TSHRS",
        "MScatter": "MSCATTER",
        "MGather": "MGATHER",
        "TDequant": "TDEQUANT",
        "TQuant": "TQUANT",
        "TCmps": "TCMPS",
        "TMaxs": "TMAXS",
        "TPrelu": "TPRELU",
        "TFmod": "TFMOD",
        "TFmodS": "TFMODS",
        "TRem": "TREM",
        "TRemS": "TREMS",
        "TPrefetch": "TPREFETCH",
        "TRsqrt": "TRSQRT",
        "TPow": "TPOW",
    }
    return name_map.get(stem, stem.upper())


def _skip_file(name: str) -> bool:
    return name in (
        "common.hpp",
        "TBinOp.hpp",
        "TBinSOp.hpp",
        "TColExpandBinOp.hpp",
        "TRowExpandBinOp.hpp",
        "TUnaryOp.hpp",
        "utils.hpp",
        "datatype.hpp",
        "TRowReduce.hpp",
        "TRowReduceIdx.hpp",
        "TRowReduceOps.hpp",
        "TColReduceOps.hpp",
        "TColReduceIdx.hpp",
        "TPartOp.hpp",
        "TPartBinOps.hpp",
        "TPartArgBinOps.hpp",
        "TBitwiseSOp.hpp",
    )


def _discover_files() -> list[Path]:
    files: list[Path] = []
    for npu_dir in NPU_DIRS:
        src_dir = SNAPSHOT_DIR / npu_dir
        if src_dir.is_dir():
            for hpp in sorted(src_dir.glob("*.hpp")):
                if not _skip_file(hpp.name):
                    files.append(hpp)
    return files


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build PTO-ISA CCE intrinsic mapping")
    parser.add_argument("--force", action="store_true", help="Full rebuild")
    parser.add_argument("--no-llm", action="store_true", help="Skip LLM context enrichment")
    parser.add_argument("--api-key", default=None, help="DeepSeek API key")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"LLM model (default: {DEFAULT_MODEL})")
    parser.add_argument("--delay", type=float, default=0.1, help="Delay between files (default: 0.1s)")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    api_key = None if args.no_llm else resolve_api_key(args.api_key)

    from npu_coding_mcp.repo_manager import ensure_docs

    docs_path = ensure_docs()
    repo_dir = Path(docs_path).parent

    logger.info("=== Snapshot pto-isa headers ===")
    commit = update_snapshot(repo_dir)

    include_dir = str(SNAPSHOT_DIR / "include")
    logger.info("Include dir: %s", include_dir)

    store = _load_existing() if not args.force else CCEMappingStore()
    existing = set(store.instructions.keys()) if not args.force else set()

    all_files = _discover_files()
    todo = [f for f in all_files if _instruction_name(f) not in existing]

    if not todo:
        logger.info("All %d instructions already processed.", len(existing))
        return

    logger.info("=== Processing %d files (%d already done) ===", len(todo), len(existing))

    success = 0
    failed: list[str] = []
    t0 = time.time()

    for i, path in enumerate(todo, 1):
        backend = _backend_from_path(path)
        name = _instruction_name(path)
        header_path = str(path.absolute())
        eta = (time.time() - t0) / i * (len(todo) - i) if i > 0 else 0

        logger.info("[%d/%d] %s (%s) — ETA %.0fs", i, len(todo), name, backend, eta)

        try:
            intrinsics, raw_code = extract_intrinsics(
                header_path, name, backend, include_dir, api_key=api_key, model=args.model
            )

            source_file = str(path.relative_to(SNAPSHOT_DIR))
            mapping = CCEMapping(source_file=source_file, raw_code=raw_code, intrinsics=intrinsics)

            if name not in store.instructions:
                store.instructions[name] = InstructionCCEMapping(name=name)
            instr = store.instructions[name]
            if backend == "a2a3":
                instr.a2a3 = mapping
            else:
                instr.a5 = mapping

            n_ctx = sum(1 for c in intrinsics if c.context) if api_key else 0
            logger.info(
                "  -> %d intrinsics, %d bytes raw code (%d with context)", len(intrinsics), len(raw_code), n_ctx
            )
            success += 1
            _save_store(store, commit)

        except Exception:
            logger.exception("  -> FAILED")
            failed.append(f"{name}({backend})")

        if args.delay > 0 and i < len(todo):
            time.sleep(args.delay)

    _save_store(store, commit)
    a2 = sum(1 for v in store.instructions.values() if v.a2a3)
    a5 = sum(1 for v in store.instructions.values() if v.a5)
    logger.info("Done: %d/%d success. Store: %d A2A3, %d A5 — %.0fs", success, len(todo), a2, a5, time.time() - t0)
    if failed:
        logger.warning("Failed: %s", ", ".join(failed))


if __name__ == "__main__":
    main()
