"""Ascend NPU kernel development MCP server."""

from fastmcp import FastMCP

mcp = FastMCP(
    name="npu-coding-mcp",
    instructions=(
        "You are an expert assistant for Ascend NPU kernel development. "
        "You help developers write, optimize, and debug custom operators and kernels "
        "using Ascend C (AscendCL), TBE (Tensor Boost Engine), and related toolchains. "
        "You provide guidance on memory hierarchy, tiling strategies, data flow, "
        "and performance tuning on Ascend AI processors."
    ),
)


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


@mcp.resource("ascend://docs/tiling-guide")
def tiling_guide_docs() -> str:
    """Tiling strategy guide for Ascend kernel development."""
    return """
# Ascend Kernel Tiling Guide

## What is Tiling?
Tiling splits large tensors into smaller blocks that fit in on-chip buffers (L1, UB).
The `GetTilingData` function computes tile shapes at compile-time/runtime.

## Typical Tiling Parameters
- `blockDim`   : number of AI Core blocks used
- `tilingKey`  : selects the tiling branch inside the kernel
- `tileLength` : number of elements per tile along the main dimension
- `totalLength`: total number of elements

## Double-Buffer Tiling Pattern
```
for (int i = 0; i < totalTiles; ++i) {
    // ping-pong between buffer 0 and buffer 1
    int bufIdx = i % 2;
    DataCopy(l1Buf[bufIdx], gmIn[i * tileLength], tileLength);
    // compute on l1Buf[1 - bufIdx] while filling l1Buf[bufIdx]
    ...
}
```

## Rules of Thumb
1. Keep UB utilisation ≤ 80 % to leave room for temporaries.
2. Choose `tileLength` as a multiple of 256 bytes (32 × fp16 elements).
3. Prefer square tiles for MatMul to maximise cube utilisation.
4. Use `SetAtomicAdd` / `SetAtomicNone` when multiple cores write the same GM region.
"""


@mcp.resource("ascend://docs/ascendc-primer")
def ascendc_primer_docs() -> str:
    """Primer on writing kernels with the Ascend C API."""
    return """
# Ascend C Kernel Primer

## Minimal Kernel Skeleton
```cpp
#include "kernel_operator.h"

extern "C" __global__ __aicore__ void my_kernel(
    GM_ADDR x, GM_ADDR y, GM_ADDR z,
    GM_ADDR tiling_gm)
{
    GET_TILING_DATA(tiling, tiling_gm);  // deserialise tiling struct

    // Declare on-chip buffers
    TPipe pipe;
    TQue<QuePosition::VECIN, 2> inQueue;
    TQue<QuePosition::VECOUT, 1> outQueue;

    GlobalTensor<half> xGm, yGm, zGm;
    xGm.SetGlobalBuffer((__gm__ half*)x);
    yGm.SetGlobalBuffer((__gm__ half*)y);
    zGm.SetGlobalBuffer((__gm__ half*)z);

    pipe.InitBuffer(inQueue, 2, tiling.tileLength * sizeof(half));
    pipe.InitBuffer(outQueue, 1, tiling.tileLength * sizeof(half));

    // Compute loop
    for (uint32_t i = 0; i < tiling.loopCount; ++i) {
        LocalTensor<half> xLocal = inQueue.AllocTensor<half>();
        DataCopy(xLocal, xGm[i * tiling.tileLength], tiling.tileLength);
        inQueue.EnQue(xLocal);

        LocalTensor<half> xComp = inQueue.DeQue<half>();
        LocalTensor<half> zLocal = outQueue.AllocTensor<half>();
        Add(zLocal, xComp, yGm[0], tiling.tileLength);  // example: z = x + y[0]
        outQueue.EnQue(zLocal);
        inQueue.FreeTensor(xComp);

        LocalTensor<half> zComp = outQueue.DeQue<half>();
        DataCopy(zGm[i * tiling.tileLength], zComp, tiling.tileLength);
        outQueue.FreeTensor(zComp);
    }
}
```

## Key APIs
| API            | Purpose                                      |
|----------------|----------------------------------------------|
| `DataCopy`     | DMA between GM ↔ L1/UB                       |
| `Add/Sub/Mul`  | Element-wise vector arithmetic               |
| `Matmul`       | Cube-unit matrix multiplication              |
| `Cast`         | Type conversion (fp32↔fp16, etc.)            |
| `Reduce*`      | Reduction along an axis (sum, max, …)        |
| `SetMaskCount` | Set the active-element mask for vector ops   |
"""


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def generate_tiling_struct(
    fields: list[dict],
    struct_name: str = "TilingData",
) -> str:
    """Generate a C++ tiling struct and its Python registration boilerplate.

    Args:
        fields: List of {"name": str, "type": str} dicts describing each field.
                Supported types: uint32_t, int32_t, uint64_t, int64_t, float.
        struct_name: Name for the generated tiling struct (default: TilingData).

    Returns:
        A string containing the C++ struct definition and the Python tiling
        registration snippet.
    """
    supported_types = {"uint32_t", "int32_t", "uint64_t", "int64_t", "float"}
    for f in fields:
        if f["type"] not in supported_types:
            raise ValueError(
                f"Unsupported type '{f['type']}' for field '{f['name']}'. "
                f"Supported: {supported_types}"
            )

    cpp_fields = "\n".join(f"    {f['type']} {f['name']};" for f in fields)
    cpp_struct = f"""\
// {struct_name}.h  – auto-generated tiling struct
#pragma once
#include <cstdint>

BEGIN_TILING_DATA_DEF({struct_name})
{cpp_fields}
END_TILING_DATA_DEF({struct_name})

REGISTER_TILING_DATA_CLASS({struct_name}, {struct_name})
"""

    py_setter_lines = "\n".join(
        f'    tiling_data.{f["name"]} = {f["name"]}_value  # TODO: compute value'
        for f in fields
    )
    py_snippet = f"""\
# tiling.py  – Python tiling function snippet
from ascend_tiling import TilingContext  # adjust import to your SDK path

def {struct_name.lower()}_tiling(context: TilingContext) -> None:
    tiling_data = context.get_tiling_data()
{py_setter_lines}
    context.set_tiling_data(tiling_data)
    block_dim = 1  # TODO: set real block_dim
    context.set_block_dim(block_dim)
"""

    return f"{cpp_struct}\n{py_snippet}"


