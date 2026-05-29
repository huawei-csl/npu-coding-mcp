# __floats2half2_rn

> **Section**: 6.3.9.236  
> **PDF Pages**: 3646–3646  

---

<!-- page 3646 -->

```cpp
}    output[idx] = __bfloat1622float2(input[idx]);}__global__ __vector__ void cast_kernel(__gm__ bfloat16_t* input, __gm__ float* output, uint32_t input_total_length){    asc_vf_call<simt_bfloat1622float2>(dim3(1024), (__gm__ bfloat16x2_t*)input, (__gm__ float2*)output, input_total_length);}
```

## 6.3.9.236 __floats2half2_rn

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

将输入数据x、y遵循CAST_RINT模式分别转换为half类型，并填充到half2的前后两部分，返回转换后的half2类型数据。

函数原型

```cpp
inline half2 __floats2half2_rn(const float x, const float y)
```

参数说明

表6-1871参数说明

参数名输入/输出

描述

x输入源操作数。

y输入源操作数。

返回值说明

将输入float类型数据遵循CAST_RINT模式分别转换为half类型，并填充到half2的前后两部分的结果。
