# __float22bfloat162_ru_sat

> **Section**: 6.3.9.46  
> **PDF Pages**: 3408–3408  

---

<!-- page 3408 -->

```cpp
output[idx] = __float22bfloat162_ru(input[idx]);}
__global__ __vector__ void cast_kernel(__gm__ float* input, __gm__ bfloat16_t* output, uint32_t input_total_length){    asc_vf_call<simt_float22bfloat162_ru>(dim3(1024), (__gm__ float2*)input, (__gm__ bfloat16x2_t*)output, input_total_length);}
```

## 6.3.9.46 __float22bfloat162_ru_sat

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

饱和模式下，将float2类型数据的两个分量遵循CAST_CEIL模式转换为bfloat16精度，返回转换后的bfloat16x2_t类型数据。

函数原型

```cpp
inline bfloat16x2_t __float22bfloat162_ru_sat(const float2 x)
```

参数说明

表6-1681参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

饱和模式下将输入的两个分量遵循CAST_CEIL模式转换成的bfloat16x2_t类型数据。
