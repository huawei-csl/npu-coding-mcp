# __float2half_ro_sat

> **Section**: 6.3.9.28  
> **PDF Pages**: 3384–3384  

---

<!-- page 3384 -->

●当x为nan时，返回值为nan。

●当x为inf时，返回值为inf。

●当x为-inf时，返回值为-inf。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_fp16.h"头文件。

```cpp
#include "simt_api/asc_fp16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2half_ro(__gm__ half* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2half_ro(x[idx]);}

## 6.3.9.28 __float2half_ro_sat

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

饱和模式下，将浮点数转换为半精度浮点数，并遵循CAST_ODD模式，返回转换后的值。

函数原型

```cpp
inline half __float2half_ro_sat(const float x)
```
