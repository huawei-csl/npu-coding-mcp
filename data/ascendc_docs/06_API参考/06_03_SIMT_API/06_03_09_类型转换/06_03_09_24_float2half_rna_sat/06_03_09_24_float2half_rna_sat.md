# __float2half_rna_sat

> **Section**: 6.3.9.24  
> **PDF Pages**: 3379–3379  

---

<!-- page 3379 -->

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2half_rna(__gm__ half* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2half_rna(x[idx]);}

## 6.3.9.24 __float2half_rna_sat

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

饱和模式下，将浮点数转换为半精度浮点数，并遵循CAST_ROUND模式，返回转换后的值。

函数原型

```cpp
inline half __float2half_rna_sat(const float x)
```

参数说明

表6-1659参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

饱和模式下将输入遵循CAST_ROUND模式转换成的半精度浮点数。
