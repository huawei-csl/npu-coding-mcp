# __bfloat162half_rz_sat

> **Section**: 6.3.9.114  
> **PDF Pages**: 3495–3496  

---

<!-- page 3495 -->

参数说明

表6-1748参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_TRUNC模式转换成的half类型数据。特别场景说明如下：

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

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__bfloat162half_rz(__gm__ half* dst, __gm__ bfloat16_t* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __bfloat162half_rz(x[idx]);}

## 6.3.9.114 __bfloat162half_rz_sat

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

<!-- page 3496 -->

产品是否支持

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

饱和模式下，将bfloat16类型数据转换为half类型数据，并遵循CAST_TRUNC模式，返回转换后的值。

函数原型

```cpp
inline half __bfloat162half_rz_sat(const bfloat16_t x)
```

参数说明

表6-1749参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

饱和模式下将输入遵循CAST_TRUNC模式转换成的half类型数据。

约束说明

使用此接口前需将CTRL[60]寄存器设置为0，否则饱和模式不生效。设置方式请参见控制饱和行为的方式。

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__bfloat162half_rz_sat(__gm__ half* dst, __gm__ bfloat16_t* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __bfloat162half_rz_sat(x[idx]);}
