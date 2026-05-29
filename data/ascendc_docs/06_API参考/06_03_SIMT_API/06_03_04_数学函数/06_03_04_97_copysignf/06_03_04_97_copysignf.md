# copysignf

> **Section**: 6.3.4.97  
> **PDF Pages**: 3239–3240  

---

<!-- page 3239 -->

返回值说明

输入数据x除以y的余数。

●y为0时，返回值为nan。

●x为inf或-inf时，返回值为nan。

●x为有限数，y为inf或-inf时，返回值为x。

●x，y任意一个为nan时，返回值为nan。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/math_functions.h"头文件。

```cpp
#include "simt_api/math_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void KernelRemainder(__gm__ float* dst, __gm__ float* x, __gm__ float* y){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = remainderf(x[idx], y[idx]);}

## 6.3.4.97 copysignf

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

获取由第一个输入x的数值部分和第二个输入y的符号部分拼接得到的浮点数。

<!-- page 3240 -->

![p3240_img001.png](../../images/p3240_img001.png)

函数原型

```cpp
inline float copysignf(float x, float y)
```

参数说明

表6-1551参数说明

参数名输入/输出

描述

x输入源操作数。

y输入源操作数。

返回值说明

●y>=0时，返回x的绝对值Abs(x)。

●y<0时，返回x绝对值的相反数，-Abs(x)。

●y=nan时，返回-Abs(x)。

●y=-inf时，返回-Abs(x)。

●y=inf时，返回Abs(x)。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/math_functions.h"头文件。

```cpp
#include "simt_api/math_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void KerneCopySign(__gm__ float* dst, __gm__ float* x, __gm__ float* y){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = copysignf(x[idx], y[idx]);}
