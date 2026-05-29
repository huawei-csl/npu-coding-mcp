# __float22half2_rna_sat

> **Section**: 6.3.9.26  
> **PDF Pages**: 3381–3382  

---

<!-- page 3381 -->

参数说明

表6-1660参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

将输入的两个分量遵循CAST_ROUND模式转换成的half2类型数据。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_fp16.h"头文件。

```cpp
#include "simt_api/asc_fp16.h"
```

调用示例

SIMD与SIMT混合编程场景：// 使用小向量可提升数据搬运效率__simt_vf__ __launch_bounds__(1024) inline void simt_float22half2_rna(__gm__ float2* input, __gm__ half2* output, uint32_t input_total_length){    uint32_t idx = blockIdx.x * blockDim.x + threadIdx.x;    // 每个线程处理1个float2类型的数据，即2个float类型的数据，因此idx >= input_total_length / 2的线程不处理数据    if (idx >= input_total_length / 2) {        return;    }    output[idx] = __float22half2_rna(input[idx]);}

```cpp
__global__ __vector__ void cast_kernel(__gm__ float* input, __gm__ half* output, uint32_t input_total_length){    asc_vf_call<simt_float22half2_rna>(dim3(1024), (__gm__ float2*)input, (__gm__ half2*)output, input_total_length);}
```

## 6.3.9.26 __float22half2_rna_sat

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

<!-- page 3382 -->

产品是否支持

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

饱和模式下，将float2类型数据的两个分量遵循CAST_ROUND模式转换为半精度浮点数，返回转换后的half2类型数据。

函数原型

```cpp
inline half2 __float22half2_rna_sat(const float2 x)
```

参数说明

表6-1661参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

饱和模式下将输入的两个分量遵循CAST_ROUND模式转换成的half2类型数据。

约束说明

使用此接口前需将CTRL[60]寄存器设置为0，否则饱和模式不生效。设置方式请参见控制饱和行为的方式。

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_fp16.h"头文件。

```cpp
#include "simt_api/asc_fp16.h"
```

调用示例

SIMD与SIMT混合编程场景：// 使用小向量可提升数据搬运效率__simt_vf__ __launch_bounds__(1024) inline void simt_float22half2_rna_sat(__gm__ float2* input, __gm__ half2* output, uint32_t input_total_length){
