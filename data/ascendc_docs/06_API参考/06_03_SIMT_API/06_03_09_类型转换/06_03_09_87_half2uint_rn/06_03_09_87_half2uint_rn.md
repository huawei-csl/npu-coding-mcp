# __half2uint_rn

> **Section**: 6.3.9.87  
> **PDF Pages**: 3461–3461  

---

<!-- page 3461 -->

需要包含的头文件

使用该接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__half2bfloat16_rna(__gm__ bfloat16_t* dst, __gm__ half* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __half2bfloat16_rna(x[idx]);}

## 6.3.9.87 __half2uint_rn

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

遵循CAST_RINT模式，将half类型数据转换为无符号整数，返回转换后的值。

函数原型

```cpp
inline unsigned int __half2uint_rn(const half x)
```

参数说明

表6-1722参数说明

参数名输入/输出

描述

x输入源操作数。
