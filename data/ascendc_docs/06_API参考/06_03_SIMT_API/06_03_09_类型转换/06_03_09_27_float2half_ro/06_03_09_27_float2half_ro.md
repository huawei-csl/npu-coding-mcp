# __float2half_ro

> **Section**: 6.3.9.27  
> **PDF Pages**: 3383–3383  

---

<!-- page 3383 -->

uint32_t idx = blockIdx.x * blockDim.x + threadIdx.x;    // 每个线程处理1个float2类型的数据，即2个float类型的数据，因此idx >= input_total_length / 2的线程不处理数据    if (idx >= input_total_length / 2) {        return;    }    output[idx] = __float22half2_rna_sat(input[idx]);}

```cpp
__global__ __vector__ void cast_kernel(__gm__ float* input, __gm__ half* output, uint32_t input_total_length){    asc_vf_call<simt_float22half2_rna_sat>(dim3(1024), (__gm__ float2*)input, (__gm__ half2*)output, input_total_length);}
```

## 6.3.9.27 __float2half_ro

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

遵循CAST_ODD模式，将浮点数转换为半精度浮点数，返回转换后的值。

函数原型

```cpp
inline half __float2half_ro(const float x)
```

参数说明

表6-1662参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_ODD模式转换成的半精度浮点数。特别场景说明如下：
