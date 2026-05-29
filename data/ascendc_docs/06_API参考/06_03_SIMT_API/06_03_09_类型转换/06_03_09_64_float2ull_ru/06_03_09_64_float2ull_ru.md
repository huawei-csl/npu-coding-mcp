# __float2ull_ru

> **Section**: 6.3.9.64  
> **PDF Pages**: 3431–3431  

---

<!-- page 3431 -->

需要包含的头文件

使用该接口需要包含"simt_api/device_functions.h"头文件。

```cpp
#include "simt_api/device_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2ull_rd(__gm__ uint64_t* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2ull_rd(x[idx]);}

## 6.3.9.64 __float2ull_ru

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

遵循CAST_CEIL模式，将浮点数转换为64位无符号整数，返回转换后的值。

函数原型

```cpp
inline unsigned long long int __float2ull_ru(const float x)
```

参数说明

表6-1699参数说明

参数名输入/输出

描述

x输入源操作数。
