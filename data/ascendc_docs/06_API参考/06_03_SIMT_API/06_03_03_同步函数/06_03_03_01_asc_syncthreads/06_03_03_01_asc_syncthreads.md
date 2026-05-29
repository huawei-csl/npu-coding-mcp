# asc_syncthreads

> **Section**: 6.3.3.1  
> **PDF Pages**: 3101–3101  

---

<!-- page 3101 -->

约束说明

SIMT编程场景不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/common_functions.h"头文件。

```cpp
#include "simt_api/common_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：

对Global Memory数据做加法计算。__simt_vf__ __launch_bounds__(2048) inline void SimtCompute(    __gm__ float* dst, __gm__ float* src0, __gm__ float* src1, int count) const{    // simt 代码    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = src0[idx] + src1[idx];}

__global__ __vector__ void SimtComputeShell(__gm__ float* x, __gm__ float* y, __gm__ float* z, const int size){    __gm__ float* dst = x;    __gm__ float* src0 = y;    __gm__ float* src1 = z;    // asc_vf_call启动SIMT VF子任务    asc_vf_call<SimtCompute>(dim3{1024, 1, 1}, dst, src0, src1, size);}

## 6.3.3 同步函数

## 6.3.3.1 asc_syncthreads

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

等待当前线程块内所有线程代码都执行到该函数位置。
