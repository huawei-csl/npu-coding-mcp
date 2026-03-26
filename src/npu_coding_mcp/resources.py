"""PTO-ISA context
---------------
PTO is a virtual ISA from Huawei CANN that sits above hardware
assembly (CCE) and provides ~90 tile-level operations (GEMM, vector math, data-move,
collective-comms).  Kernels are written in two modes:

  Auto   – CPU-sim only; no buffer allocation or pipeline management required.
  Manual – real NPU; programmer allocates tile buffers, owns the pipeline.

The resources below give an agent exactly the hardware facts it needs to write
correct, performant Manual-mode PTO kernels targeting the 910B (A2 or A3 backend).

Resources
---------
  host://npu-smi/info        executes 'npu-smi info' on MCP server host
  host://npu/driver-version  returns Ascend driver version
  npu://device               chip identity, core count, clock, HBM specs
  npu://memory-map           on-chip buffer hierarchy with byte capacities
  npu://compute-units        Cube / Vector / Scalar throughput and data types
  npu://pipeline             canonical 5-stage pipeline: MTE2→MTE1→CUBE→VEC→MTE3
  npu://constraints          hard limits an agent must never violate
"""

from __future__ import annotations
import subprocess
from pathlib import Path


from . import mcp

@mcp.resource("host://npu-smi/info")
def npu_smi_info() -> str:
    """Run `npu-smi info` on host where MCP server runs.
    
    Return string contains the Ascend driver version"""
    try:
        result = subprocess.run(
            ["npu-smi", "info"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        output = result.stdout
        if result.stderr:
            output += f"\nstderr:\n{result.stderr}"
        return output
    except FileNotFoundError:
        return "Error: npu-smi not found. Check if Ascend toolkit is installed."
    except subprocess.TimeoutExpired:
        return "Error: npu-smi info timed out after 30 seconds."


@mcp.resource("host://npu/driver-version")
def npu_driver_version() -> str:
    """Read the Ascend NPU driver version from /usr/local/Ascend/version.info."""
    version_file = Path("/usr/local/Ascend/version.info")
    try:
        return version_file.read_text()
    except FileNotFoundError:
        return (
            f"Error: {version_file} not found. Ensure the Ascend driver is installed."
        )
    except PermissionError:
        return f"Error: permission denied reading {version_file}."


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
- L1/L0A/L0B memory alignment: tiles must be 512-bytes aligned.
"""

 
@mcp.resource("npu://device")
def device() -> str:
    return """\
# npu://device — Ascend 910B identity
 
chip          : HiSilicon Ascend 910B  (PTO backend tag: a3, covers A2/A3 family)
process       : SMIC N+1  (7 nm-class DUV)
ai_cores      : 20–24 exposed to software  (die estimate ~25 physical)
               910B2 → 24 AIC  |  910B3 → 20 AIC
clock         : 2.0 GHz
hbm_type      : HBM2e (B1/B2) · HBM3e (B3)
hbm_capacity  : 64 GiB
hbm_bandwidth : 900 GB/s (B1/B2)  ·  1 200 GB/s (B3)
tdp           : 400 W
 
PTO target string  : a3
CANN min version   : 8.x  (HBM3e features require 8.5.0+)
"""
 
 
 
@mcp.resource("npu://memory-map")
def memory_map() -> str:
    return """\
# npu://memory-map — per-AI-Core on-chip buffer hierarchy
 
Every buffer is private to one AI Core; no cross-core sharing at this level.
PTO Manual mode requires the agent to allocate tile addresses inside these buffers.
 
Buffer  │ Alias │ Typical size │ Fed by  │ Consumed by          │ Notes
────────┼───────┼──────────────┼─────────┼──────────────────────┼──────────────
L0A     │  —    │  512 KiB     │ MTE1    │ Cube Engine (A input) │ NZ layout only
L0B     │  —    │  512 KiB     │ MTE1    │ Cube Engine (B input) │ NZ layout only
L0C     │  —    │  256 KiB     │ Cube    │ MTE3 / Vector (UB)   │ accumulator
UB      │ UnifiedBuffer │ 256 KiB │ MTE2/MTE3 │ Vector units   │ double-buffer here
L1      │  —    │  ~1 MiB      │ MTE2    │ MTE1 → L0A/L0B       │ tile reuse cache
L2      │  —    │ shared/die   │ HBM/MTE2│ all cores via NoC     │ not per-core
 
Data path (Manual mode):
  HBM ──MTE2──▶ L1 ──MTE1──▶ L0A/L0B ──Cube──▶ L0C ──MTE3──▶ UB ──Vector──▶ UB ──MTE3──▶ HBM
  HBM ──MTE2──▶ UB ──Vector──▶ UB ──MTE3──▶ HBM          (vector-only path)
"""
 
  
@mcp.resource("npu://compute-units")
def compute_units() -> str:
    return """\
# npu://compute-units — compute throughput per AI Core
 
## Cube Engine  (AIC × 1)
  shape/cycle  : 16 × 16 × 16  (M-K-N systolic MMA)
  dtypes       : FP16 → FP32 accum  |  BF16 → FP32 accum  |  INT8 → INT32 accum
  FP16 MACs/cy : 4 096
  INT8 MACs/cy : 8 192
  peak/core    : ~18.75 TFLOPS FP16
  native layout: NZ (fractal); ND input is auto-converted by MTE1 if declared
 
## Vector Unit  (AIV × 2 per core)
  model        : SIMD, 256-bit wide (16 × FP16 per instruction)
  ops          : add, sub, mul, div, min, max, abs, exp, log, sqrt, rsqrt,
                 sigmoid, tanh, cast, reduce-sum, reduce-max, broadcast
  dtypes       : FP16, BF16, FP32, INT8, INT32  (cast between all)
  operand src  : Unified Buffer (UB)
  rule         : 2 AIV run concurrently with 1 AIC ("split" architecture)
               ⚠ AIC↔AIV data exchange must go via HBM or L2 — no direct path
 
## Scalar (×1 per AIC, ×1 per AIV)
  purpose      : control flow, address arithmetic, loop counters
  do not use   : for bulk tensor math — overhead is O(N) not O(N/SIMD_width)
"""
 
 
 
@mcp.resource("npu://pipeline")
def pipeline() -> str:
    return """\
# npu://pipeline — canonical Manual-mode pipeline for PTO kernels
 
Stage      │ HW unit │ Action
───────────┼─────────┼──────────────────────────────────────────────────────
COPY_IN    │ MTE2    │ HBM/L2 → L1 or UB  (prefetch next macro-tile)
LOAD       │ MTE1    │ L1 → L0A + L0B      (feed Cube for current tile)
COMPUTE_M  │ Cube    │ MMA 16×16×16 → L0C  (matrix path)
COMPUTE_V  │ Vector  │ UB ops (activation, norm, cast)  (vector path)
COPY_OUT   │ MTE3    │ L0C or UB → HBM/L2  (writeback result)
 
Overlap rule (double-buffer)
  COPY_IN[tile N+1]  runs concurrently with COMPUTE_M[tile N]
  COMPUTE_V[tile N]  runs concurrently with COMPUTE_M[tile N+1]
  COPY_OUT[tile N]   runs concurrently with COPY_IN[tile N+2]
 
PTO pipeline mapping
  PTO Auto mode  : compiler inserts all MTE and sync automatically.
  PTO Manual mode: agent must call pto::copy_in / pto::matmul / pto::copy_out
                   with explicit buffer addresses and pipe_barrier() fences.
 
pipe_barrier tokens
  PIPE_MTE2  PIPE_MTE1  PIPE_M (Cube)  PIPE_V (Vector)  PIPE_MTE3
  Fence between producer and consumer; do not insert more than necessary.
 
Bottleneck checklist
  CUBE bound  → increase tile M/N, fuse epilogue into kernel
  MTE2 bound  → add prefetch depth (L1 double-buffer), widen HBM access
  Vector bound→ fuse activation with drain, or use INT8 path
  Sync bound  → reduce pipe_barrier granularity
"""
 
  
@mcp.resource("npu://constraints")
def constraints() -> str:
    return """\
# npu://constraints — hard limits for PTO-ISA kernel authors
 
1. Tile shape divisibility
   Cube tile dimensions M, K, N must each be a multiple of 16.
   Vector tile length must be a multiple of 32 bytes (= 16 × FP16).
 
2. Buffer alignment
   All L0A, L0B, L0C, UB base addresses must be 32-byte aligned.
   L1 base addresses must be 64-byte aligned.
 
3. Buffer size limits (per core — do not exceed)
   L0A ≤ 512 KiB  ·  L0B ≤ 512 KiB  ·  L0C ≤ 256 KiB  ·  UB ≤ 256 KiB
 
4. Layout contract
   Cube Engine only accepts L0A/L0B in NZ (fractal) layout.
   MTE1 performs ND→NZ conversion if src is declared as ND — add conversion cost.
 
5. No direct AIC↔AIV data path
   Data produced by Cube (L0C) and consumed by Vector (UB) must be staged
   through MTE3 writeback.  Plan this in tile scheduling.
 
6. Cross-core communication
   No shared L0/UB across cores.  Use HBM tensors + HCCL (AllReduce etc.)
   for multi-core reduction.  On 910B intra-server HCCS bandwidth = 3 × 30 GB/s.
 
7. Instruction ordering
   All MTE and compute ops are asynchronous.  Missing pipe_barrier between
   a producer and its consumer causes silent data corruption — not a crash.
 
8. PTO backend tag for 910B : a3
   Use  -v a3  when invoking run_st.py or the PTO cmake target.
   The a3 backend covers both A2 and A3 silicon; 910B is A3 family.
 
9. CPU simulation (Auto mode) vs real NPU (Manual mode)
   Auto mode ignores buffer addresses; always validate algorithm in Auto mode
   before porting to Manual mode on real hardware.
"""