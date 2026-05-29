# __int_as_float

> **Section**: 6.3.9.246  
> **PDF Pages**: 3659–3659  

---

<!-- page 3659 -->

返回值说明

将half2的两个分量分别转换为float，并填充到float2的结果。

约束说明

SIMT编程场景当前不支持使用该接口。

调用示例

SIMD与SIMT混合编程场景：// 使用小向量可提升数据搬运效率__simt_vf__ __launch_bounds__(1024) inline void simt_half22float2(__gm__ half2* input, __gm__ float2* output, uint32_t input_total_length){    uint32_t idx = blockIdx.x * blockDim.x + threadIdx.x;    // 每个线程处理1个half2类型的数据，即2个half类型的数据，因此idx >= input_total_length / 2的线程不处理数据    if (idx >= input_total_length / 2) {        return;    }     output[idx] = __half22float2(input[idx]);}

```cpp
__global__ __vector__ void cast_kernel(__gm__ half* input, __gm__ float* output, uint32_t input_total_length){    asc_vf_call<simt_half22float2>(dim3(1024), (__gm__ half2*)input, (__gm__ float2*)output, input_total_length);}
```

## 6.3.9.246 __int_as_float

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

将整数中的位重新解释为浮点数，即将整数存储的位按照float的格式进行读取。

函数原型

```cpp
inline float __int_as_float(const int x)
```
