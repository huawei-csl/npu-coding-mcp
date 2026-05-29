# npu-coding-mcp

MCP server exposing **PTO-ISA tile instruction documentation** and the complete **CANN 9.0.0 AscendC operator development guide** for code-generation and optimization agents.

## Overview

This server provides two documentation domains through a single FastMCP server:

| Domain | Content | Tools |
|--------|---------|-------|
| **PTO-ISA** | ~143 tile instructions (assembly, C++ intrinsics, constraints, examples) | 14 tools |
| **AscendC** | CANN 9.0.0 operator development guide — 1,771 sections across 7 chapters (Chinese) | 6 tools |

**Zero-setup for PTO-ISA**: When no `docs_path` is provided, the server auto-clones [pto-isa](https://gitcode.com/cann/pto-isa) into `~/.cache/pto-isa-mcp/`. AscendC docs are pre-extracted and committed to `data/ascendc_docs/`.

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

# Build the AscendC search index (one-time)
python -m npu_coding_mcp build-ascendc-index

# Or from outside the venv:
PYTHONPATH="src:$PYTHONPATH" python3 -m npu_coding_mcp.__main__ build-ascendc-index
```

The AscendC FTS5 index is ~11 MB and lives at `data/ascendc_index.db`. If the index is missing when the server starts, it's auto-built from `data/ascendc_docs/`.

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
```

### Rebuild the AscendC index

```bash
python -m npu_coding_mcp build-ascendc-index
```

### CLI options

| Flag | Default | Description |
|------|---------|-------------|
| `docs_path` (positional) | auto-clone | Path to `pto-isa/docs/`. Auto-clones from gitcode.com if omitted |
| `--cache-dir` | `~/.cache/pto-isa-mcp/` | Cache directory for auto-cloned pto-isa |
| `--ascendc-docs` | `data/ascendc_docs/` | Path to AscendC docs |
| `--ascendc-index` | `data/ascendc_index.db` | Path to AscendC FTS5 index |
| `--host` | `0.0.0.0` | HTTP bind address |
| `--port` | `8080` | HTTP port |
| `--stdio` | off | Run in stdio transport mode |
| `--log-level` | `INFO` | Logging level |

## MCP Tools (20 total)

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
| `search_docs(query, max_results, language)` | Full-text FTS5 search across 1,771 sections. `language="en"` (default) for translation instruction, `"zh"` for raw Chinese |
| `get_section(path, language)` | Read a section by file path |
| `list_chapters()` | List 7 chapters with descriptions and section counts |
| `get_chapter_tree(chapter_path)` | Section hierarchy for a chapter, with page ranges |
| `search_api(api_name)` | Fast API lookup in `06_API参考/` only (1,561 API sections) |
| `get_toc()` | Complete document table of contents |

All tools are read-only and idempotent.

## Agent Orientation Resources

The server exposes two MCP resources that agents load automatically:

| Resource | Content |
|----------|---------|
| `npu-coding://guide` | PTO-ISA + AscendC orientation: all 20 tools, recommended workflow, key concepts |
| `ascendc://guide` | AscendC-specific guide: chapter overview, language support, search patterns |

## OpenCode Integration

Add to your `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "npu-coding": {
      "type": "local",
      "command": ["python3", "-m", "npu_coding_mcp.__main__", "serve", "--stdio"],
      "env": {
        "PYTHONPATH": "/home/ebezati/git/workflow/npu-coding-mcp/src"
      },
      "enabled": true
    }
  }
}
```

### Other MCP clients (Claude, Cursor, etc.)

```json
{
  "mcpServers": {
    "npu-coding": {
      "command": "python3",
      "args": ["-m", "npu_coding_mcp.__main__", "serve", "--stdio"],
      "env": {
        "PYTHONPATH": "/home/ebezati/git/workflow/npu-coding-mcp/src"
      }
    }
  }
}
```

## Language support (AscendC)

All AscendC content is in Chinese. Every content-returning tool accepts a `language` parameter:

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
│   │   ├── 00-index.md
│   │   ├── 01_入门教程/
│   │   ├── 02_编程指南/
│   │   └── ...
│   └── ascendc_index.db         # FTS5 search index (~11 MB)
├── src/
│   └── npu_coding_mcp/
│       ├── __init__.py
│       ├── __main__.py           # CLI: serve | build-ascendc-index
│       ├── server.py              # FastMCP server + both stores
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
│       └── cce_extractor/         # CCE intrinsic extraction (g++ preprocessor)
├── scripts/
│   └── build_cce_mapping.py       # CCE mapping build script
├── tests/
│   ├── test_loader.py
│   └── test_cce_extractor.py
└── plan/
    └── TODO.md
```
