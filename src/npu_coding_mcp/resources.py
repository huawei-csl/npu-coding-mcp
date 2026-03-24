"""MCP resources for Ascend NPU kernel development."""

import subprocess
from pathlib import Path

from . import mcp


@mcp.resource("host://npu-smi/info")
def npu_smi_info() -> str:
    """Run `npu-smi info` and return its output."""
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
        return f"Error: {version_file} not found. Ensure the Ascend driver is installed."
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


@mcp.resource("ascend://docs/910b-architecture")
def ascend_910b_architecture() -> str:
    """Hardware architecture overview of the Ascend 910B NPU."""
    return """
# Ascend 910B NPU Architecture Overview

## Chip-Level Specs
- **AI Compute**: 256 TFLOPS (FP16), 512 TOPS (INT8)
- **HBM capacity**: 64 GB HBM2e per chip
- **HBM bandwidth**: ~1.6 TB/s
- **On-chip SRAM (L2)**: 32 MB shared across all cores
- **TDP**: ~400 W

## Die Composition
The 910B integrates multiple **AI Core clusters** (Da Vinci cores) plus scalar,
vector, and cube compute units inside each core.

### Per AI Core
| Sub-unit      | Function                                       |
|---------------|------------------------------------------------|
| Cube Unit     | Systolic-array matrix multiply (MMA)           |
| Vector Unit   | Element-wise ops, activations, reductions      |
| Scalar Unit   | Loop control, address calculation, branches    |
| MTE1 / MTE2   | Memory Transfer Engines — DMA between GM↔L1   |
| MTE3          | DMA between L1↔L0 and UB↔GM                  |

## Interconnect
- **HCCS (Huawei Collective Communication Subsystem)**: high-speed ring between
  chips in an Atlas 800T A2 training server (8 × 910B), ~400 GB/s bidirectional.
- **PCIe Gen4 x16**: host ↔ device control path.

## Multi-Card / Multi-Node
- 8 devices per server, up to 1024 devices per cluster.
- CollectiveComm library (HCCL) mirrors NCCL semantics.

## Key Differences vs. 910A
- Larger HBM (64 GB vs 32 GB)
- Improved FP16/BF16 MMA throughput
- Higher HCCS bandwidth
- Better support for FP32 accumulation in cube unit
"""


@mcp.resource("ascend://docs/daVinci-compute-units")
def da_vinci_compute_units() -> str:
    """Detailed description of Da Vinci core compute units and their instruction sets."""
    return """
# Da Vinci Core Compute Units

## 1. Cube Unit (Matrix Compute Engine)
Implements a 16×16 systolic array for matrix multiply-accumulate.

### Supported Operations
| API / Intrinsic       | Description                                   |
|-----------------------|-----------------------------------------------|
| `matmul`              | C = A × B, L0A × L0B → L0C                   |
| `mmad`                | Mixed-precision MMA (FP16 in, FP32 accum)     |
| `conv2d`              | Im2col + matmul fusion                        |

### Data Types
- Inputs: FP16, BF16, INT8, INT4 (910B)
- Accumulator: FP32, INT32

### Tiling Rule for MatMul
A tile of shape (M, K) × (K, N) must satisfy:
- M, N are multiples of 16
- K is a multiple of 16 (FP16) or 32 (INT8)
- Each tile fits in L0A (64 KB) and L0B (64 KB) simultaneously

## 2. Vector Unit
Operates on 256-byte vectors stored in UB.

### Instruction Categories
| Category          | Examples                                           |
|-------------------|----------------------------------------------------|
| Arithmetic        | `vadd`, `vsub`, `vmul`, `vdiv`                    |
| Activation        | `vrelu`, `vsigmoid`, `vtanh`, `vexp`, `vlog`      |
| Comparison        | `vcmpv_gt`, `vcmpv_eq`                             |
| Reduction         | `vcadd`, `vcmax`, `vcmin`                          |
| Data movement     | `vconv` (type cast), `vtranspose`                  |
| Special math      | `vsqrt`, `vrsqrt`, `vrec`                          |

### Vector Width
- 128 FP16 elements per cycle (256 bytes)
- 64 FP32 elements per cycle

## 3. Scalar Unit
General-purpose RISC-like unit for control flow:
- Integer and address arithmetic
- Branch, loop, call
- Loads/stores to UB scalars

## Execution Pipeline
Instructions from Cube, Vector, and Scalar units execute in parallel; explicit
`pipe_barrier` synchronisation (or the Ascend C `sync_all` abstraction) is required
when a consumer reads results produced by a different unit.
"""


