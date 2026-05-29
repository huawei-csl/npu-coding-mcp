"""Tests for the PTO-ISA MCP loader, running against the real docs directory."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

# The real docs path — set via PTOISA_DOCS_PATH env var, or default to sibling repo
_DEFAULT_DOCS = Path(__file__).resolve().parent.parent.parent.parent / "pto-isa" / "docs"
DOCS_PATH = Path(os.environ.get("PTOISA_DOCS_PATH", str(_DEFAULT_DOCS)))


@pytest.fixture(scope="module")
def store():
    """Load the ISA store once for the entire test module."""
    if not DOCS_PATH.is_dir():
        pytest.skip(f"Docs directory not found: {DOCS_PATH}")
    from npu_coding_mcp.loader import load_isa_store

    return load_isa_store(DOCS_PATH)


# ---------------------------------------------------------------------------
# Loader tests
# ---------------------------------------------------------------------------


class TestLoaderBasics:
    def test_instructions_loaded(self, store):
        assert len(store.instructions) >= 90, f"Expected >=90 instructions, got {len(store.instructions)}"

    def test_categories_populated(self, store):
        assert len(store.categories) >= 5, f"Expected >=5 categories, got {len(store.categories)}"

    def test_scalar_ops_loaded(self, store):
        assert len(store.scalar_ops) >= 40, f"Expected >=40 scalar ops, got {len(store.scalar_ops)}"

    def test_control_flow_ops_loaded(self, store):
        assert len(store.control_flow_ops) >= 5, f"Expected >=5 CF ops, got {len(store.control_flow_ops)}"

    def test_auxiliary_ops_loaded(self, store):
        assert len(store.auxiliary_ops) >= 5, f"Expected >=5 aux ops, got {len(store.auxiliary_ops)}"

    def test_grammar_loaded(self, store):
        assert len(store.grammar_bnf) > 100
        assert len(store.grammar_spec) > 100
        assert len(store.conventions) > 50

    def test_assembly_family_docs_loaded(self, store):
        assert len(store.assembly_family_docs) >= 7


class TestInstructionParsing:
    def test_tadd_exists(self, store):
        assert "TADD" in store.instructions

    def test_tadd_category(self, store):
        assert store.instructions["TADD"].category == "Elementwise (Tile-Tile)"

    def test_tadd_summary(self, store):
        assert "add" in store.instructions["TADD"].summary.lower()

    def test_tadd_operands(self, store):
        assert store.instructions["TADD"].operands == ["dst", "src0", "src1"]

    def test_tadd_assembly_forms(self, store):
        forms = store.instructions["TADD"].assembly_forms
        assert len(forms) >= 2
        levels = {f.level for f in forms}
        assert "L1_SSA" in levels
        assert "L2_DPS" in levels

    def test_tadd_cpp_intrinsic(self, store):
        cpp = store.instructions["TADD"].cpp_intrinsic
        assert cpp is not None
        assert "TADD" in cpp.signature
        assert cpp.header != ""

    def test_tadd_constraints(self, store):
        constraints = store.instructions["TADD"].constraints
        assert len(constraints) >= 2
        backends = {c.backend for c in constraints}
        assert "a2a3" in backends
        assert "a5" in backends

    def test_tadd_examples(self, store):
        examples = store.instructions["TADD"].examples
        assert len(examples) >= 2
        modes = {e.mode for e in examples}
        assert "auto" in modes
        assert "manual" in modes

    def test_tadd_math(self, store):
        assert "src0" in store.instructions["TADD"].math or "dst" in store.instructions["TADD"].math

    def test_tmatmul_exists(self, store):
        assert "TMATMUL" in store.instructions

    def test_tmatmul_category(self, store):
        assert store.instructions["TMATMUL"].category == "Matrix Multiply"

    def test_tmatmul_constraints_a5(self, store):
        constraints = store.instructions["TMATMUL"].constraints
        a5 = [c for c in constraints if c.backend == "a5"]
        assert len(a5) >= 1
        # A5 should have raw_text with useful content
        assert len(a5[0].raw_text) > 20


class TestScalarOps:
    def test_addi_exists(self, store):
        assert "arith.addi" in store.scalar_ops

    def test_addi_has_syntax(self, store):
        op = store.scalar_ops["arith.addi"]
        assert "arith.addi" in op.syntax

    def test_addi_subcategory(self, store):
        op = store.scalar_ops["arith.addi"]
        assert "Integer" in op.subcategory or "Arithmetic" in op.subcategory


class TestControlFlowOps:
    def test_scf_for_exists(self, store):
        assert "scf.for" in store.control_flow_ops

    def test_scf_for_has_syntax(self, store):
        op = store.control_flow_ops["scf.for"]
        assert "scf.for" in op.syntax

    def test_scf_if_exists(self, store):
        assert "scf.if" in store.control_flow_ops


class TestAuxiliaryOps:
    def test_make_tensor_view_exists(self, store):
        assert "make_tensor_view" in store.auxiliary_ops

    def test_alloc_tile_exists(self, store):
        # There may be two headings for alloc_tile (static + dynamic)
        assert "alloc_tile" in store.auxiliary_ops


class TestCommunicationInstructions:
    def test_comm_instructions_loaded(self, store):
        """At least some communication instructions should be loaded."""
        comm_names = ["TBROADCAST", "TREDUCE", "TPUT", "TGET"]
        found = [n for n in comm_names if n in store.instructions]
        assert len(found) >= 2, f"Expected >=2 comm instructions, found: {found}"
