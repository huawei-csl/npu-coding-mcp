# npu-coding-mcp

An [MCP](https://modelcontextprotocol.io/) server for **Ascend NPU kernel development**. It provides tools, resources, and prompts to help developers write, optimize, and debug custom operators and kernels using Ascend C (AscendCL), TBE (Tensor Boost Engine), and related toolchains.

## Features

### Tools

| Tool | Description |
|------|-------------|
| `generate_tiling_struct` | Generates a C++ tiling struct and Python registration boilerplate from a list of field definitions |
| `explain_ascendc_error` | Interprets common Ascend C / CANN compilation or runtime errors and suggests fixes |
| `scaffold_custom_op` | Scaffolds the file tree and boilerplate for a new custom Ascend operator |

### Resources

| URI | Description |
|-----|-------------|
| `ascend://docs/memory-hierarchy` | Reference docs for the Ascend NPU memory hierarchy (L0A/B/C, L1, UB, L2, GM) |
| `ascend://docs/tiling-guide` | Tiling strategy guide including double-buffer patterns and rules of thumb |
| `ascend://docs/ascendc-primer` | Primer on writing kernels with the Ascend C API, including a minimal kernel skeleton |

### Prompts

| Prompt | Description |
|--------|-------------|
| `kernel_review_prompt` | Structured review prompt for an Ascend C kernel snippet |
| `op_design_prompt` | Design-discussion prompt for a new Ascend custom operator |

## Installation

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/zouzias/npu-coding-mcp
cd npu-coding-mcp
uv sync
```

## Usage

### Run the MCP server

```bash
uv run npu-coding-mcp
```

### Configure with Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "npu-coding-mcp": {
      "command": "uv",
      "args": [
        "--directory", "/path/to/npu-coding-mcp",
        "run", "npu-coding-mcp"
      ]
    }
  }
}
```

### Configure with Claude Code

```bash
claude mcp add npu-coding-mcp -- uv --directory /path/to/npu-coding-mcp run npu-coding-mcp
```

## Development

```bash
# Install dev dependencies
uv sync --group dev

# Run tests
uv run pytest

# Lint
uv run ruff check src tests
```

## License

See [LICENSE](LICENSE).
