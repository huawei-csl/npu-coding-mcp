"""MCP prompts for Ascend NPU kernel development."""

from . import mcp

# ---------------------------------------------------------------------------
# Resources
# ---------------------------------------------------------------------------


@mcp.resource("ascend://docs/memory-hierarchy")
def memory_hierarchy_docs() -> str:
    """Reference documentation for the Ascend NPU memory hierarchy."""
    return """
# Ascend NPU Memory Hierarchy

## Memory Levels (from fastest to slowest)

| Level | Name       | Scope        | Typical Size | Notes                              |
|-------|------------|--------------|--------------|------------------------------------|
| L0A   | Local Buf A| Single core  | 64 KB        | Input buffer for cube units        |
| L0B   | Local Buf B| Single core  | 64 KB        | Input buffer for cube units        |
| L0C   | Local Buf C| Single core  | 256 KB       | Accumulator output of cube units   |
| L1    | L1 Buffer  | Single core  | 1 MB         | On-chip SRAM, feeds L0             |
| UB    | Unified Buf| Single core  | 256 KB       | Vector unit working buffer         |
| L2    | L2 Cache   | All cores    | 32 MB        | Shared on-chip cache               |
| GM    | Global Mem | Host + cores | GBs          | HBM / DDR, off-chip                |

## Data Flow Pattern (typical MatMul)
GM → L1 → L0A/L0B → Cube Unit → L0C → UB → GM

## Key Constraints
- L0C output must be cast/moved to UB before vector ops.
- DMA transfers between GM and L1 should be double-buffered to hide latency.
- UB alignment: tensors must be 32-byte aligned.
"""