@mcp.resource("ascend://docs/ascend-c-programming-model")
def ascend_c_programming_model() -> str:
    """Ascend C (AICORE kernel language) programming model and workflow."""
    return """
# Ascend C Programming Model

Ascend C is a C++-based kernel development language for Da Vinci cores.
It replaces TBE TIK (Python DSL) for custom operator development on Ascend 910 series.

## Kernel Entry Point
```cpp
extern "C" __global__ __aicore__ void my_kernel(GM_ADDR x, GM_ADDR y, GM_ADDR z) {
    // kernel body
}
```
- `__global__`: callable from host
- `__aicore__`: compiled for Da Vinci AI Core

## Execution Model
- A kernel is launched with a grid of **blocks** (one block per AI Core).
- Each block runs a single-threaded control flow on the Scalar unit, issuing
  async DMA and compute instructions to MTE / Cube / Vector units.
- `GetBlockIdx()` returns the current core index (0-based).

## Memory Allocation (stack-based, no heap)
```cpp
// Allocate tile buffers in UB
TBuf<TPosition::UB> ub_buf;
LocalTensor<half> x_ub = ub_buf.Get<half>();  // slice from UB

// Allocate L1 buffer
TBuf<TPosition::A1> l1_buf;
LocalTensor<half> x_l1 = l1_buf.Get<half>();
```

## Data Copy (DMA)
```cpp
// GM → UB (direct, for element-wise ops)
DataCopy(x_ub, x_gm, copy_params);

// GM → L1 → L0A (for cube ops)
DataCopy(x_l1, x_gm, copy_params);
DataCopy(x_l0a, x_l1, copy_params);
```

## Double Buffering Pattern
Use `SetFlag` / `WaitFlag` on `PIPE_MTE1` and `PIPE_MTE2` events to overlap
DMA with compute:
```cpp
// Ping-pong loop sketch
for (int i = 0; i < n_tiles; i++) {
    int pingpong = i % 2;
    WaitFlag<HardEvent::MTE2_V>(pingpong);   // wait previous DMA
    DataCopy(ub[pingpong], gm[i], params);
    SetFlag<HardEvent::MTE2_V>(pingpong);    // signal DMA done
    WaitFlag<HardEvent::V_MTE3>(pingpong);   // wait vector done
    // ... compute on ub[1 - pingpong]
    SetFlag<HardEvent::V_MTE3>(pingpong);
}
```

## Synchronisation Primitives
| Primitive                          | Purpose                                  |
|------------------------------------|------------------------------------------|
| `SetFlag<EVENT>(id)`               | Mark a pipeline event as done            |
| `WaitFlag<EVENT>(id)`              | Stall until event is signalled           |
| `PipeBarrier<PIPE_ALL>()`          | Full barrier across all sub-pipelines    |
| `SyncAll()`                        | Barrier across all AI Cores in a block   |

## Compilation & Packaging
1. Write kernel in `.cpp` with Ascend C headers.
2. Compile with `acl_kernel_compiler` or `acbuild` (part of CANN SDK).
3. Package into an `.so` via `atc` (Ascend Tensor Compiler).
4. Load and invoke via ACL (`aclrtLaunchKernel`) or PyTorch custom op bridge.
"""


