"""Pydantic models for CCE intrinsic mapping data."""

from __future__ import annotations

from pydantic import BaseModel, Field


class CCEIntrinsicCall(BaseModel):
    """A single CCE intrinsic function call."""

    name: str = Field(description="Intrinsic name, e.g. 'vadd', '__cce_get_tile_ptr'")
    signature: str = Field(description="Full call signature with arguments")
    context: str = Field(default="", description="LLM-enriched one-line description")


class CCEMapping(BaseModel):
    """Per-backend CCE intrinsic mapping for one instruction."""

    source_file: str = Field(description="Path to the NPU header")
    raw_code: str = Field(default="", description="Full preprocessed C++ source code")
    intrinsics: list[CCEIntrinsicCall] = Field(
        default_factory=list, description="CCE intrinsic calls in this instruction"
    )


class InstructionCCEMapping(BaseModel):
    """CCE intrinsic mapping for a PTO-ISA instruction, split by backend."""

    name: str = Field(description="PTO instruction name")
    a2a3: CCEMapping | None = Field(default=None)
    a5: CCEMapping | None = Field(default=None)


class CCEMappingStore(BaseModel):
    """Top-level store for all CCE intrinsic mappings."""

    ptoisa_commit: str = Field(default="", description="Commit hash of pto-isa used for extraction")
    generated_at: str = Field(default="", description="ISO-8601 timestamp")
    instructions: dict[str, InstructionCCEMapping] = Field(default_factory=dict)
