# __int2half_ru_sat

> **Section**: 6.3.9.179  
> **PDF Pages**: 3575–3575  

---

<!-- page 3575 -->

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__int2half_ru(__gm__ half* dst, __gm__ int32_t* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __int2half_ru(x[idx]);}

## 6.3.9.179 __int2half_ru_sat

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

饱和模式下，将int32类型数据转换为half类型数据，并遵循CAST_CEIL模式，返回转换后的值。

函数原型

```cpp
inline half __int2half_ru_sat(const int x)
```

参数说明

表6-1814参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

饱和模式下，遵循CAST_CEIL模式，将输入int32数据转换成的half数据。
