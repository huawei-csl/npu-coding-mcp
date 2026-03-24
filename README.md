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
| `host://npu-smi/info` | Run `npu-smi info` and return the live output |
| `host://npu/driver-version` | Read the Ascend NPU driver version from `/usr/local/Ascend/version.info` |
| `ascend://docs/memory-hierarchy` | Reference docs for the Ascend NPU memory hierarchy (L0A/B/C, L1, UB, L2, GM) including alignment constraints |
| `ascend://docs/910b-architecture` | Hardware architecture overview of the Ascend 910B (specs, AI Core sub-units, interconnect, multi-card) |
| `ascend://docs/daVinci-compute-units` | Detailed description of Da Vinci core compute units (Cube, Vector, Scalar) and their instruction sets |
| `ascend://docs/ascend-c-programming-model` | Ascend C kernel programming model: entry points, execution model, memory allocation, DMA, double buffering, and sync |
| `ascend://docs/cann-api-reference` | Key CANN SDK APIs for host-side management, memory, kernel launch, and Python/PyTorch integration |
| `ascend://docs/performance-tuning` | Performance tuning guidelines: Cube utilization, double buffering, occupancy, alignment, profiling tools, and pitfalls |
| `ascend://docs/operator-development-workflow` | End-to-end workflow for developing and deploying a custom Ascend C operator (env setup, build, OPP install, PyTorch integration) |

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
