# npu-coding-mcp

An [MCP](https://modelcontextprotocol.io/) server for **Ascend NPU kernel development**. It provides tools, resources, and prompts to help developers write, optimize, and debug custom operators and kernels using Ascend CANN software stack, and related toolchains.

## Features

### Tools

| Tool | Parameters | Description |
|------|------------|-------------|
| `compile_pto_isa` | `kernel_source`, `npu_arch` (default: `dav-2201`), `define_membase` (default: `false`), `timeout` (default: `120`) | Compile a PTO-ISA kernel source string using the `bisheng` compiler and return the compilation result (exit code, stdout/stderr, duration, path to `.so`, exported functions) |
| `load_dylib` | `lib_path` | Load a compiled `.so` dynamic library and prepare it for kernel invocation via ctypes |

### Resources

| URI | Description |
|-----|-------------|
| `host://npu-smi/info` | Run `npu-smi info` on the MCP server host and return the output (includes driver version) |
| `host://npu/driver-version` | Read the Ascend NPU driver version from `/usr/local/Ascend/version.info` |
| `npu://device` | Ascend 910B chip identity: AI core count, clock, HBM type/capacity/bandwidth, TDP, PTO backend tag |
| `npu://memory-map` | Per-AI-Core on-chip buffer hierarchy (L0A/B/C, UB, L1, L2) with sizes, data paths, and Manual-mode notes |
| `npu://compute-units` | Cube / Vector / Scalar throughput, supported dtypes, MACs/cycle, and AIC↔AIV architecture rules |
| `npu://pipeline` | Canonical 5-stage Manual-mode pipeline (MTE2→MTE1→Cube→Vector→MTE3), double-buffer overlap rules, and bottleneck checklist |
| `npu://constraints` | Hard limits for PTO-ISA kernel authors: tile divisibility, buffer alignment, size caps, layout contracts, and ordering rules |

### Prompts

| Prompt | Parameters | Description |
|--------|------------|-------------|
| `kernel_review_prompt` | `kernel_code` | Structured expert review covering correctness, memory usage, performance, tiling logic, and improvement suggestions |
| `op_design_prompt` | `op_description` | Structured design-discussion prompt covering op category, data types, tiling strategy, parallelism, memory plan, and edge cases |

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
