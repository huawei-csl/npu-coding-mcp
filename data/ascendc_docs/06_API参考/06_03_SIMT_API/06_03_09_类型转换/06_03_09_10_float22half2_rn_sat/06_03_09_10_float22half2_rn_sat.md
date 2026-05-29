# __float22half2_rn_sat

> **Section**: 6.3.9.10  
> **PDF Pages**: 3360–3360  

---

<!-- page 3360 -->

约束说明

使用此接口前需将CTRL[60]寄存器设置为0，否则饱和模式不生效。设置方式请参见控制饱和行为的方式。

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_fp16.h"头文件。

```cpp
#include "simt_api/asc_fp16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2half_rn_sat(__gm__ half* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2half_rn_sat(x[idx]);}

## 6.3.9.10 __float22half2_rn_sat

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

饱和模式下，将float2类型数据的两个分量遵循CAST_RINT模式转换为半精度浮点数，返回转换后的half2类型数据。

函数原型

```cpp
inline half2 __float22half2_rn_sat(const float2 x)
```
