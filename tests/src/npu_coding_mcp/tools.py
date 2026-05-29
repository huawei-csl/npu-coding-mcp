"""MCP tool definitions for the PTO-ISA server.

All 14 tools are registered on the FastMCP server instance and operate on
the in-memory ISAStore that was populated at startup.
"""

from __future__ import annotations

import difflib
from typing import Any

from fastmcp import FastMCP

from .models import ISAStore

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

_TOOL_ANNOTATIONS = {
    "readOnlyHint": True,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": False,
}


def _suggest_similar(name: str, known: list[str], n: int = 5) -> list[str]:
    """Return up to *n* similar names from *known*."""
    return difflib.get_close_matches(name.upper(), [k.upper() for k in known], n=n, cutoff=0.4)


def _not_found_msg(kind: str, name: str, known: list[str]) -> str:
    similar = _suggest_similar(name, known)
    msg = f"{kind} '{name}' not found."
    if similar:
        msg += f" Did you mean: {', '.join(similar)}?"
    msg += " Use list_instructions() or list_categories() to browse available items."
    return msg


# ---------------------------------------------------------------------------
# Tool registration
# ---------------------------------------------------------------------------


def _intrinsic_in_lines(lines: list[str], start: int, end: int, intrinsics: list[Any]) -> list[str]:
    """Return which intrinsic names appear in the given line range."""
    block = "\n".join(lines[start:end])
    found = []
    for ic in intrinsics:
        ic_name = getattr(ic, "name", "")
        if ic_name and ic_name in block:
            found.append(ic_name)
    # Also detect Op::BinInstr template calls (expands to the actual intrinsic)
    if "BinInstr" in block and not found:
        found = ["Op::BinInstr → " + ic.name for ic in intrinsics]
    return found


def _extract_loops(raw_code: str, intrinsics: list[Any]) -> list[dict[str, Any]]:
    """Extract loop structures from raw CCE code.

    Returns a list of loop objects with their loop variable, bounds,
    and which intrinsics appear inside the loop body.
    """
    if not raw_code:
        return []

    lines = raw_code.splitlines()
    loops: list[dict[str, Any]] = []
    depth = 0
    loop_stack: list[dict[str, Any]] = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        depth_before = depth

        if stripped.startswith("for (") or stripped.startswith("for("):
            try:
                inner = stripped[stripped.index("(") + 1 : stripped.rindex(")")]
                parts = inner.split(";")
                loop_info: dict[str, Any] = {
                    "line": i,
                    "init": parts[0].strip() if len(parts) > 0 else "",
                    "cond": parts[1].strip() if len(parts) > 1 else "",
                    "incr": parts[2].strip() if len(parts) > 2 else "",
                    "depth": depth + 1,
                }
                loop_stack.append(loop_info)
            except (ValueError, IndexError):
                pass

        depth += stripped.count("{") - stripped.count("}")

        if depth < depth_before:
            while loop_stack and loop_stack[-1].get("depth", 0) > depth:
                lp = loop_stack.pop()
                lp["body_lines"] = f"{lp['line']}-{i}"
                lp["body_intrinsics"] = _intrinsic_in_lines(lines, lp["line"], i + 1, intrinsics)
                loops.append(lp)

    while loop_stack:
        lp = loop_stack.pop()
        lp["body_lines"] = f"{lp['line']}-{len(lines)}"
        lp["body_intrinsics"] = _intrinsic_in_lines(lines, lp["line"], len(lines), intrinsics)
        loops.append(lp)

    summary: dict[str, list[dict[str, Any]]] = {}
    for lp in loops:
        key = f"depth_{lp['depth']}"
        summary.setdefault(key, []).append(lp)

    result = []
    for depth_key in sorted(summary.keys()):
        result.append(
            {
                "depth": int(depth_key.split("_")[1]),
                "count": len(summary[depth_key]),
                "structures": [
                    {
                        "init": lp["init"],
                        "cond": lp["cond"],
                        "incr": lp["incr"],
                        "body_intrinsics": lp["body_intrinsics"],
                    }
                    for lp in summary[depth_key][:3]
                ],
            }
        )

    return result


