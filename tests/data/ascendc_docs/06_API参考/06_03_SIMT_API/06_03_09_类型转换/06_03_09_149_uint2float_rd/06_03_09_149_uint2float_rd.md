# __uint2float_rd

> **Section**: 6.3.9.149  
> **PDF Pages**: 3539–3539  

---

<!-- page 3539 -->

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/device_functions.h"头文件。

```cpp
#include "simt_api/device_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__uint2float_rz(__gm__ float* dst, __gm__ uint32_t* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __uint2float_rz(x[idx]);}

## 6.3.9.149 __uint2float_rd

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

遵循CAST_FLOOR模式，将uint32类型数据转换为浮点数，返回转换后的值。

函数原型

```cpp
inline float __uint2float_rd(const unsigned int x)
```
