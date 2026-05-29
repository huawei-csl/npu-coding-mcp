# __uint2bfloat16_rna

> **Section**: 6.3.9.166  
> **PDF Pages**: 3559–3560  

---

<!-- page 3559 -->

功能说明

遵循CAST_CEIL模式，将uint32类型数据转换为bfloat16类型数据，返回转换后的值。

函数原型

```cpp
inline bfloat16_t __uint2bfloat16_ru(const unsigned int x)
```

参数说明

表6-1800参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_CEIL模式转换成的bfloat16类型数据。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__uint2bfloat16_ru(__gm__ bfloat16_t* dst, __gm__ uint32_t* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __uint2bfloat16_ru(x[idx]);}

## 6.3.9.166 __uint2bfloat16_rna

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

<!-- page 3560 -->

产品是否支持

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

遵循CAST_ROUND模式，将uint32类型数据转换为bfloat16类型数据，返回转换后的值。

函数原型

```cpp
inline bfloat16_t __uint2bfloat16_rna(const unsigned int x)
```

参数说明

表6-1801参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_ROUND模式转换成的bfloat16类型数据。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__uint2bfloat16_rna(__gm__ bfloat16_t* dst, __gm__ uint32_t* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __uint2bfloat16_rna(x[idx]);}
