# asc_reduce_min

> **Section**: 6.3.8.11  
> **PDF Pages**: 3336–3336  

---

<!-- page 3336 -->

返回值说明

Warp内所有活跃线程输入val的最大值。

约束说明

无

需要包含的头文件

使用除half类型之外的接口需要包含"simt_api/device_warp_functions.h"头文件，使用half类型接口需要包含"simt_api/asc_fp16.h"头文件。

```cpp
#include "simt_api/device_warp_functions.h" #include "simt_api/asc_fp16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void KernelReduceMax(__gm__ int32_t* dst){    // asc_vf_call参数：dim3{1024, 1, 1}    int idx = threadIdx.x + blockIdx.x * blockDim.x;    int32_t laneId = idx % 32;    int32_t result = asc_reduce_max(laneId); // 返回值为31    dst[idx] = result;}

## 6.3.8.11 asc_reduce_min

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

对Warp内所有活跃线程输入val求最小值。Warp内所有活跃线程返回相同的结果。

函数原型

```cpp
inline int32_t asc_reduce_min(int32_t val)inline uint32_t asc_reduce_min(uint32_t val)
```