@mcp.resource("ascend://docs/cann-api-reference")
def cann_api_reference() -> str:
    """Key CANN SDK APIs for host-side management, memory, and kernel launch."""
    return """
# CANN SDK — Key Host-Side APIs

CANN (Compute Architecture for Neural Networks) is Huawei's software stack for
Ascend NPUs. Version ≥ 7.0 is recommended for 910B.

## Initialisation
```cpp
aclInit(nullptr);                          // load ACL, optionally pass config JSON
aclrtSetDevice(device_id);                 // select NPU device
aclrtCreateContext(&ctx, device_id);       // create execution context
aclrtCreateStream(&stream);                // create async execution stream
```

## Memory Management
```cpp
// Device memory
aclrtMalloc(&d_ptr, size, ACL_MEM_MALLOC_NORMAL_ONLY);
aclrtFree(d_ptr);

// Host ↔ Device transfer
aclrtMemcpy(dst, dst_size, src, src_size, ACL_MEMCPY_HOST_TO_DEVICE);
aclrtMemcpy(dst, dst_size, src, src_size, ACL_MEMCPY_DEVICE_TO_HOST);

// Async variant (overlaps with compute on stream)
aclrtMemcpyAsync(dst, dst_size, src, src_size, kind, stream);
```

## Kernel Launch
```cpp
// Ascend C custom kernel
uint32_t block_dim = tiling.tile_num;
ACLRT_LAUNCH_KERNEL(my_kernel)(block_dim, stream, x_dev, y_dev, tiling_dev);

// Synchronise
aclrtSynchronizeStream(stream);
```

## Model Inference (ACL)
```cpp
aclmdlLoadFromFile("model.om", &model_id);
aclmdlCreateDataset(&input_dataset);
// ... fill dataset buffers ...
aclmdlExecute(model_id, input_dataset, output_dataset);
aclmdlUnload(model_id);
```

## Error Handling
```cpp
aclError ret = aclrtMalloc(...);
if (ret != ACL_SUCCESS) {
    // aclGetRecentErrMsg() returns a human-readable string
    printf("ACL error: %s\n", aclGetRecentErrMsg());
}
```

## Useful Queries
```cpp
aclrtGetMemInfo(ACL_HBM_MEM, &free_bytes, &total_bytes);  // HBM usage
uint32_t dev_count;
aclrtGetDeviceCount(&dev_count);
```

## Python / PyTorch Integration
- **torch_npu**: drop-in extension, moves tensors with `.npu()`, exposes
  `torch.npu.current_device()`, `torch.npu.synchronize()`, etc.
- Custom Ascend C ops registered via `torch_npu.utils.cpp_extension.NpuExtension`.
"""


@mcp.resource("ascend://docs/performance-tuning")
def performance_tuning_docs() -> str:
    """Performance tuning guidelines for Ascend 910B custom kernels."""
    return """
# Performance Tuning — Ascend 910B

## 1. Maximise Cube Unit Utilisation
- Tile M/N/K to multiples of **16** (FP16) or **32** (INT8) to avoid padding ops.
- Use **FP16 inputs with FP32 accumulation** (`mmad`) for accuracy without throughput loss.
- Fuse consecutive matmuls/convolutions to avoid round-trips to GM.

## 2. Hide Memory Latency with Double Buffering
- Always use **ping-pong buffers** in UB/L1 to overlap DMA (MTE2) with compute (Vector/Cube).
- Rule of thumb: if arithmetic intensity < 8 ops/byte, DMA is the bottleneck.
- Use `SetFlag` / `WaitFlag` with `PIPE_MTE1`, `PIPE_MTE2`, `PIPE_V`, `PIPE_M` events.

## 3. Increase AI Core Occupancy
- Set `block_dim` = number of available AI Cores on the device (typically 24 for 910B).
- Balance tile size: large tiles → better arithmetic intensity; too large → UB spill.

## 4. Alignment Rules
| Buffer | Required alignment |
|--------|--------------------|
| UB     | 32 bytes           |
| L1     | 512 bytes          |
| L0A/B  | 512 bytes          |
| GM     | 32 bytes (DMA)     |

Misaligned accesses silently pad or cause correctness issues — always verify.

## 5. Data Type Selection
| Task               | Recommended dtype | Notes                              |
|--------------------|-------------------|------------------------------------|
| Training forward   | BF16 / FP16       | 910B supports both natively        |
| Training backward  | FP32 accumulator  | Use `mmad` for grad stability      |
| Inference          | INT8 / FP16       | INT8 ~2× throughput vs FP16        |
| Attention softmax  | FP32 intermediate | Precision-critical reduction       |

## 6. Profiling Tools
- **msprof**: Ascend profiler, collects hardware PMU counters.
  ```bash
  msprof --application="python train.py" --output=./prof_output
  ```
- **MindStudio Profiling**: GUI-based timeline viewer for AI Core activity.
- **acl_prof API**: programmatic profiling regions inside C++ / Python.
- Key metrics to watch:
  - `cube_utilization` (target > 60%)
  - `vector_utilization`
  - `mte2_bw` vs theoretical HBM BW
  - `aicore_time` vs end-to-end time (identifies host-side overhead)

## 7. Common Pitfalls
- Forgetting `PipeBarrier` between producer/consumer units → silent data races.
- UB buffer over-allocation → kernel fail at runtime (no static check in CANN < 8.0).
- Not accounting for the last-tile edge case in tiling → out-of-bounds GM access.
- Launching with `block_dim=1` during debugging but forgetting to scale up → low util.
"""


