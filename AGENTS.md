# AGENTS.md

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Build the AscendC + CCE FTS5 search indexes (one-time, committed but server auto-builds if missing)
python -m npu_coding_mcp build-ascendc-index
python -m npu_coding_mcp build-cce-index
```

CI uses `uv sync --all-groups` and `uv run` — works as an alternative to pip.

## Commands

```bash
# Lint + format check
ruff check src/ tests/
ruff format --check src/ tests/

# Fix lint + format
ruff check --fix src/ tests/
ruff format src/ tests/

# Run tests (requires pto-isa docs)
PTOISA_DOCS_PATH=/path/to/pto-isa/docs pytest tests/ -v

# Run server (stdio mode for MCP clients)
python -m npu_coding_mcp serve --stdio

# Run server with explicit pto-isa docs path (HTTP mode, default 0.0.0.0:8080)
python -m npu_coding_mcp serve /path/to/pto-isa/docs

# Rebuild indexes
python -m npu_coding_mcp build-ascendc-index
python -m npu_coding_mcp build-cce-index
```

The CLI accepts bare positional args without the `serve` subcommand for backward compat: `python -m npu_coding_mcp /path/to/docs --stdio`.

## Testing

Tests require access to the real `pto-isa` documentation tree. Set `PTOISA_DOCS_PATH` env var or place the `pto-isa` repo as a sibling directory (`../pto-isa/docs`). Without docs, all tests fail.

CCE mapping tests (`test_cce_extractor.py`) additionally require `data/cce_mapping.json` (committed) to exist.

Only two test modules exist: `test_loader.py` (PTO-ISA, 28+ tests) and `test_cce_extractor.py` (CCE mapping). No AscendC-specific tests.

## Architecture

- **Single package** at `src/npu_coding_mcp/`
- **Three domains**: PTO-ISA (14 tools in `tools.py`) + AscendC (6 tools in `ascendc/tools.py`) + CCE (6 tools in `cce/tools.py`) = 26 total
- **Startup**: `loader.py` parses all markdown docs into an in-memory `ISAStore` (Pydantic models in `models.py`). AscendC loader lives in `ascendc/loader.py`, CCE loader in `cce/loader.py`
- **Auto-clone**: when no `docs_path` given, `repo_manager.py` clones `https://gitcode.com/cann/pto-isa.git` into `~/.cache/npu-coding-mcp/` (NB: README.md still references the old path `~/.cache/pto-isa-mcp/` — the code uses `npu-coding-mcp`)
- **Transport**: FastMCP supports `--stdio` and HTTP (`streamable-http`)
- **CCE mapping**: Pre-built by `scripts/build_cce_mapping.py` via compile-and-extract, committed as `data/cce_mapping.json`. `loader.py` loads it into `ISAStore.cce_mappings`
- **Entry point**: `__main__.py` — subcommands `serve` (default), `build-ascendc-index`, `build-cce-index`
- **Tool prefixes**: All AscendC doc tools use `ascendc_` prefix, all CCE doc tools use `cce_` prefix, PTO-ISA tools have no prefix

## CCE Mapping (`get_cce_intrinsics` tool)

Maps each PTO-ISA instruction to the CCE (CANN Compute Engine) intrinsics it calls. The mapping in `data/cce_mapping.json` is committed (tracks pto-isa commit in `data/ptoisacommit.txt`) and generated via **compile-and-extract**: NPU headers are compiled with `g++ -E` to resolve templates and `if constexpr` branches, then CCE intrinsic calls are regex-extracted. LLM is optional — only for `context` field enrichment when `--api-key` is provided.

```bash
# Rebuild cce_mapping.json (fast, ~100s)
python scripts/build_cce_mapping.py --force --no-llm
```

Requires: `g++` on PATH, PTO headers at `/usr/local/Ascend/cann-9.0.0/x86_64-linux/include`. Set `GXX` env var to override compiler path.

## AscendC documentation

- 1,771 markdown sections across 7 chapters, all in Chinese, committed to `data/ascendc_docs/`
- FTS5 index at `data/ascendc_index.db` (committed; auto-built on startup if missing)
- All 6 AscendC tools use `ascendc_` prefix and accept `language` param: `"en"` (default, prepends translation instruction) or `"zh"` (raw Chinese)

## CCE documentation

- 154 markdown sections across 6 chapters, all in Chinese, committed to `data/cce_docs/`
- FTS5 index at `data/cce_index.db` (committed; auto-built on startup if missing)
- Source PDF converted via pdf-to-markdown, then split by `scripts/split_cce_docs.py`
- All 6 CCE tools use `cce_` prefix and accept `language` param, same pattern as AscendC
- Tools: `cce_search_docs`, `cce_get_section`, `cce_list_chapters`, `cce_get_chapter_tree`, `cce_search_api`, `cce_get_toc`

## Maintenance note

`tests/AGENTS.md` is an outdated duplicate of this file. Prefer the root `AGENTS.md` as the single source of truth.

## Known quirks

- `pyproject.toml` line 34 has `packages = ["src/pto_isa_mcp"]` — stale; the real package is `src/npu_coding_mcp`. Editable installs work, wheel builds may need this fixed.
- The manifest at `docs/isa/manifest.yaml` is actually JSON (despite `.yaml` extension). The loader tries `json.loads()` first with YAML fallback.
- `data/pto_isa_headers/` is committed (~457 files, mostly `.hpp` headers). It's a snapshot required by CCE mapping — only the README files plus extracted headers are tracked; temporarily generated preprocessed files are not.

## Style

- Ruff: line-length 120, target py310, double quotes
- No type checker configured (no mypy/pyright)
- No pre-commit hooks or CI pipelines configured (`.github/` directory does not exist)
