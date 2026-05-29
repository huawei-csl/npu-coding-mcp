# __float2float_ru

> **Section**: 6.3.9.5  
> **PDF Pages**: 3354–3354  

---

<!-- page 3354 -->

需要包含的头文件

使用该接口需要包含"simt_api/device_functions.h"头文件。

```cpp
#include "simt_api/device_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2float_rd(__gm__ float* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2float_rd(x[idx]);}

## 6.3.9.5 __float2float_ru

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

将浮点数四舍五入取整，并遵循CAST_CEIL模式。

函数原型

```cpp
inline float __float2float_ru(const float x)
```

参数说明

表6-1640参数说明

参数名输入/输出

描述

x输入源操作数。