@mcp.resource("ascend://docs/operator-development-workflow")
def operator_development_workflow() -> str:
    """End-to-end workflow for developing and deploying a custom Ascend C operator."""
    return """
# Custom Operator Development Workflow (Ascend C / CANN)

## 1. Environment Setup
```bash
# Activate CANN environment (adjust path to your installation)
source /usr/local/Ascend/ascend-toolkit/set_env.sh

# Verify device visibility
npu-smi info

# Check CANN version
cat /usr/local/Ascend/ascend-toolkit/latest/version.cfg
```

## 2. Directory Structure
```
my_op/
├── op_kernel/
│   └── my_op.cpp          # Ascend C kernel (.cpp)
├── op_host/
│   ├── my_op_tiling.h     # TilingData struct (shared host+device)
│   └── my_op.cpp          # TilingFunc + op registration
├── cmake/
│   └── config.cmake
└── CMakeLists.txt
```

## 3. Write the Kernel (op_kernel/my_op.cpp)
```cpp
#include "kernel_operator.h"

extern "C" __global__ __aicore__ void my_op(
        GM_ADDR x_gm, GM_ADDR y_gm, GM_ADDR tiling_gm) {
    GET_TILING_DATA(td, tiling_gm, MyOpTilingData);
    // ... tiled compute logic ...
}
```

## 4. Write TilingFunc (op_host/my_op.cpp)
Implement `MyOpTiling(gert::TilingContext*)` and register:
```cpp
IMPL_OP("MyOp").Tiling(MyOpTiling).TilingData<MyOpTilingData>();
```

## 5. Build
```bash
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release \
         -DASCEND_CANN_PACKAGE_PATH=/usr/local/Ascend/ascend-toolkit/latest
make -j$(nproc)
# Produces: libcust_opsproto_rt_opp.so
```

## 6. Install into OPP (Operator Package)
```bash
./custom_opp_<soc_version>.run
# Installs into $ASCEND_OPP_PATH/vendors/customize/
```

## 7. PyTorch Custom Op (torch_npu)
```python
import torch, torch_npu
from torch_npu.utils.cpp_extension import NpuExtension, BuildExtension
# or load via torch.ops after loading the shared library:
torch.ops.load_library("libcust_opsproto_rt_opp.so")
result = torch.ops.custom_domain.my_op(x, y)
```

## 8. Debugging Tips
- Set `ASCEND_GLOBAL_LOG_LEVEL=0` for verbose ACL logs.
- Use `aclprofiling` or `msprof` to capture timeline.
- Test with `block_dim=1` first to isolate correctness from parallelism bugs.
- Compile with `-DDEBUG_MODE` and insert `ASSERT` / `PRINT` intrinsics if available.
- For shape/dtype issues, `aclmdlGetDesc` dumps model I/O descriptors.

## 9. Useful References
- CANN operator development guide: https://www.hiascend.com/document/detail/en/CANNCommunityEdition/
- Ascend C API reference: search "Ascend C" on https://www.hiascend.com/document
- torch_npu GitHub: https://github.com/Ascend/pytorch
"""