@mcp.tool()
def explain_ascendc_error(error_message: str) -> str:
    """Interpret a common Ascend C / CANN compilation or runtime error.

    Args:
        error_message: The raw error string from the compiler or runtime log.

    Returns:
        A human-readable explanation and suggested fix.
    """
    checks = [
        (
            "alignment",
            "Tensor alignment error. Ensure all on-chip tensor addresses and sizes are "
            "multiples of 32 bytes. Check pipe.InitBuffer() sizes and DataCopy lengths.",
        ),
        (
            "out of ub",
            "Unified Buffer (UB) overflow. Reduce tile size or the number of "
            "simultaneously allocated UB tensors.",
        ),
        (
            "tiling key",
            "Tiling key mismatch. The tilingKey set in the Python tiling function must "
            "match a TILING_KEY_DEF branch inside the kernel.",
        ),
        (
            "dma",
            "DMA transfer error. Verify that source/destination addresses are "
            "correctly offset, sizes are non-zero, and the memory space (GM/L1/UB) is correct.",
        ),
        (
            "pipe overflow",
            "TPipe queue overflow. Increase the depth parameter in InitBuffer() or "
            "ensure EnQue/DeQue calls are balanced.",
        ),
        (
            "undefined symbol",
            "Linker error: undefined symbol. Make sure the kernel is compiled with the "
            "correct CANN toolkit version and that all required op libraries are linked.",
        ),
    ]

    lower_msg = error_message.lower()
    for keyword, explanation in checks:
        if keyword in lower_msg:
            return f"**Detected issue: {keyword}**\n\n{explanation}"

    return (
        "No automatic match found for this error.\n\n"
        "General debugging steps:\n"
        "1. Check CANN toolkit version compatibility.\n"
        "2. Validate tiling struct field types match between C++ and Python.\n"
        "3. Run `msopst` (op simulation tool) to reproduce offline.\n"
        "4. Add `AscendC::printf` calls to narrow down the failing tile.\n\n"
        f"Raw error:\n```\n{error_message}\n```"
    )


