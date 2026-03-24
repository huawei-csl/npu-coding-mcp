"""MCP server for Ascend NPU kernel development."""

from fastmcp import FastMCP

mcp = FastMCP(
    name="npu-coding-mcp",
    instructions=(
        "You are an expert assistant for Ascend NPU kernel development. "
        "You help developers write, optimize, and debug custom operators and kernels "
        "using PTO-ISA, and related toolchains. "
        "You provide guidance on memory hierarchy, tiling strategies, data flow, "
        "and performance tuning on Ascend AI processors."
    ),
)

import npu_coding_mcp.prompts  # noqa
import npu_coding_mcp.resources  # noqa
import npu_coding_mcp.tools  # noqa
