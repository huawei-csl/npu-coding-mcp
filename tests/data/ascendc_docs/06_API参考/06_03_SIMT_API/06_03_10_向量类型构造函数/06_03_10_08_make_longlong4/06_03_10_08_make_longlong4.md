# make_longlong4

> **Section**: 6.3.10.8  
> **PDF Pages**: 3675–3676  

---

<!-- page 3675 -->

参数说明

表6-1893参数说明

参数名输入/输出

描述

x输入源操作数。

y输入源操作数。

返回值说明

由两个long long int类型数字构成的新longlong2向量。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/vector_functions.h"头文件。

```cpp
#include "simt_api/vector_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__global__ __launch_bounds__(1024) inline void kernel_make_longlong2(__gm__ longlong2* dst, __gm__ long long int* x, __gm__ long long int* y){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = make_longlong2(x[idx], y[idx]);}

## 6.3.10.8 make_longlong4

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

<!-- page 3676 -->

功能说明

使用给定的四个long long int类型的数据创建一个longlong4类型的向量。

函数原型

```cpp
inline longlong4 make_longlong4(long long int x, long long int y, long long int z,                                                               long long int w)
```

参数说明

表6-1894参数说明

参数名输入/输出

描述

x输入源操作数。

y输入源操作数。

z输入源操作数。

w输入源操作数。

返回值说明

由四个long long int类型数字构成的新longlong4向量。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/vector_functions.h"头文件。

```cpp
#include "simt_api/vector_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel_make_longlong4(__gm__ longlong4* dst, __gm__ long long int* x, __gm__ long long int* y, __gm__ long long int* z, __gm__ long long int* w){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = make_longlong4(x[idx], y[idx], z[idx], w[idx]);}
