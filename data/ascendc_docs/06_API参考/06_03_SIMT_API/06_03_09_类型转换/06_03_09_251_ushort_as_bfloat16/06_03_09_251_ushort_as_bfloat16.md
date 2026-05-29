# __ushort_as_bfloat16

> **Section**: 6.3.9.251  
> **PDF Pages**: 3665–3665  

---

<!-- page 3665 -->

参数说明

表6-1885参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

unsigned short int的数据按位重新解释为half的值。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_fp16.h"头文件。

```cpp
#include "simt_api/asc_fp16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__ushort_as_half(__gm__ half * dst, __gm__ unsigned short int* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __ushort_as_half(x[idx]);}

## 6.3.9.251 __ushort_as_bfloat16

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x
