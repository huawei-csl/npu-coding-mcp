# npu-coding-mcp

MCP server exposing **PTO-ISA tile instruction documentation**, the complete **CANN 9.0.0 AscendC operator development guide**, and the **CCE Intrinsic development guide** for code-generation and optimization agents.

## Overview

This server provides three documentation domains through a single FastMCP server:

| Domain | Content | Tools |
|--------|---------|-------|
| **PTO-ISA** | ~143 tile instructions (assembly, C++ intrinsics, constraints, examples) | 14 tools |
| **AscendC** | CANN 9.0.0 operator development guide — 1,771 sections across 7 chapters (Chinese) | 6 tools |
| **CCE** | CANN 9.0.0 CCE Intrinsic development guide — 154 sections across 6 chapters (Chinese) | 6 tools |

**Zero-setup for PTO-ISA**: When no `docs_path` is provided, the server auto-clones [pto-isa](https://gitcode.com/cann/pto-isa) into `~/.cache/pto-isa-mcp/`.

## Requirements

- Python >= 3.10
- `git` (for auto-clone of pto-isa; optional if passing explicit `docs_path`)

## Installation

```bash
cd /home/ebezati/git/workflow/npu-coding-mcp

# Create venv and install
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Build the AscendC and CCE search indexes (one-time)
python -m npu_coding_mcp build-ascendc-index
python -m npu_coding_mcp build-cce-index

# Or from outside the venv:
PYTHONPATH="src:$PYTHONPATH" python3 -m npu_coding_mcp.__main__ build-ascendc-index
PYTHONPATH="src:$PYTHONPATH" python3 -m npu_coding_mcp.__main__ build-cce-index
```

The AscendC FTS5 index is ~11 MB and lives at `data/ascendc_index.db`. The CCE index is ~0.5 MB at `data/cce_index.db`. If either index is missing when the server starts, it's auto-built from the corresponding `data/*_docs/` directory.

## Usage

### Start the server

```bash
# Auto-clone pto-isa + load AscendC docs (stdio mode for MCP clients)
python -m npu_coding_mcp serve --stdio

# Explicit pto-isa path + AscendC
python -m npu_coding_mcp serve /path/to/pto-isa/docs --stdio

# HTTP mode
python -m npu_coding_mcp serve --host 0.0.0.0 --port 8080

# Explicit AscendC paths
python -m npu_coding_mcp serve --ascendc-docs data/ascendc_docs --ascendc-index data/ascendc_index.db --stdio

# With CCE docs enabled
python -m npu_coding_mcp serve --cce-docs data/cce_docs --cce-index data/cce_index.db --stdio
```

### Rebuild the indexes

```bash
python -m npu_coding_mcp build-ascendc-index
python -m npu_coding_mcp build-cce-index
```

### CLI options

| Flag | Default | Description |
|------|---------|-------------|
| `docs_path` (positional) | auto-clone | Path to `pto-isa/docs/`. Auto-clones from gitcode.com if omitted |
| `--cache-dir` | `~/.cache/pto-isa-mcp/` | Cache directory for auto-cloned pto-isa |
| `--ascendc-docs` | `data/ascendc_docs/` | Path to AscendC docs |
| `--ascendc-index` | `data/ascendc_index.db` | Path to AscendC FTS5 index |
| `--cce-docs` | `data/cce_docs/` | Path to CCE docs |
| `--cce-index` | `data/cce_index.db` | Path to CCE FTS5 index |
| `--host` | `0.0.0.0` | HTTP bind address |
| `--port` | `8080` | HTTP port |
| `--stdio` | off | Run in stdio transport mode |
| `--log-level` | `INFO` | Logging level |

## MCP Tools (26 total)

### PTO-ISA — Discovery & search

| Tool | Description |
|------|-------------|
| `list_categories()` | List all instruction families with counts and member names |
| `list_instructions(category?)` | List instructions, filtered optionally by category (partial match) |
| `search_instructions(query)` | Full-text search across names, summaries, categories |

### PTO-ISA — Per-instruction detail

| Tool | Description |
|------|-------------|
| `get_instruction(name)` | Full detail: math, assembly, C++ intrinsic, constraints, examples |
| `get_assembly_format(name, level?)` | Assembly syntax (L1_SSA / L2_DPS / sync) |
| `get_cpp_intrinsic(name)` | C++ template signature + header path |
| `get_constraints(name, backend?)` | Constraints, optionally filtered by backend (a2a3/a5/common) |
| `get_examples(name, mode?)` | Code examples (auto/manual/asm variants) |

### PTO-ISA — Reference

| Tool | Description |
|------|-------------|
| `get_grammar()` | PTO-AS BNF grammar, language spec, conventions |
| `get_family_doc(category)` | Full assembly family document for a category |
| `get_scalar_ops(name?, subcategory?)` | Scalar arithmetic ops (MLIR arith dialect, 49 ops) |
| `get_control_flow_ops(name?)` | Control flow ops (MLIR scf dialect, 8 ops) |
| `get_auxiliary_ops(name?)` | Non-ISA aux ops (alloc, sync, view, pointer) |
| `get_cce_intrinsics(name, backend?)` | CCE intrinsic calls per backend |

### AscendC — Documentation

| Tool | Description |
|------|-------------|
| `ascendc_search_docs(query, max_results, language)` | Full-text FTS5 search across 1,771 sections. `language="en"` (default) for translation instruction, `"zh"` for raw Chinese |
| `ascendc_get_section(path, language)` | Read a section by file path |
| `ascendc_list_chapters()` | List 7 chapters with descriptions and section counts |
| `ascendc_get_chapter_tree(chapter_path)` | Section hierarchy for a chapter, with page ranges |
| `ascendc_search_api(api_name)` | Fast API lookup in `06_API参考/` only (1,561 API sections) |
| `ascendc_get_toc()` | Complete document table of contents |

### CCE — Documentation

| Tool | Description |
|------|-------------|
| `cce_search_docs(query, max_results, language)` | Full-text FTS5 search across 154 sections. `language="en"` (default) for translation instruction, `"zh"` for raw Chinese |
| `cce_get_section(path, language)` | Read a section by file path |
| `cce_list_chapters()` | List 6 chapters with descriptions and section counts |
| `cce_get_chapter_tree(chapter_path)` | Section hierarchy for a chapter |
| `cce_search_api(api_name)` | Fast API lookup in `06_API参考/` only |
| `cce_get_toc()` | Complete document table of contents |

All tools are read-only and idempotent.

## Agent Orientation Resources

The server exposes three MCP resources that agents load automatically:

| Resource | Content |
|----------|---------|
| `npu-coding://guide` | PTO-ISA + AscendC + CCE orientation: all 26 tools, recommended workflow, key concepts |
| `ascendc://guide` | AscendC-specific guide: chapter overview, language support, search patterns |
| `cce://guide` | CCE-specific guide: chapter overview, language support, search patterns |

## OpenCode Integration

After `uv sync --all-groups`, add to `opencode.json`:

```json
{
  "mcp": {
    "npu-coding": {
      "type": "local",
      "command": ["/home/ebezati/git/workflow/npu-coding-mcp/.venv/bin/python", "-m", "npu_coding_mcp.__main__", "serve", "--stdio"],
      "enabled": true
    }
  }
}
```

Works globally — data dirs auto-detect from the package location, independent of cwd.

## Language support (AscendC and CCE)

All AscendC and CCE content is in Chinese. Every content-returning tool accepts a `language` parameter:

| Value | Behavior |
|-------|----------|
| `"en"` (default) | Prepends translation instruction. LLM translates Chinese to English |
| `"zh"` | Returns raw Chinese content as-is |

## Testing

```bash
# PTO-ISA tests (requires pto-isa docs)
PTOISA_DOCS_PATH=/path/to/pto-isa/docs pytest tests/ -v

# Or auto-detect sibling directory:
pytest tests/ -v
```

## Project Structure

```
npu-coding-mcp/
├── pyproject.toml
├── README.md
├── data/
│   ├── cce_mapping.json         # Pre-built CCE intrinsic mapping
│   ├── ptoisa_headers/          # Snapshot of pto-isa headers
│   ├── ascendc_docs/            # AscendC markdown (1,771 sections)
│   ├── ascendc_index.db         # AscendC FTS5 search index (~11 MB)
│   ├── cce_docs/                # CCE markdown (154 sections)
│   └── cce_index.db             # CCE FTS5 search index (~0.5 MB)
├── src/
│   └── npu_coding_mcp/
│       ├── __init__.py
│       ├── __main__.py           # CLI: serve | build-ascendc-index | build-cce-index
│       │   ├── server.py              # FastMCP server + all three stores
│       ├── loader.py              # PTO-ISA doc parser (ISAStore)
│       ├── models.py              # PTO-ISA Pydantic models
│       ├── tools.py               # 14 PTO-ISA tool definitions
│       ├── repo_manager.py        # Auto-clone/pull pto-isa.git
│       ├── ascendc/               # AscendC documentation submodule
│       │   ├── __init__.py
│       │   ├── models.py          # SearchResult, SectionContent, ChapterInfo
│       │   ├── loader.py          # AscendCStore + FTS5 access
│       │   ├── tools.py           # 6 AscendC tool definitions
│       │   └── index_builder.py   # Build FTS5 index
│       └── cce/                    # CCE documentation submodule
│           ├── __init__.py
│           ├── models.py          # SearchResult, SectionContent, ChapterInfo
│           ├── loader.py          # CCEStore + FTS5 access
│           ├── tools.py           # 6 CCE tool definitions
│           └── index_builder.py   # Build FTS5 index
├── scripts/
│   └── build_cce_mapping.py       # CCE mapping build script
├── tests/
│   ├── test_loader.py
│   └── test_cce_extractor.py
└── plan/
    └── TODO.md
```
