# SIMD与SIMT混合算子实现

> **Section**: 3.5  
> **PDF Pages**: 554–560  

---

<!-- page 554 -->

```cpp
for (int32_t col = 0;
 col < in_width;
 col++) {    gather_output[output_idx] = input[input_idx];
    input_idx += 1;
    output_idx += 1;}
```

**----结束**

完整的核函数功能代码如下：constexpr uint32_t MAX_THREAD_COUNT = 2048;constexpr uint32_t MAX_BLOCK_COUNT = 65535;

```cpp
template <typename type_data, typename type_idx>__global__ __launch_bounds__(MAX_THREAD_COUNT) void gather_custom(    type_data* input,    type_idx* index,    type_data* gather_output,    uint32_t in_width,    uint32_t index_total_length){    // Calculate global thread ID    int32_t out_row = blockIdx.x * blockDim.x + threadIdx.x;    // Maps to the row index of output tensor    if (out_row >= index_total_length) {        return;    }    // Single thread processes entire row (all columns) - enables coalesced memory access    uint32_t in_row = index[out_row];
    int input_idx = in_row * in_width;
    int output_idx = out_row * in_width;
    for (int32_t col = 0;
 col < in_width;
 col++) {        gather_output[output_idx] = input[input_idx];
        input_idx += 1;
        output_idx += 1;    }}
```

运行验证

核函数即算子Kernel程序开发完成后，即可编写Host侧的核函数调用程序，实现从Host侧的APP程序调用算子，进行运行验证。

Host侧的关键代码如下：std::vector<float> gather(std::vector<float>& input, const uint32_t* in_shape, std::vector<uint32_t>& index){    ...    // 计算切分参数，设置动态UB内存    uint32_t block_num = 0;    uint32_t thread_num_per_block = 0;    block_split(index_total_length, block_num, thread_num_per_block))    ...    // 计算切分参数，设置动态UB内存    uint32_t dyn_ubuf_size = 0;  // No need to alloc dynamic memory.    // 用内存调用符<<<...>>>调用核函数完成指定的运算    gather_custom<<<block_num, thread_num_per_block, dyn_ubuf_size, stream>>>(              input_device, index_device, output_device, in_shape[1], index_total_length);    ...}

## 3.5 SIMD 与SIMT 混合算子实现

