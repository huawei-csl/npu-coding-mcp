# __float2bfloat16_rn

> **Section**: 6.3.9.32  
> **PDF Pages**: 3389–3390  

---

<!-- page 3389 -->

参数说明

表6-1666参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_RINT模式转换成的bfloat16类型数据。特别场景说明如下：

●当x为nan时，返回值为nan。

●当x为inf时，返回值为inf。

●当x为-inf时，返回值为-inf。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2bfloat16(__gm__ bfloat16_t* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2bfloat16(x[idx]);}

## 6.3.9.32 __float2bfloat16_rn

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

<!-- page 3390 -->

产品是否支持

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

遵循CAST_RINT模式，将浮点数转换为bfloat16精度，返回转换后的值。

函数原型

```cpp
inline bfloat16_t __float2bfloat16_rn(const float x)
```

参数说明

表6-1667参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_RINT模式转换成的bfloat16类型数据。特别场景说明如下：

●当x为nan时，返回值为nan。

●当x为inf时，返回值为inf。

●当x为-inf时，返回值为-inf。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2bfloat16_rn(__gm__ bfloat16_t* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2bfloat16_rn(x[idx]);}
