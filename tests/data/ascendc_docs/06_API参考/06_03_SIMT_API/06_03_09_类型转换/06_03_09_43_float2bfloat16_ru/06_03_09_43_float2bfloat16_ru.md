# __float2bfloat16_ru

> **Section**: 6.3.9.43  
> **PDF Pages**: 3404–3404  

---

<!-- page 3404 -->

bfloat16x2_t* output, uint32_t input_total_length){    uint32_t idx = blockIdx.x * blockDim.x + threadIdx.x;    // 每个线程处理1个float2类型的数据，即2个float类型的数据，因此idx >= input_total_length / 2的线程不处理数据    if (idx >= input_total_length / 2) {        return;    }    output[idx] = __float22bfloat162_rd_sat(input[idx]);}

```cpp
__global__ __vector__ void cast_kernel(__gm__ float* input, __gm__ bfloat16_t* output, uint32_t input_total_length){    asc_vf_call<simt_float22bfloat162_rd_sat>(dim3(1024), (__gm__ float2*)input, (__gm__ bfloat16x2_t*)output, input_total_length);}
```

## 6.3.9.43 __float2bfloat16_ru

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

遵循CAST_CEIL模式，将浮点数转换为bfloat16精度，返回转换后的值。

函数原型

```cpp
inline bfloat16_t __float2bfloat16_ru(const float x)
```

参数说明

表6-1678参数说明

参数名输入/输出

描述

x输入源操作数。
