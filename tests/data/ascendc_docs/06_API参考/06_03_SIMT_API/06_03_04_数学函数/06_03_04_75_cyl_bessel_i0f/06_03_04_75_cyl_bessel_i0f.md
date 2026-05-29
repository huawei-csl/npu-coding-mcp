# cyl_bessel_i0f

> **Section**: 6.3.4.75  
> **PDF Pages**: 3208–3208  

---

<!-- page 3208 -->

```cpp
#include "simt_api/math_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void KernelLgamma(__gm__ float* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = lgammaf(x[idx]);}

## 6.3.4.75 cyl_bessel_i0f

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

获取输入数据x的0阶常规修正圆柱贝塞尔函数的值。

![p3208_img001.png](../../images/p3208_img001.png)

函数原型

```cpp
inline float cyl_bessel_i0f(float x)
```

参数说明

表6-1529参数说明

参数名输入/输出

描述

x输入源操作数。
