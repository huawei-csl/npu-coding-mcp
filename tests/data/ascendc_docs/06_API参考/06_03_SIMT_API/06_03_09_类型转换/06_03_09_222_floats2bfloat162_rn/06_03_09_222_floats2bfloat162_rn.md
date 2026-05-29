# __floats2bfloat162_rn

> **Section**: 6.3.9.222  
> **PDF Pages**: 3626–3627  

---

<!-- page 3626 -->

函数原型

```cpp
inline bfloat16x2_t __float2bfloat162_rn(const float x)
```

参数说明

表6-1856参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

将输入数据遵循CAST_RINT模式转换为bfloat16类型并填充到bfloat16x2的前后两部分，返回填充后的数据。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：// 使用小向量可提升数据搬运效率__simt_vf__ __launch_bounds__(1024) inline void simt_float2bfloat162_rn(__gm__ float* input, __gm__ bfloat16x2_t* output, uint32_t input_total_length){    uint32_t idx = blockIdx.x * blockDim.x + threadIdx.x;    if (idx > input_total_length) {        return;    }    output[idx] = __float2bfloat162_rn(input[idx]);}__global__ __vector__ void cast_kernel(__gm__ float* input,  __gm__ bfloat16_t* output, uint32_t input_total_length){    asc_vf_call<simt_float2bfloat162_rn>(dim3(1024), input, (__gm__ bfloat16x2_t*)output, input_total_length);}

## 6.3.9.222 __floats2bfloat162_rn

产品支持情况

产品是否支持

Atlas 350 加速卡√

<!-- page 3627 -->

产品是否支持

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

将输入数据x、y遵循CAST_RINT模式分别转换为bfloat16类型，并填充到bfloat16x2的前后两部分，返回转换后的bfloat16x2类型数据。

函数原型

```cpp
inline bfloat16x2_t __floats2bfloat162_rn(const float x, const float y)
```

参数说明

表6-1857参数说明

参数名输入/输出

描述

x输入源操作数。

y输入源操作数。

返回值说明

将输入float类型数据遵循CAST_RINT模式分别转换为bfloat16类型并填充到bfloat16x2的前后两部分，返回转换后的数据。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：
