# __float2bfloat16_rd_sat

> **Section**: 6.3.9.40  
> **PDF Pages**: 3400–3400  

---

<!-- page 3400 -->

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2bfloat16_rd(__gm__ bfloat16_t* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2bfloat16_rd(x[idx]);}

## 6.3.9.40 __float2bfloat16_rd_sat

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

饱和模式下，将浮点数转换为bfloat16精度，并遵循CAST_FLOOR模式，返回转换后的值。

函数原型

```cpp
inline bfloat16_t __float2bfloat16_rd_sat(const float x)
```

参数说明

表6-1675参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

饱和模式下将输入遵循CAST_FLOOR模式转换成的bfloat16类型数据。
