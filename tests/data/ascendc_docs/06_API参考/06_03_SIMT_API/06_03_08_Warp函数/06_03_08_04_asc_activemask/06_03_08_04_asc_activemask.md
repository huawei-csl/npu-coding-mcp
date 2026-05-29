# asc_activemask

> **Section**: 6.3.8.4  
> **PDF Pages**: 3324–3324  

---

<!-- page 3324 -->

参数说明

表6-1623参数说明

参数名输入/输出

描述

predicate

输入操作数。

返回值说明

32bit的无符号整数：若Warp内活跃线程输入的predicate不为0，则返回值中与线程LaneId对应的bit位为1，否则为0。

约束说明

无

需要包含的头文件

使用该接口需要包含"simt_api/device_warp_functions.h"头文件。

```cpp
#include "simt_api/device_warp_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void KernelBallot(__gm__ uint32_t* dst){    // asc_vf_call参数：dim3{1024, 1, 1}    int idx = threadIdx.x + blockIdx.x * blockDim.x;    int32_t laneId = idx % 32;    uint32_t result = asc_ballot(laneId); // 返回值为0xfffffffe    dst[idx] = result;}

## 6.3.8.4 asc_activemask

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex
