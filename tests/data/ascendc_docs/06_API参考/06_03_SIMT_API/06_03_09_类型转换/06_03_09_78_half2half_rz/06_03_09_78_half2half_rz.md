# __half2half_rz

> **Section**: 6.3.9.78  
> **PDF Pages**: 3450–3450  

---

<!-- page 3450 -->

```cpp
#include "simt_api/asc_fp16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__half2half_rn(__gm__ half* dst, __gm__ half* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __half2half_rn(x[idx]);}

## 6.3.9.78 __half2half_rz

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

将half类型数据遵循CAST_TRUNC模式取整。

函数原型

```cpp
inline float __half2half_rz(const half x)
```

参数说明

表6-1713参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_TRUNC模式取整后的half类型数据。