# ---------------------------------------------------------------------------
# Tool registration (continued)
# ---------------------------------------------------------------------------


def register_tools(mcp: FastMCP, store: ISAStore) -> None:
    """Register all 14 PTO-ISA tools on the given FastMCP server."""

    # -----------------------------------------------------------------------
    # 1. list_categories
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def list_categories() -> dict[str, Any]:
        """List all PTO-ISA instruction categories with counts.

        Returns a mapping of category name -> {count, instructions[]}.
        Use this first to understand what instruction families exist.
        """
        result: dict[str, Any] = {}
        for cat_name, cat_info in sorted(store.categories.items()):
            result[cat_name] = {
                "count": cat_info.count,
                "instructions": cat_info.instructions,
            }
        return result

    # -----------------------------------------------------------------------
    # 2. list_instructions
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def list_instructions(category: str | None = None) -> list[dict[str, str]]:
        """List PTO-ISA instructions, optionally filtered by category.

        Args:
            category: If provided, only list instructions in this category.
                      Case-insensitive partial match is supported.

        Returns a list of {name, category, summary} dicts.
        """
        results: list[dict[str, str]] = []
        for name, info in sorted(store.instructions.items()):
            if category:
                if category.lower() not in info.category.lower():
                    continue
            results.append(
                {
                    "name": info.name,
                    "category": info.category,
                    "summary": info.summary,
                }
            )
        return results

    # -----------------------------------------------------------------------
    # 3. get_instruction
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_instruction(name: str) -> dict[str, Any]:
        """Get full detail for one PTO-ISA instruction (all representations).

        Args:
            name: Instruction name, e.g. 'TADD', 'TMATMUL'. Case-insensitive.

        Returns all available information: summary, math, assembly forms,
        C++ intrinsic, constraints, examples, and raw markdown.
        """
        key = name.upper()
        info = store.instructions.get(key)
        if not info:
            return {"error": _not_found_msg("Instruction", name, list(store.instructions.keys()))}
        return info.model_dump()

    # -----------------------------------------------------------------------
    # 4. get_assembly_format
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_assembly_format(name: str, level: str | None = None) -> dict[str, Any]:
        """Get assembly syntax for a PTO-ISA instruction.

        Args:
            name: Instruction name, e.g. 'TADD'. Case-insensitive.
            level: Optional filter: 'L1_SSA', 'L2_DPS', 'sync', or None for all.

        Returns the assembly form(s) for the instruction.
        """
        key = name.upper()
        info = store.instructions.get(key)
        if not info:
            return {"error": _not_found_msg("Instruction", name, list(store.instructions.keys()))}

        forms = info.assembly_forms
        if level:
            forms = [f for f in forms if f.level.upper() == level.upper()]

        return {
            "instruction": key,
            "assembly_forms": [f.model_dump() for f in forms],
        }

    # -----------------------------------------------------------------------
    # 5. get_cpp_intrinsic
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_cpp_intrinsic(name: str) -> dict[str, Any]:
        """Get the C++ intrinsic signature and header for a PTO-ISA instruction.

        Args:
            name: Instruction name, e.g. 'TADD'. Case-insensitive.

        Returns the header file path and C++ template signature.
        """
        key = name.upper()
        info = store.instructions.get(key)
        if not info:
            return {"error": _not_found_msg("Instruction", name, list(store.instructions.keys()))}

        if not info.cpp_intrinsic:
            return {
                "instruction": key,
                "cpp_intrinsic": None,
                "note": "No C++ intrinsic documented for this instruction.",
            }

        return {
            "instruction": key,
            "cpp_intrinsic": info.cpp_intrinsic.model_dump(),
        }

    # -----------------------------------------------------------------------
    # 6. get_constraints
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_constraints(name: str, backend: str | None = None) -> dict[str, Any]:
        """Get constraint details for a PTO-ISA instruction, optionally per backend.

        Args:
            name: Instruction name, e.g. 'TADD'. Case-insensitive.
            backend: Optional filter: 'a2a3', 'a5', 'common', or None for all.

        Returns constraint sets (dtypes, layout, notes) for the instruction.
        """
        key = name.upper()
        info = store.instructions.get(key)
        if not info:
            return {"error": _not_found_msg("Instruction", name, list(store.instructions.keys()))}

        constraints = info.constraints
        if backend:
            constraints = [c for c in constraints if c.backend.lower() == backend.lower()]

        return {
            "instruction": key,
            "constraints": [c.model_dump() for c in constraints],
        }

    # -----------------------------------------------------------------------
    # 7. search_instructions
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def search_instructions(query: str) -> list[dict[str, str]]:
        """Full-text search across instruction names, summaries, and categories.

        Args:
            query: Search string (case-insensitive). Matches against name, summary, and category.

        Returns a list of matching {name, category, summary} dicts.
        """
        q = query.lower()
        results: list[dict[str, str]] = []
        for name, info in sorted(store.instructions.items()):
            if q in info.name.lower() or q in info.summary.lower() or q in info.category.lower():
                results.append(
                    {
                        "name": info.name,
                        "category": info.category,
                        "summary": info.summary,
                    }
                )
        return results

    # -----------------------------------------------------------------------
    # 8. get_grammar
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_grammar() -> dict[str, str]:
        """Get the PTO-AS BNF grammar, language specification, and conventions.

        Returns the full BNF grammar text, the PTO-AS spec, and conventions document.
        """
        return {
            "bnf_grammar": store.grammar_bnf,
            "specification": store.grammar_spec,
            "conventions": store.conventions,
        }

    # -----------------------------------------------------------------------
    # 9. get_scalar_ops
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_scalar_ops(
        name: str | None = None, subcategory: str | None = None
    ) -> dict[str, Any] | list[dict[str, Any]]:
        """Get scalar arithmetic operations (arith dialect).

        Args:
            name: Optional specific op name, e.g. 'arith.addi'. Case-insensitive.
            subcategory: Optional filter by subcategory, e.g. 'Integer Arithmetic'.

        If name is provided, returns the full detail for that op.
        Otherwise, returns a list of all matching ops.
        """
        if name:
            # Try exact match (case-insensitive)
            for op_name, op in store.scalar_ops.items():
                if op_name.lower() == name.lower() or op.mnemonic.lower() == name.lower():
                    return op.model_dump()
            return {"error": _not_found_msg("Scalar op", name, list(store.scalar_ops.keys()))}

        results: list[dict[str, Any]] = []
        for _, op in sorted(store.scalar_ops.items()):
            if subcategory and subcategory.lower() not in op.subcategory.lower():
                continue
            results.append(op.model_dump())
        return results

    # -----------------------------------------------------------------------
    # 10. get_control_flow_ops
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_control_flow_ops(name: str | None = None) -> dict[str, Any] | list[dict[str, Any]]:
        """Get control flow operations (scf dialect).

        Args:
            name: Optional specific op name, e.g. 'scf.for'. Case-insensitive.

        If name is provided, returns full detail. Otherwise returns all ops.
        """
        if name:
            for op_name, op in store.control_flow_ops.items():
                if op_name.lower() == name.lower() or op.mnemonic.lower() == name.lower():
                    return op.model_dump()
            return {"error": _not_found_msg("Control flow op", name, list(store.control_flow_ops.keys()))}

        return [op.model_dump() for _, op in sorted(store.control_flow_ops.items())]

    # -----------------------------------------------------------------------
    # 11. get_auxiliary_ops
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_auxiliary_ops(name: str | None = None) -> dict[str, Any] | list[dict[str, Any]]:
        """Get non-ISA auxiliary operations (alloc, sync, view, pointer).

        Args:
            name: Optional specific op name, e.g. 'make_tensor_view'. Case-insensitive.

        If name is provided, returns full detail. Otherwise returns all ops.
        """
        if name:
            for op_name, op in store.auxiliary_ops.items():
                if op_name.lower() == name.lower():
                    return op.model_dump()
            return {"error": _not_found_msg("Auxiliary op", name, list(store.auxiliary_ops.keys()))}

        return [op.model_dump() for _, op in sorted(store.auxiliary_ops.items())]

    # -----------------------------------------------------------------------
    # 12. get_examples
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_examples(name: str, mode: str | None = None) -> dict[str, Any]:
        """Get code examples for a PTO-ISA instruction.

        Args:
            name: Instruction name, e.g. 'TADD'. Case-insensitive.
            mode: Optional filter: 'auto', 'manual', 'asm_auto', 'asm_manual', 'asm_pto'.

        Returns the code examples for the instruction.
        """
        key = name.upper()
        info = store.instructions.get(key)
        if not info:
            return {"error": _not_found_msg("Instruction", name, list(store.instructions.keys()))}

        examples = info.examples
        if mode:
            examples = [e for e in examples if e.mode.lower() == mode.lower()]

        return {
            "instruction": key,
            "examples": [e.model_dump() for e in examples],
        }

    # -----------------------------------------------------------------------
    # 13. get_family_doc
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_family_doc(category: str) -> dict[str, Any]:
        """Get the full assembly family document for a category.

        Args:
            category: Category name, e.g. 'Elementwise (Tile-Tile)'.
                      Case-insensitive partial match is supported.

        Returns the full raw markdown for the assembly family document.
        """
        # Try exact match first
        for cat_name, doc in store.assembly_family_docs.items():
            if cat_name.lower() == category.lower():
                return doc.model_dump()

        # Try partial match
        for cat_name, doc in store.assembly_family_docs.items():
            if category.lower() in cat_name.lower():
                return doc.model_dump()

        available = list(store.assembly_family_docs.keys())
        return {
            "error": f"No assembly family document found for category '{category}'.",
            "available_categories": available,
            "hint": "Use list_categories() to see all categories.",
        }

    # -----------------------------------------------------------------------
    # 14. get_cce_intrinsics
    # -----------------------------------------------------------------------
    @mcp.tool(annotations=_TOOL_ANNOTATIONS)
    def get_cce_intrinsics(name: str, backend: str | None = None) -> dict[str, Any]:
        """Get the CCE intrinsic call signatures for a PTO-ISA instruction.

        Maps each PTO-ISA API call to the underlying CCE (CANN Compute Engine)
        intrinsic function calls used in the NPU backend implementations.

        Args:
            name: Instruction name, e.g. 'TADD'. Case-insensitive.
            backend: Optional filter: 'a2a3', 'a5', or None for both.

        Returns per-backend CCE intrinsic names, full call signatures, and
        the preprocessed C++ source code.
        """
        key = name.upper()
        m = store.cce_mappings.get(key)
        if not m:
            similar = _suggest_similar(name, list(store.cce_mappings.keys()))
            msg = f"CCE mapping for '{name}' not found."
            if similar:
                msg += f" Did you mean: {', '.join(similar)}?"
            if not store.cce_mappings:
                msg += " No CCE mappings loaded — run build_cce_mapping.py to generate them."
            return {"error": msg}

        result: dict[str, Any] = {"instruction": key}

        def _dump(bm):
            if bm is None:
                return None
            loops = _extract_loops(bm.raw_code, bm.intrinsics)
            return {
                "source_file": bm.source_file,
                "intrinsics": [c.model_dump() for c in bm.intrinsics],
                "raw_code": bm.raw_code,
                "loops": loops,
            }

        if backend:
            backend_lower = backend.lower()
            if backend_lower not in ("a2a3", "a5"):
                return {"error": f"Invalid backend '{backend}'. Must be 'a2a3' or 'a5'."}
            filtered = _dump(m.a2a3 if backend_lower == "a2a3" else m.a5)
            if filtered is None:
                return {"error": f"No {backend.upper()} CCE mapping for '{key}'."}
            result[backend_lower] = filtered
        else:
            result["a2a3"] = _dump(m.a2a3)
            result["a5"] = _dump(m.a5)

        return result
