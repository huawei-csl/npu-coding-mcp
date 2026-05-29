# __float22bfloat162_rn_sat

> **Section**: 6.3.9.34  
> **PDF Pages**: 3392–3392  

---

<!-- page 3392 -->

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2bfloat16_rn_sat(__gm__ bfloat16_t* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2bfloat16_rn_sat(x[idx]);}

## 6.3.9.34 __float22bfloat162_rn_sat

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

饱和模式下，将float2类型数据的两个分量遵循CAST_RINT模式转换为bfloat16精度，返回转换后的bfloat16x2_t类型数据。

函数原型

```cpp
inline bfloat16x2_t __float22bfloat162_rn_sat(const float2 x)
```

参数说明

表6-1669参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

饱和模式下将输入的两个分量遵循CAST_RINT模式转换成的bfloat16x2_t类型数据。
