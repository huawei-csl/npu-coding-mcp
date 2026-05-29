"""Load and parse all PTO-ISA documentation from a docs directory at startup."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path

from .models import (
    AssemblyFamilyDoc,
    AssemblyForm,
    AuxiliaryOp,
    CategoryInfo,
    CodeExample,
    ConstraintSet,
    ControlFlowOp,
    CppIntrinsic,
    InstructionInfo,
    ISAStore,
    ScalarOp,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Assembly family files -> category mapping
# ---------------------------------------------------------------------------

_FAMILY_FILE_TO_CATEGORY: dict[str, str] = {
    "elementwise-ops.md": "Elementwise (Tile-Tile)",
    "tile-scalar-ops.md": "Tile-Scalar / Tile-Immediate",
    "axis-ops.md": "Axis Reduce / Expand",
    "memory-ops.md": "Memory (GM <-> Tile)",
    "matrix-ops.md": "Matrix Multiply",
    "data-movement-ops.md": "Data Movement / Layout",
    "complex-ops.md": "Complex",
    "manual-binding-ops.md": "Manual / Resource Binding",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _read_text(path: Path) -> str:
    """Read a file as UTF-8, stripping BOM if present."""
    text = path.read_text(encoding="utf-8-sig")
    return text


def _extract_code_blocks(text: str, language: str | None = None) -> list[tuple[str, str]]:
    """Extract fenced code blocks from markdown.

    Returns list of (language, code) tuples.
    """
    pattern = r"```(\w*)\n(.*?)```"
    blocks: list[tuple[str, str]] = []
    for m in re.finditer(pattern, text, re.DOTALL):
        lang = m.group(1) or ""
        code = m.group(2).rstrip("\n")
        if language is None or lang == language:
            blocks.append((lang, code))
    return blocks


def _extract_section(text: str, heading: str, level: int = 2) -> str:
    """Extract text under a markdown heading (##, ###, etc.) up to the next heading of same or higher level."""
    prefix = "#" * level
    # Match: exactly `level` hashes, a space, then the heading text
    pattern = rf"^{prefix}\s+{re.escape(heading)}\s*$"
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        return ""
    start = m.end()
    # Find the next heading at same level or higher
    next_heading = re.search(rf"^#{{{1},{level}}}\s", text[start:], re.MULTILINE)
    if next_heading:
        return text[start : start + next_heading.start()].strip()
    return text[start:].strip()


def _extract_subsection(text: str, heading: str) -> str:
    """Extract a ### subsection."""
    return _extract_section(text, heading, level=3)


# ---------------------------------------------------------------------------
# ISA per-instruction parser
# ---------------------------------------------------------------------------


def _parse_instruction_md(name: str, text: str, category: str, summary: str, operands: list[str]) -> InstructionInfo:
    """Parse a single ISA instruction markdown page."""

    # --- Math interpretation ---
    math = _extract_section(text, "Math Interpretation")

    # --- Assembly forms ---
    assembly_forms: list[AssemblyForm] = []

    asm_section = _extract_section(text, "Assembly Syntax")
    if asm_section:
        # Synchronous form: code block directly under "Assembly Syntax" before subsections
        sync_match = re.search(r"Synchronous form:\s*\n\s*```text\n(.*?)```", asm_section, re.DOTALL)
        if sync_match:
            assembly_forms.append(AssemblyForm(level="sync", syntax=sync_match.group(1).strip()))

        # AS Level 1 (SSA)
        l1_text = _extract_subsection(asm_section, "AS Level 1 (SSA)")
        if l1_text:
            blocks = _extract_code_blocks(l1_text, "text")
            for _, code in blocks:
                assembly_forms.append(AssemblyForm(level="L1_SSA", syntax=code.strip()))

        # AS Level 2 (DPS)
        l2_text = _extract_subsection(asm_section, "AS Level 2 (DPS)")
        if l2_text:
            blocks = _extract_code_blocks(l2_text, "text")
            for _, code in blocks:
                assembly_forms.append(AssemblyForm(level="L2_DPS", syntax=code.strip()))

    # --- C++ Intrinsic ---
    cpp_intrinsic: CppIntrinsic | None = None
    cpp_section = _extract_section(text, "C++ Intrinsic")
    if cpp_section:
        header = ""
        header_match = re.search(r"Declared in `([^`]+)`", cpp_section)
        if header_match:
            header = header_match.group(1)
        blocks = _extract_code_blocks(cpp_section, "cpp")
        signature = "\n".join(code for _, code in blocks) if blocks else ""
        cpp_intrinsic = CppIntrinsic(header=header, signature=signature)

    # --- Constraints ---
    constraints: list[ConstraintSet] = []
    constraints_section = _extract_section(text, "Constraints")
    if constraints_section:
        for backend_label, backend_key in [("A2A3", "a2a3"), ("A5", "a5")]:
            pattern = rf"\*\*Implementation checks \({backend_label}\)\*\*:\s*\n(.*?)(?=\n- \*\*Implementation checks|\n##|\Z)"
            m = re.search(pattern, constraints_section, re.DOTALL)
            if m:
                raw = m.group(1).strip()
                # Extract dtype info
                dtypes: list[str] = []
                dtype_match = re.search(r"`TileData::DType` must be one of: (.+)", raw)
                if dtype_match:
                    dtypes = [d.strip().strip("`").strip(".") for d in dtype_match.group(1).split(",")]
                # Extract layout
                layout = ""
                layout_match = re.search(r"Tile layout must be (.+)", raw)
                if layout_match:
                    layout = layout_match.group(1).strip().rstrip(".")

                # Collect all bullet points as notes
                notes = [line.strip().lstrip("- ") for line in raw.splitlines() if line.strip().startswith("-")]

                constraints.append(
                    ConstraintSet(backend=backend_key, dtypes=dtypes, layout=layout, notes=notes, raw_text=raw)
                )

    # Also look for "Valid region" constraint
    valid_region_match = (
        re.search(r"\*\*Valid region\*\*:\s*\n(.*?)(?=\n- \*\*|\n##|\Z)", constraints_section, re.DOTALL)
        if constraints_section
        else None
    )
    if valid_region_match:
        raw = valid_region_match.group(1).strip()
        notes = [line.strip().lstrip("- ") for line in raw.splitlines() if line.strip().startswith("-")]
        constraints.append(ConstraintSet(backend="common", notes=notes, raw_text=raw))

    # --- Examples ---
    examples: list[CodeExample] = []
    examples_section = _extract_section(text, "Examples")
    if examples_section:
        for mode_label, mode_key in [("Auto", "auto"), ("Manual", "manual")]:
            sub = _extract_subsection(examples_section, mode_label)
            if sub:
                blocks = _extract_code_blocks(sub, "cpp")
                for _, code in blocks:
                    examples.append(CodeExample(mode=mode_key, language="cpp", code=code))

    asm_examples_section = _extract_section(text, "ASM Form Examples")
    if asm_examples_section:
        for mode_label, mode_key in [
            ("Auto Mode", "asm_auto"),
            ("Manual Mode", "asm_manual"),
            ("PTO Assembly Form", "asm_pto"),
        ]:
            sub = _extract_subsection(asm_examples_section, mode_label)
            if sub:
                blocks = _extract_code_blocks(sub, "text")
                for _, code in blocks:
                    examples.append(CodeExample(mode=mode_key, language="text", code=code))

    return InstructionInfo(
        name=name,
        category=category,
        summary=summary,
        operands=operands,
        math=math,
        assembly_forms=assembly_forms,
        cpp_intrinsic=cpp_intrinsic,
        constraints=constraints,
        examples=examples,
        raw_markdown=text,
    )


# ---------------------------------------------------------------------------
# Scalar arith ops parser
# ---------------------------------------------------------------------------


def _parse_scalar_arith_ops(text: str) -> dict[str, ScalarOp]:
    """Parse scalar-arith-ops.md into ScalarOp models."""
    ops: dict[str, ScalarOp] = {}
    current_subcategory = ""

    # Split into sections by ### headings
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        # Track ## subcategories
        if line.startswith("## ") and not line.startswith("### "):
            current_subcategory = line[3:].strip()
            i += 1
            continue

        # Parse ### op headings like "### arith.addi - Integer Addition"
        m = re.match(r"^### (arith\.\w+|[\w.]+)\s*-?\s*(.*)", line)
        if m:
            op_name = m.group(1).strip()
            description = m.group(2).strip() if m.group(2) else ""
            mnemonic = op_name.split(".")[-1] if "." in op_name else op_name

            # Gather the full block until next ### or ##
            block_start = i + 1
            i += 1
            while (
                i < len(lines)
                and not lines[i].startswith("### ")
                and not (lines[i].startswith("## ") and not lines[i].startswith("### "))
            ):
                i += 1

            block = "\n".join(lines[block_start:i])

            # Extract description if present in block
            desc_match = re.search(r"\*\*Description:\*\*\s*(.+)", block)
            if desc_match:
                description = desc_match.group(1).strip()

            # Extract syntax code block
            syntax = ""
            syntax_section = re.search(r"\*\*Syntax:\*\*\s*\n\s*```\w*\n(.*?)```", block, re.DOTALL)
            if syntax_section:
                syntax = syntax_section.group(1).strip()

            # Extract example
            example = ""
            example_section = re.search(r"\*\*Example:\*\*\s*\n\s*```\w*\n(.*?)```", block, re.DOTALL)
            if example_section:
                example = example_section.group(1).strip()

            ops[op_name] = ScalarOp(
                name=op_name,
                mnemonic=mnemonic,
                subcategory=current_subcategory,
                description=description,
                syntax=syntax,
                example=example,
            )
            continue

        i += 1

    return ops


# ---------------------------------------------------------------------------
# Control flow ops parser
# ---------------------------------------------------------------------------


def _parse_control_flow_ops(text: str) -> dict[str, ControlFlowOp]:
    """Parse control-flow-ops.md into ControlFlowOp models."""
    ops: dict[str, ControlFlowOp] = {}
    current_subcategory = ""

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("## ") and not line.startswith("### "):
            current_subcategory = line[3:].strip()
            i += 1
            continue

        # Parse ### op headings like "### scf.for - For Loop"
        m = re.match(r"^### (scf\.\w+|[\w.]+)\s*-?\s*(.*)", line)
        if m:
            op_name = m.group(1).strip()
            title = m.group(2).strip() if m.group(2) else ""
            mnemonic = op_name.split(".")[-1] if "." in op_name else op_name

            block_start = i + 1
            i += 1
            while (
                i < len(lines)
                and not lines[i].startswith("### ")
                and not (lines[i].startswith("## ") and not lines[i].startswith("### "))
            ):
                i += 1

            block = "\n".join(lines[block_start:i])

            description = ""
            desc_match = re.search(r"\*\*Description:\*\*\s*(.+)", block)
            if desc_match:
                description = desc_match.group(1).strip()
            elif title:
                description = title

            syntax = ""
            syntax_section = re.search(r"\*\*Syntax:\*\*\s*\n\s*```\w*\n(.*?)```", block, re.DOTALL)
            if syntax_section:
                syntax = syntax_section.group(1).strip()

            example = ""
            example_section = re.search(r"\*\*Example:\*\*\s*\n\s*```\w*\n(.*?)```", block, re.DOTALL)
            if example_section:
                example = example_section.group(1).strip()

            operands_text = ""
            operands_section = re.search(r"\*\*Operands:\*\*\s*\n(.*?)(?=\n\*\*|\n---|\Z)", block, re.DOTALL)
            if operands_section:
                operands_text = operands_section.group(1).strip()

            results_text = ""
            results_section = re.search(r"\*\*Results:\*\*\s*\n(.*?)(?=\n\*\*|\n---|\Z)", block, re.DOTALL)
            if results_section:
                results_text = results_section.group(1).strip()

            ops[op_name] = ControlFlowOp(
                name=op_name,
                mnemonic=mnemonic,
                subcategory=current_subcategory,
                description=description,
                syntax=syntax,
                example=example,
                operands=operands_text,
                results=results_text,
            )
            continue

        i += 1

    return ops


# ---------------------------------------------------------------------------
# Auxiliary ops parser
# ---------------------------------------------------------------------------


def _parse_auxiliary_ops(text: str) -> dict[str, AuxiliaryOp]:
    """Parse nonisa-ops.md into AuxiliaryOp models."""
    ops: dict[str, AuxiliaryOp] = {}
    current_subcategory = ""

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        # Track ## level subcategories (e.g. "## 2. View Operations")
        if line.startswith("## ") and not line.startswith("### "):
            # Strip leading number prefix like "2. "
            sub = re.sub(r"^##\s+\d+\.\s*", "", line).strip()
            current_subcategory = sub
            i += 1
            continue

        # Parse ### headings like "### 2.1 `make_tensor_view`"
        m = re.match(r"^###\s+[\d.]*\s*`?(\w+)`?\s*(?:\(.*\))?\s*$", line)
        if m:
            op_name = m.group(1).strip()

            block_start = i + 1
            i += 1
            while (
                i < len(lines)
                and not lines[i].startswith("### ")
                and not (lines[i].startswith("## ") and not lines[i].startswith("### "))
            ):
                i += 1

            block = "\n".join(lines[block_start:i])

            # Extract syntax from code blocks
            syntax_parts: list[str] = []
            for _, code in _extract_code_blocks(block):
                syntax_parts.append(code.strip())
            syntax = "\n\n".join(syntax_parts)

            ops[op_name] = AuxiliaryOp(
                name=op_name,
                subcategory=current_subcategory,
                syntax=syntax,
                raw_text=block.strip(),
            )
            continue

        i += 1

    return ops


# ---------------------------------------------------------------------------
# Main loader
# ---------------------------------------------------------------------------


def load_isa_store(docs_path: str | Path) -> ISAStore:
    """Load all PTO-ISA documentation from the given docs directory.

    Args:
        docs_path: Path to the ``docs/`` directory of the pto-isa repo.

    Returns:
        A fully populated ISAStore.
    """
    docs = Path(docs_path)
    if not docs.is_dir():
        raise FileNotFoundError(f"docs_path does not exist or is not a directory: {docs}")

    isa_dir = docs / "isa"
    assembly_dir = docs / "assembly"
    comm_dir = isa_dir / "comm"

    store = ISAStore()

    # -----------------------------------------------------------------------
    # 1. Load manifest (JSON despite .yaml extension)
    # -----------------------------------------------------------------------
    manifest_path = isa_dir / "manifest.yaml"
    manifest_entries: list[dict] = []
    if manifest_path.exists():
        raw = _read_text(manifest_path)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            import yaml

            data = yaml.safe_load(raw)
        manifest_entries = data.get("instructions", [])
        logger.info("Loaded manifest with %d entries", len(manifest_entries))
    else:
        logger.warning("manifest.yaml not found at %s", manifest_path)

    # Build a quick lookup: instruction name -> manifest entry
    manifest_lookup: dict[str, dict] = {}
    for entry in manifest_entries:
        manifest_lookup[entry["instruction"]] = entry

    # -----------------------------------------------------------------------
    # 2. Parse per-instruction ISA pages
    # -----------------------------------------------------------------------
    # English-only instruction markdown files (skip _zh.md, README.md)
    isa_md_files = sorted(
        p
        for p in isa_dir.glob("*.md")
        if not p.name.endswith("_zh.md") and p.name != "README.md" and p.name != "README_zh.md"
    )
    # Also include comm/ instructions
    if comm_dir.is_dir():
        isa_md_files += sorted(
            p
            for p in comm_dir.glob("*.md")
            if not p.name.endswith("_zh.md") and p.name != "README.md" and p.name != "README_zh.md"
        )

    for md_file in isa_md_files:
        name = md_file.stem  # e.g. "TADD"
        text = _read_text(md_file)

        # Look up manifest data
        mentry = manifest_lookup.get(name, {})
        category = mentry.get("category", "Communication" if md_file.parent == comm_dir else "Unknown")
        summary = mentry.get("summary_en", "")
        operands = mentry.get("operands", [])

        # If no summary from manifest, try extracting from intro section
        if not summary:
            intro = _extract_section(text, "Introduction")
            if intro:
                summary = intro.splitlines()[0].strip()

        info = _parse_instruction_md(name, text, category, summary, operands)
        store.instructions[name] = info

    logger.info("Parsed %d ISA instruction pages", len(store.instructions))

    # -----------------------------------------------------------------------
    # 3. Build category index
    # -----------------------------------------------------------------------
    cat_map: dict[str, list[str]] = {}
    for name, info in store.instructions.items():
        cat_map.setdefault(info.category, []).append(name)
    for cat_name, instr_names in cat_map.items():
        store.categories[cat_name] = CategoryInfo(
            name=cat_name,
            count=len(instr_names),
            instructions=sorted(instr_names),
        )

    # -----------------------------------------------------------------------
    # 4. Load assembly family docs
    # -----------------------------------------------------------------------
    for filename, category in _FAMILY_FILE_TO_CATEGORY.items():
        fpath = assembly_dir / filename
        if fpath.exists():
            raw = _read_text(fpath)
            store.assembly_family_docs[category] = AssemblyFamilyDoc(
                filename=filename,
                category=category,
                raw_markdown=raw,
            )

    # -----------------------------------------------------------------------
    # 5. Enrich instructions with assembly forms from family docs
    #    (for instructions whose own ISA page might have incomplete AS forms)
    # -----------------------------------------------------------------------
    for category, fam_doc in store.assembly_family_docs.items():
        _enrich_from_family_doc(store, fam_doc)

    # -----------------------------------------------------------------------
    # 6. Parse scalar arith ops
    # -----------------------------------------------------------------------
    scalar_path = assembly_dir / "scalar-arith-ops.md"
    if scalar_path.exists():
        store.scalar_ops = _parse_scalar_arith_ops(_read_text(scalar_path))
        logger.info("Parsed %d scalar arith ops", len(store.scalar_ops))

    # -----------------------------------------------------------------------
    # 7. Parse control flow ops
    # -----------------------------------------------------------------------
    cf_path = assembly_dir / "control-flow-ops.md"
    if cf_path.exists():
        store.control_flow_ops = _parse_control_flow_ops(_read_text(cf_path))
        logger.info("Parsed %d control flow ops", len(store.control_flow_ops))

    # -----------------------------------------------------------------------
    # 8. Parse auxiliary / non-ISA ops
    # -----------------------------------------------------------------------
    aux_path = assembly_dir / "nonisa-ops.md"
    if aux_path.exists():
        store.auxiliary_ops = _parse_auxiliary_ops(_read_text(aux_path))
        logger.info("Parsed %d auxiliary ops", len(store.auxiliary_ops))

    # -----------------------------------------------------------------------
    # 9. Load grammar and spec files
    # -----------------------------------------------------------------------
    bnf_path = assembly_dir / "PTO-AS.bnf"
    if bnf_path.exists():
        store.grammar_bnf = _read_text(bnf_path)

    spec_path = assembly_dir / "PTO-AS.md"
    if spec_path.exists():
        store.grammar_spec = _read_text(spec_path)

    conv_path = assembly_dir / "conventions.md"
    if conv_path.exists():
        store.conventions = _read_text(conv_path)

    # -----------------------------------------------------------------------
    # 10. Load CCE intrinsic mapping (pre-built by build_cce_mapping.py)
    # -----------------------------------------------------------------------
    _load_cce_mapping(store)

    logger.info(
        "ISAStore loaded: %d instructions, %d categories, %d scalar ops, %d cf ops, %d aux ops, %d cce mappings",
        len(store.instructions),
        len(store.categories),
        len(store.scalar_ops),
        len(store.control_flow_ops),
        len(store.auxiliary_ops),
        len(store.cce_mappings),
    )

    return store


def _load_cce_mapping(store: ISAStore) -> None:
    """Load pre-built CCE intrinsic mapping from data/cce_mapping.json."""
    json_path = Path(__file__).parent.parent.parent / "data" / "cce_mapping.json"

    if not json_path.exists():
        logger.info("cce_mapping.json not found — CCE intrinsic tool will be unavailable")
        return

    from .models import InstructionCCEMapping

    try:
        data = json.loads(_read_text(json_path))
        store.ptoisa_commit = data.get("ptoisa_commit", "")
        for name, mdata in data.get("instructions", {}).items():
            store.cce_mappings[name] = InstructionCCEMapping(**mdata)
        logger.info("Loaded %d CCE intrinsic mappings (commit %s)", len(store.cce_mappings), store.ptoisa_commit[:8])
    except Exception:
        logger.warning("Failed to parse cce_mapping.json — CCE intrinsic tool will be unavailable")


# ---------------------------------------------------------------------------
# Enrich instructions from assembly family docs
# ---------------------------------------------------------------------------


def _enrich_from_family_doc(store: ISAStore, fam_doc: AssemblyFamilyDoc) -> None:
    """Parse a family assembly doc and fill in any missing assembly forms on instructions."""
    text = fam_doc.raw_markdown

    # Split into per-instruction blocks by ### INSTR_NAME headings
    blocks = re.split(r"^### (\w+)", text, flags=re.MULTILINE)
    # blocks[0] = preamble, then pairs of (name, content)
    for i in range(1, len(blocks) - 1, 2):
        instr_name = blocks[i].strip()
        block_text = blocks[i + 1]

        if instr_name not in store.instructions:
            continue

        info = store.instructions[instr_name]

        # Only fill if the instruction has no assembly forms yet
        if info.assembly_forms:
            continue

        # Extract AS Level 1 (SSA)
        l1_match = re.search(r"\*\*AS Level 1 \(SSA\):\*\*\s*\n\s*```text\n(.*?)```", block_text, re.DOTALL)
        if l1_match:
            info.assembly_forms.append(AssemblyForm(level="L1_SSA", syntax=l1_match.group(1).strip()))

        # Extract AS Level 2 (DPS)
        l2_match = re.search(r"\*\*AS Level 2 \(DPS\):\*\*\s*\n\s*```text\n(.*?)```", block_text, re.DOTALL)
        if l2_match:
            info.assembly_forms.append(AssemblyForm(level="L2_DPS", syntax=l2_match.group(1).strip()))
