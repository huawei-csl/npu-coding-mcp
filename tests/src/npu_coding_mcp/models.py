"""Pydantic data models for PTO-ISA instruction data."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AssemblyForm(BaseModel):
    """Assembly representation of an instruction at a specific level."""

    level: str = Field(description="AS level: 'L1_SSA', 'L2_DPS', or 'sync'")
    syntax: str = Field(description="Assembly syntax text")


class CppIntrinsic(BaseModel):
    """C++ intrinsic signature and metadata."""

    header: str = Field(default="", description="Header file where the intrinsic is declared")
    signature: str = Field(default="", description="Full C++ template signature")


class ConstraintSet(BaseModel):
    """Backend-specific constraints for an instruction."""

    backend: str = Field(description="Backend identifier: 'a2a3', 'a5', or 'common'")
    dtypes: list[str] = Field(default_factory=list, description="Supported data types")
    layout: str = Field(default="", description="Layout requirements")
    notes: list[str] = Field(default_factory=list, description="Additional constraint notes")
    raw_text: str = Field(default="", description="Raw constraint markdown text")


class CodeExample(BaseModel):
    """A code example for an instruction."""

    mode: str = Field(description="Example mode: 'auto', 'manual', 'asm_auto', 'asm_manual', 'asm_pto'")
    language: str = Field(default="cpp", description="Language of the example: 'cpp' or 'text'")
    code: str = Field(description="The example code")


class InstructionInfo(BaseModel):
    """Complete information about a single PTO-ISA instruction."""

    name: str = Field(description="Instruction name, e.g. 'TADD'")
    category: str = Field(description="Category, e.g. 'Elementwise (Tile-Tile)'")
    summary: str = Field(description="One-line summary in English")
    operands: list[str] = Field(default_factory=list, description="Operand names, e.g. ['dst', 'src0', 'src1']")
    math: str = Field(default="", description="Math interpretation (LaTeX / markdown)")
    assembly_forms: list[AssemblyForm] = Field(default_factory=list, description="Assembly syntax forms")
    cpp_intrinsic: CppIntrinsic | None = Field(default=None, description="C++ intrinsic info")
    constraints: list[ConstraintSet] = Field(default_factory=list, description="Per-backend constraints")
    examples: list[CodeExample] = Field(default_factory=list, description="Code examples")
    raw_markdown: str = Field(default="", description="Full raw markdown of the instruction page")


class ScalarOp(BaseModel):
    """A scalar arithmetic operation (from the arith dialect)."""

    name: str = Field(description="Operation name, e.g. 'arith.addi'")
    mnemonic: str = Field(default="", description="Short mnemonic, e.g. 'addi'")
    subcategory: str = Field(default="", description="Subcategory, e.g. 'Integer Arithmetic'")
    description: str = Field(default="", description="Operation description")
    syntax: str = Field(default="", description="MLIR syntax example")
    example: str = Field(default="", description="Usage example")


class ControlFlowOp(BaseModel):
    """A control flow operation (from the scf dialect)."""

    name: str = Field(description="Operation name, e.g. 'scf.for'")
    mnemonic: str = Field(default="", description="Short mnemonic, e.g. 'for'")
    subcategory: str = Field(default="", description="Subcategory, e.g. 'Loop Operations'")
    description: str = Field(default="", description="Operation description")
    syntax: str = Field(default="", description="MLIR syntax example")
    example: str = Field(default="", description="Usage example")
    operands: str = Field(default="", description="Operand descriptions")
    results: str = Field(default="", description="Result descriptions")


class AuxiliaryOp(BaseModel):
    """A non-ISA auxiliary operation (alloc, sync, view, pointer)."""

    name: str = Field(description="Operation name, e.g. 'make_tensor_view'")
    subcategory: str = Field(default="", description="Subcategory, e.g. 'View Operations'")
    syntax: str = Field(default="", description="Syntax in assembly")
    raw_text: str = Field(default="", description="Raw markdown text for this operation")


class CategoryInfo(BaseModel):
    """Summary info for one instruction category."""

    name: str = Field(description="Category name")
    count: int = Field(description="Number of instructions in this category")
    instructions: list[str] = Field(description="Instruction names in this category")


class AssemblyFamilyDoc(BaseModel):
    """A full assembly family document (e.g. elementwise-ops.md)."""

    filename: str = Field(description="Source filename, e.g. 'elementwise-ops.md'")
    category: str = Field(description="Category name")
    raw_markdown: str = Field(description="Full raw markdown content")


class ISAStore(BaseModel):
    """Top-level data store holding all parsed ISA documentation."""

    instructions: dict[str, InstructionInfo] = Field(
        default_factory=dict, description="Instruction name -> full info (upper-case keys)"
    )
    scalar_ops: dict[str, ScalarOp] = Field(
        default_factory=dict, description="Scalar op name -> info (e.g. 'arith.addi')"
    )
    control_flow_ops: dict[str, ControlFlowOp] = Field(
        default_factory=dict, description="Control flow op name -> info (e.g. 'scf.for')"
    )
    auxiliary_ops: dict[str, AuxiliaryOp] = Field(default_factory=dict, description="Auxiliary op name -> info")
    categories: dict[str, CategoryInfo] = Field(default_factory=dict, description="Category name -> category info")
    assembly_family_docs: dict[str, AssemblyFamilyDoc] = Field(
        default_factory=dict, description="Category name -> assembly family document"
    )
    grammar_bnf: str = Field(default="", description="PTO-AS BNF grammar text")
    grammar_spec: str = Field(default="", description="PTO-AS specification text")
    conventions: str = Field(default="", description="PTO ISA conventions text")
    cce_mappings: dict[str, "InstructionCCEMapping"] = Field(
        default_factory=dict, description="PTO instruction name -> per-backend CCE intrinsic mappings"
    )
    ptoisa_commit: str = Field(default="", description="Commit hash of pto-isa used for CCE mapping")


class CCEIntrinsicCall(BaseModel):
    """A single CCE intrinsic function call."""

    name: str = Field(description="Intrinsic name, e.g. 'vadd', '__cce_get_tile_ptr'")
    signature: str = Field(description="Full call signature with arguments")
    context: str = Field(default="", description="LLM-enriched one-line description")


class CCEMapping(BaseModel):
    """Per-backend CCE intrinsic mapping for one instruction."""

    source_file: str = Field(description="Path to the NPU header")
    raw_code: str = Field(default="", description="Full preprocessed C++ source code")
    intrinsics: list[CCEIntrinsicCall] = Field(default_factory=list)


class InstructionCCEMapping(BaseModel):
    """CCE intrinsic mapping for a PTO-ISA instruction, split by backend."""

    name: str = Field(description="PTO instruction name, e.g. 'TADD'")
    a2a3: CCEMapping | None = Field(default=None, description="A2/A3 backend mapping")
    a5: CCEMapping | None = Field(default=None, description="A5 backend mapping")
