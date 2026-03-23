"""MCP prompts for Ascend NPU kernel development."""

from . import mcp


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
