"""FastMCP server setup and transport configuration."""

from __future__ import annotations

import logging
from pathlib import Path

from fastmcp import FastMCP

from .loader import load_isa_store
from .tools import register_tools

logger = logging.getLogger(__name__)


_AGENT_GUIDE = """\
# NPU Coding MCP Server — Agent Guide

Read this first when connecting to the npu-coding-mcp server.

## What Is PTO-ISA?

PTO (Parallel Tile Operation) is a virtual ISA for Ascend AI processors (CANN).
It defines ~120 tile-level instructions for elementwise math, matrix multiply,
memory transfers, data layout, reductions, and more. Code targets two backends:

- **A2/A3** — Atlas 300I / Atlas A2 family (Ascend 910B)
- **A5** — next-generation Atlas A3 family

Programs are written in C++ using PTO intrinsics (e.g. `TADD(dst, src0, src1)`)
or in PTO-AS assembly (an MLIR-inspired text format with SSA values and typed
tile operands).

## Available Tools (26)

### PTO-ISA — Discovery & search
| Tool | When to use |
|------|-------------|
| `list_categories()` | First call — understand what instruction families exist |
| `list_instructions(category?)` | Browse instructions, optionally filtered by category |
| `search_instructions(query)` | Free-text search across names, summaries, categories |

### PTO-ISA — Per-instruction detail
| Tool | When to use |
|------|-------------|
| `get_instruction(name)` | Full detail: math, assembly, C++ intrinsic, constraints, examples |
| `get_assembly_format(name, level?)` | Just the assembly syntax (L1_SSA / L2_DPS / sync) |
| `get_cpp_intrinsic(name)` | Just the C++ template signature and header path |
| `get_constraints(name, backend?)` | Just the constraints, optionally filtered by backend (a2a3/a5) |
| `get_examples(name, mode?)` | Just the code examples (auto/manual/asm variants) |

### PTO-ISA — Reference documents
| Tool | When to use |
|------|-------------|
| `get_grammar()` | PTO-AS BNF grammar, language spec, and notation conventions |
| `get_family_doc(category)` | Full assembly family document (all ops in a category with AS forms) |
| `get_scalar_ops(name?, subcategory?)` | Scalar arithmetic ops from the MLIR arith dialect (47 ops) |
| `get_control_flow_ops(name?)` | Structured control flow from the MLIR scf dialect (scf.for, scf.if, ...) |
| `get_auxiliary_ops(name?)` | Non-ISA helpers: alloc_tile, make_tensor_view, sync primitives, etc. |
| `get_cce_intrinsics(name, backend?)` | CCE intrinsic call signatures per backend |

### AscendC Documentation
| Tool | When to use |
|------|-------------|
| `ascendc_search_docs(query, max_results, language)` | Full-text search across 1,771 CANN AscendC docs sections |
| `ascendc_get_section(path, language)` | Read a specific section by file path |
| `ascendc_list_chapters()` | List all 7 AscendC chapters with descriptions |
| `ascendc_get_chapter_tree(chapter_path)` | Hierarchy of sections within a chapter |
| `ascendc_search_api(api_name)` | Fast API lookup in the API Reference chapter |
| `ascendc_get_toc()` | Complete AscendC document table of contents |

### CCE Documentation
| Tool | When to use |
|------|-------------|
| `cce_search_docs(query, max_results, language)` | Full-text search across 154 CCE Intrinsic docs sections |
| `cce_get_section(path, language)` | Read a specific section by file path |
| `cce_list_chapters()` | List all 6 CCE chapters with descriptions |
| `cce_get_chapter_tree(chapter_path)` | Hierarchy of sections within a chapter |
| `cce_search_api(api_name)` | Fast API lookup in the API Reference chapter |
| `cce_get_toc()` | Complete CCE document table of contents |

## Recommended Workflow

1. **Orient**: Call `list_categories()` for PTO-ISA, `ascendc_list_chapters()` for AscendC, or `cce_list_chapters()` for CCE.
2. **Find**: Use `search_instructions("multiply")` for PTO-ISA, `ascendc_search_docs("SIMT model")` for AscendC, or `cce_search_docs("vadd")` for CCE.
3. **Inspect**: Call `get_instruction("TMATMUL")` for PTO-ISA, `ascendc_get_section(path)` for AscendC, or `cce_get_section(path)` for CCE.
4. **Drill down**: Use `get_constraints("TMATMUL", backend="a5")` or `get_assembly_format("TMATMUL")` for PTO-ISA. Use `ascendc_get_chapter_tree()` or `cce_get_chapter_tree()` for docs.
5. **APIs**: Use `ascendc_search_api("Matmul")` or `cce_search_api("copy_gm_to_ubuf")` for fast API reference lookups.

## Key Concepts

- **Tile**: A 2D on-chip data block — the core operand for PTO instructions.
  Tiles have a *valid region* (active sub-rectangle) that defines the iteration domain.
- **Assembly levels**: PTO-AS has two forms:
  - **Level 1 (SSA)**: `%dst = pto.tadd %src0, %src1 : (types) -> type` — functional style.
  - **Level 2 (DPS)**: `pto.tadd ins(%src0, %src1 : types) outs(%dst : type)` — explicit buffers.
- **Backends**: Constraints differ per backend. Always check both `a2a3` and `a5` when generating code.
- **C++ intrinsics**: The primary programming interface. Template-parameterized on tile types.
- **AscendC docs**: CANN 9.0.0 operator development guide in Chinese. Use `language="en"` for translated responses.
"""

