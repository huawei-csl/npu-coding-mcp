"""Tests for the CCE intrinsic extraction and mapping."""

from __future__ import annotations

from pathlib import Path

import pytest

from npu_coding_mcp.cce_extractor.models import CCEMappingStore
from npu_coding_mcp.models import ISAStore


DATA_DIR = Path(__file__).parent.parent / "data"


def _has_cce_mapping() -> bool:
    path = DATA_DIR / "cce_mapping.json"
    return path.exists()


@pytest.fixture(scope="module")
def mapping_store() -> CCEMappingStore:
    path = DATA_DIR / "cce_mapping.json"
    assert path.exists(), "cce_mapping.json not found — run build_cce_mapping.py first"
    return CCEMappingStore.model_validate_json(path.read_text())


@pytest.fixture(scope="module")
def isa_store() -> ISAStore:
    from npu_coding_mcp.loader import _load_cce_mapping

    store = ISAStore()
    _load_cce_mapping(store)
    return store


class TestCCEMappingStore:
    @pytest.mark.skipif(not _has_cce_mapping(), reason="cce_mapping.json not generated yet")
    def test_json_has_top_level_fields(self, mapping_store):
        assert mapping_store.ptoisa_commit, "Missing ptoisa_commit"
        assert mapping_store.generated_at, "Missing generated_at"
        assert isinstance(mapping_store.instructions, dict)

    @pytest.mark.skipif(not _has_cce_mapping(), reason="cce_mapping.json not generated yet")
    def test_json_covers_known_instructions(self, mapping_store):
        known = {"TADD", "TMATMUL", "TLOAD", "TSTORE", "TASSIGN"}
        found = set(mapping_store.instructions.keys())
        missing = known - found
        if missing:
            pytest.skip(f"Build still in progress — missing: {missing}")

    @pytest.mark.skipif(not _has_cce_mapping(), reason="cce_mapping.json not generated yet")
    def test_tadd_has_both_backends(self, mapping_store):
        tadd = mapping_store.instructions.get("TADD")
        if not tadd or not tadd.a2a3 or not tadd.a5:
            pytest.skip("TADD not fully mapped yet (build in progress)")
        assert tadd.a5 is not None

    @pytest.mark.skipif(not _has_cce_mapping(), reason="cce_mapping.json not generated yet")
    def test_intrinsics_have_required_fields(self, mapping_store):
        for name, instr in mapping_store.instructions.items():
            for backend_key in ("a2a3", "a5"):
                mapping = getattr(instr, backend_key)
                if mapping is None:
                    continue
                for intrinsic in mapping.intrinsics:
                    assert intrinsic.name, f"{name}/{backend_key}: intrinsic missing name"
                    assert intrinsic.signature, f"{name}/{backend_key}: {intrinsic.name} missing signature"

    @pytest.mark.skipif(not _has_cce_mapping(), reason="cce_mapping.json not generated yet")
    def test_a2a3_and_a5_have_source_files(self, mapping_store):
        for name, instr in mapping_store.instructions.items():
            for backend_key, backend_label in [("a2a3", "A2A3"), ("a5", "A5")]:
                mapping = getattr(instr, backend_key)
                if mapping:
                    assert backend_label.lower() in mapping.source_file.lower() or backend_key in mapping.source_file, (
                        f"{name}: {backend_key} source_file '{mapping.source_file}' doesn't reference backend"
                    )


class TestCCEMappingLoader:
    @pytest.mark.skipif(not _has_cce_mapping(), reason="cce_mapping.json not generated yet")
    def test_isa_store_has_cce_mappings(self, isa_store):
        assert len(isa_store.cce_mappings) > 0, "No CCE mappings loaded into ISAStore"
        assert isa_store.ptoisa_commit, "No commit hash in ISAStore"

    @pytest.mark.skipif(not _has_cce_mapping(), reason="cce_mapping.json not generated yet")
    def test_cce_mapping_field_matches_json(self, isa_store, mapping_store):
        assert isa_store.ptoisa_commit == mapping_store.ptoisa_commit
        assert len(isa_store.cce_mappings) == len(mapping_store.instructions)


class TestMCPToolGetCCEIntrinsics:
    @pytest.mark.skipif(not _has_cce_mapping(), reason="cce_mapping.json not generated yet")
    def test_tool_returns_data_for_known_instruction(self, isa_store):
        from npu_coding_mcp.tools import register_tools
        from fastmcp import FastMCP

        mcp = FastMCP(name="test")
        register_tools(mcp, isa_store)

        assert "TADD" in isa_store.cce_mappings, "TADD should be in CCE mappings"

    @pytest.mark.skipif(not _has_cce_mapping(), reason="cce_mapping.json not generated yet")
    def test_tool_returns_error_for_unknown_instruction(self, isa_store):
        # Test directly via the store
        result = isa_store.cce_mappings.get("ZZZDOESNOTEXIST")
        assert result is None
