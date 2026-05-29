# remainderf

> **Section**: 6.3.4.96  
> **PDF Pages**: 3238–3238  

---

<!-- page 3238 -->

需要包含的头文件

使用该接口需要包含"simt_api/math_functions.h"头文件。

```cpp
#include "simt_api/math_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void KernelMod(__gm__ float* dst, __gm__ float* x, __gm__ float* y){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = fmodf(x[idx], y[idx]);}

## 6.3.4.96 remainderf

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

获取输入数据x除以y的余数。求余数时，商取最接近x除以y浮点数结果的整数，当x除以y的浮点数结果与左右最接近的整数距离相等时，商取偶数。

函数原型

```cpp
inline float remainderf(float x, float y)
```

参数说明

表6-1550参数说明

参数名输入/输出

描述

x输入源操作数。

y输入源操作数。
