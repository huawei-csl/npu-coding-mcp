# __float22hif82_rh_sat

> **Section**: 6.3.9.74  
> **PDF Pages**: 3444–3444  

---

<!-- page 3444 -->

调用示例

SIMD与SIMT混合编程场景：// 使用小向量可提升数据搬运效率__simt_vf__ __launch_bounds__(1024) inline void simt_float22hif82_rh(__gm__ float2* input, __gm__ hifloat8x2_t* output, uint32_t input_total_length){    uint32_t idx = blockIdx.x * blockDim.x + threadIdx.x;    // 每个线程处理1个float2类型的数据，即2个float类型的数据，因此idx >= input_total_length / 2的线程不处理数据    if (idx > input_total_length /2) {        return;    }    output[idx] = __float22hif82_rh(input[idx]);}__global__ __vector__ void cast_kernel(__gm__ float* input, __gm__ uint8_t* output, uint32_t input_total_length){    asc_vf_call<simt_float22hif82_rh>(dim3(1024), (__gm__ float2*)input, (__gm__ hifloat8x2_t*)output, input_total_length);}

## 6.3.9.74 __float22hif82_rh_sat

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

饱和模式下，将float2类型数据的两个分量遵循CAST_HYBRID模式转换为hifloat8_t精度，返回转换后的hifloat8x2_t类型数据。

函数原型

```cpp
inline hifloat8x2_t __float22hif82_rh_sat(const float2 x)
```