@mcp.tool()
def scaffold_custom_op(
    op_name: str,
    input_dtypes: list[str],
    output_dtypes: list[str],
    op_type: str = "Elewise",
) -> str:
    """Scaffold the file tree and boilerplate for a new custom Ascend op.

    Args:
        op_name: CamelCase name for the operator (e.g. MyAddOp).
        input_dtypes: List of input tensor dtypes (e.g. ["float16", "float16"]).
        output_dtypes: List of output tensor dtypes (e.g. ["float16"]).
        op_type: Operator category hint — "Elewise", "Reduce", or "Matmul".

    Returns:
        A formatted scaffold showing file paths and key code snippets to create.
    """
    valid_op_types = {"Elewise", "Reduce", "Matmul"}
    if op_type not in valid_op_types:
        raise ValueError(f"op_type must be one of {valid_op_types}, got '{op_type}'")

    snake = op_name.lower()

    dtype_map = {"float16": "half", "float32": "float", "int32": "int32_t", "int8": "int8_t"}
    cpp_in_types = [dtype_map.get(d, d) for d in input_dtypes]
    cpp_out_types = [dtype_map.get(d, d) for d in output_dtypes]

    in_params = ", ".join(f"GM_ADDR x{i}" for i in range(len(input_dtypes)))
    out_params = ", ".join(f"GM_ADDR y{i}" for i in range(len(output_dtypes)))

    in_gm_decls = "\n    ".join(
        f"GlobalTensor<{t}> x{i}Gm;" for i, t in enumerate(cpp_in_types)
    )
    out_gm_decls = "\n    ".join(
        f"GlobalTensor<{t}> y{i}Gm;" for i, t in enumerate(cpp_out_types)
    )
    in_gm_set = "\n    ".join(
        f"x{i}Gm.SetGlobalBuffer((__gm__ {t}*)x{i});"
        for i, t in enumerate(cpp_in_types)
    )
    out_gm_set = "\n    ".join(
        f"y{i}Gm.SetGlobalBuffer((__gm__ {t}*)y{i});"
        for i, t in enumerate(cpp_out_types)
    )

    op_host_inputs = "".join(
        f".INPUT(x{i}, TensorType({{DT_{d.upper()}}}))\\n" for i, d in enumerate(input_dtypes)
    )
    op_host_outputs = "".join(
        f".OUTPUT(y{i}, TensorType({{DT_{d.upper()}}}))\\n" for i, d in enumerate(output_dtypes)
    )

    return f"""\
# Scaffold for custom op: {op_name}  (type: {op_type})
# ─────────────────────────────────────────────────────────────────────────────
# Suggested file layout:
#
#   {snake}/
#   ├── CMakeLists.txt
#   ├── op_kernel/
#   │   └── {snake}.cpp          ← kernel implementation
#   ├── op_host/
#   │   ├── {snake}.cpp          ← host-side op registration
#   │   └── {snake}.h
#   └── tiling/
#       └── {snake}_tiling.py    ← Python tiling function
# ─────────────────────────────────────────────────────────────────────────────

# === op_kernel/{snake}.cpp ===
/*
 * Ascend C kernel for {op_name}.
 * Inputs : {input_dtypes}
 * Outputs: {output_dtypes}
 */
#include "kernel_operator.h"
using namespace AscendC;

extern "C" __global__ __aicore__ void {snake}(
    {in_params}, {out_params},
    GM_ADDR tiling_gm)
{{
    GET_TILING_DATA(tiling, tiling_gm);

    {in_gm_decls}
    {out_gm_decls}
    {in_gm_set}
    {out_gm_set}

    // TODO: implement tiling loop and compute logic here
}}

# === tiling/{snake}_tiling.py ===
from ascend_tiling import TilingContext

def {snake}_tiling(context: TilingContext) -> None:
    tiling_data = context.get_tiling_data()
    # TODO: populate tiling fields
    context.set_tiling_data(tiling_data)
    context.set_block_dim(1)

# === op_host/{snake}.h ===
#pragma once
#include "op_def.h"

namespace ops {{
    REG_OP({op_name})
        {op_host_inputs}{op_host_outputs}.OP_END_FACTORY_REG({op_name})
}}  // namespace ops
"""


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------


@mcp.prompt()
def kernel_review_prompt(kernel_code: str) -> str:
    """Return a structured review prompt for an Ascend C kernel snippet."""
    return f"""\
You are an expert Ascend NPU kernel engineer. Review the following Ascend C kernel code and provide:

1. **Correctness** – Are there any bugs (wrong offsets, missing FreeTensor, unbalanced queues)?
2. **Memory usage** – Is UB utilisation within safe limits? Are tensors aligned to 32 bytes?
3. **Performance** – Is double-buffering used? Are cube/vector units well utilised?
4. **Tiling** – Is the tiling logic sound? Could a different tile shape improve throughput?
5. **Suggestions** – Concrete code changes to improve the kernel.

Kernel code:
```cpp
{kernel_code}
```
"""


@mcp.prompt()
def op_design_prompt(op_description: str) -> str:
    """Return a design-discussion prompt for a new Ascend custom operator."""
    return f"""\
You are an Ascend NPU architect. A developer wants to implement the following operator:

{op_description}

Help them design the operator by addressing:

1. **Op category** – Is this Elewise, Reduce, Matmul, or a custom pipeline?
2. **Data types** – Which dtypes should be supported? Any implicit casting needed?
3. **Tiling strategy** – How should the input be tiled to fit L1 and UB?
4. **Parallelism** – How many AI Cores should be used? How is work divided?
5. **Memory plan** – Sketch the data-flow: GM → L1 → L0/UB → GM.
6. **Edge cases** – What corner cases (non-aligned sizes, empty tensors) need handling?
"""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
