# asc_reduce_max

> **Section**: 6.3.8.10  
> **PDF Pages**: 3335–3335  

---

<!-- page 3335 -->

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void KernelReduceAdd(__gm__ int32_t* dst){     // asc_vf_call参数：dim3{1024, 1, 1}     int idx = threadIdx.x + blockIdx.x * blockDim.x;     int32_t laneId = idx % 32;     int32_t result = asc_reduce_add(laneId); // 返回值为0+1+2+...+31=496     dst[idx] = result;}

## 6.3.8.10 asc_reduce_max

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

对Warp内所有活跃线程输入的val求最大值。Warp内所有活跃线程返回相同的结果。

函数原型

```cpp
inline int32_t asc_reduce_max(int32_t val)inline uint32_t asc_reduce_max(uint32_t val)inline float asc_reduce_max(float val)inline half asc_reduce_max(half val)
```

参数说明

表6-1629参数说明

参数名输入/输出

描述

val输入源操作数。