_ASCENDC_GUIDE = """\
# AscendC Documentation — Agent Guide

CANN 9.0.0 AscendC Operator Development Guide — 1,771 sections across 7 chapters.

## Chapters

| Chapter | Sections | Topic |
|---------|----------|-------|
| 入门教程 | 6 | Getting Started — SIMD + SIMT tutorials |
| 编程指南 | 96 | Programming models, compilation, APIs, hardware |
| 算子实践参考 | 100 | Operator implementation patterns, optimization |
| 兼容性迁移指南 | 5 | Migration and compatibility |
| 可视化专区 | 1 | Visual development tools |
| API参考 | 1,561 | Complete SIMD/SIMT/Utils/AI CPU API reference |
| 目录 | 1 | TOC |

## Language Support

All content is in Chinese. By default, tools return content with a translation
instruction. Use `language="zh"` to receive raw Chinese text.

## Workflow

1. `ascendc_list_chapters()` — see what's available
2. `ascendc_search_docs("SIMT model")` — find relevant sections
3. `ascendc_get_chapter_tree("02_编程指南/02_02_编程模型/")` — see section hierarchy
4. `ascendc_get_section(path)` — read full content
5. `ascendc_search_api("Matmul")` — quick API lookups only in the API Reference
"""

_CCE_GUIDE = """\
# CCE Intrinsic Documentation — Agent Guide

CANN 9.0.0 CCE Intrinsic Development Guide — 154 sections across 6 chapters.

## Chapters

| Chapter | Sections | Topic |
|---------|----------|-------|
| 简介 | 1 | Introduction — overview of CCE Intrinsic and supported hardware |
| 异构编程环境配置与编译器使用 | 1 | Environment setup — BiSheng compiler and configuration |
| CCE Intrinsic介绍 | 6 | Programming model — heterogeneous, kernel functions, SPMD, async pipelines |
| CCE Intrinsic特性 | 5 | Language features — execution space qualifiers, address spaces, macros, scalars |
| CCE Intrinsic样例 | 13 | Examples — Vector, Cube, and Mix operator with host/device code |
| API参考 | 128 | API Reference — vector compute, matrix compute, data movement, synchronization |

## Language Support

All content is in Chinese. By default, tools return content with a translation
instruction. Use `language="zh"` to receive raw Chinese text.

## Tools (6)

| Tool | When to use |
|------|-------------|
| `cce_search_docs(query, max_results, language)` | Full-text search across all CCE docs sections |
| `cce_get_section(path, language)` | Read a specific section by file path |
| `cce_list_chapters()` | List all 6 CCE chapters with descriptions |
| `cce_get_chapter_tree(chapter_path)` | Hierarchy of sections within a chapter |
| `cce_search_api(api_name)` | Fast API lookup in the API Reference chapter |
| `cce_get_toc()` | Complete CCE document table of contents |

## Workflow

1. `cce_list_chapters()` — see what's available
2. `cce_search_docs("vadd")` — find relevant sections
3. `cce_get_chapter_tree("06_API参考/06_03_向量计算接口/")` — see section hierarchy
4. `cce_get_section(path)` — read full content
5. `cce_search_api("copy_gm_to_ubuf")` — quick API lookups only in the API Reference
"""


def create_server(
    docs_path: str | Path,
    ascendc_docs_path: str | Path | None = None,
    ascendc_index_path: str | Path | None = None,
    cce_docs_path: str | Path | None = None,
    cce_index_path: str | Path | None = None,
) -> FastMCP:
    """Create and configure the PTO-ISA + AscendC + CCE MCP server.

    Args:
        docs_path: Path to the ``docs/`` directory of the pto-isa repo.
        ascendc_docs_path: Path to ``data/ascendc_docs/`` (optional).
        ascendc_index_path: Path to ``data/ascendc_index.db`` (optional).
        cce_docs_path: Path to ``data/cce_docs/`` (optional).
        cce_index_path: Path to ``data/cce_index.db`` (optional).

    Returns:
        A fully configured FastMCP server with all tools registered.
    """
    instructions = (
        "PTO-ISA, AscendC, and CCE documentation server. Provides access to PTO Tile Library "
        "instruction documentation, the CANN 9.0.0 AscendC operator development guide, "
        "and the CCE Intrinsic development guide. "
        "Read the resource at npu-coding://guide for a full orientation, or start with "
        "list_categories(), ascendc_list_chapters(), cce_list_chapters(), or search_instructions() to explore."
    )

    mcp = FastMCP(name="npu-coding-mcp", instructions=instructions)

    # --- Agent orientation resource ---
    @mcp.resource(
        "npu-coding://guide",
        name="agent-guide",
        title="PTO-ISA + AscendC Agent Guide",
        description=(
            "Read-this-first orientation for agents: all tools available, recommended workflow, and key concepts."
        ),
        mime_type="text/markdown",
    )
    def agent_guide() -> str:
        return _AGENT_GUIDE

    # --- Load PTO-ISA store ---
    logger.info("Loading ISA documentation from %s ...", docs_path)
    store = load_isa_store(docs_path)
    logger.info("ISA store loaded successfully.")
    register_tools(mcp, store)
    logger.info("PTO-ISA tools registered (14).")

    # --- Load AscendC store (if available) ---
    ascendc_store = None
    if ascendc_docs_path and ascendc_index_path:
        ascendc_docs = Path(ascendc_docs_path)
        ascendc_index = Path(ascendc_index_path)

        # Auto-build index if not present
        if ascendc_docs.exists() and not ascendc_index.exists():
            logger.info("AscendC index not found — building ...")
            from .ascendc.index_builder import build_index

            build_index(ascendc_docs, ascendc_index)
            logger.info("AscendC index built successfully.")

        if ascendc_index.exists():
            from .ascendc.loader import load_store as load_ascendc_store

            ascendc_store = load_ascendc_store(ascendc_docs, ascendc_index)
            from .ascendc.tools import register_tools as register_ascendc_tools

            register_ascendc_tools(mcp, ascendc_store)
            logger.info("AscendC tools registered (6).")

            @mcp.resource(
                "ascendc://guide",
                name="ascendc-guide",
                title="AscendC Documentation Guide",
                description="Orientation guide for the AscendC CANN 9.0.0 documentation.",
                mime_type="text/markdown",
            )
            def ascendc_guide() -> str:
                return _ASCENDC_GUIDE
        else:
            logger.warning("AscendC index not found and could not be built.")
    else:
        logger.info("AscendC documentation not configured — skipping.")

    # --- Load CCE store (if available) ---
    cce_store = None
    if cce_docs_path and cce_index_path:
        cce_docs = Path(cce_docs_path)
        cce_index = Path(cce_index_path)

        if cce_docs.exists() and not cce_index.exists():
            logger.info("CCE index not found — building ...")
            from .cce.index_builder import build_index

            build_index(cce_docs, cce_index)
            logger.info("CCE index built successfully.")

        if cce_index.exists():
            from .cce.loader import load_store as load_cce_store

            cce_store = load_cce_store(cce_docs, cce_index)
            from .cce.tools import register_tools as register_cce_tools

            register_cce_tools(mcp, cce_store)
            logger.info("CCE tools registered (6).")

            @mcp.resource(
                "cce://guide",
                name="cce-guide",
                title="CCE Intrinsic Documentation Guide",
                description="Orientation guide for the CCE Intrinsic CANN 9.0.0 documentation.",
                mime_type="text/markdown",
            )
            def cce_guide() -> str:
                return _CCE_GUIDE
        else:
            logger.warning("CCE index not found and could not be built.")
    else:
        logger.info("CCE documentation not configured — skipping.")

    return mcp
