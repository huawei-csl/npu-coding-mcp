# asc_atomic_sub

> **Section**: 6.3.7.2  
> **PDF Pages**: 3304–3304  

---

<!-- page 3304 -->

```cpp
__simt_vf__ __launch_bounds__(1024) inline void KernelAtomicAdd(__gm__ float* dst, __gm__ float* src){    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    asc_atomic_add(dst + idx, src[idx]);}
```

## 6.3.7.2 asc_atomic_sub

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

对Unified Buffer或Global Memory上的数据与指定数据执行原子减操作，即在这些内存区域的数据中减去指定数据。

函数原型

```cpp
inline int32_t asc_atomic_sub(int32_t *address, int32_t val)inline uint32_t asc_atomic_sub(uint32_t *address, uint32_t val)inline float asc_atomic_sub(float *address, float val)inline int64_t asc_atomic_sub(int64_t *address, int64_t val)inline uint64_t asc_atomic_sub(uint64_t *address, uint64_t val)inline half2 asc_atomic_sub(half2 *address, half2 val)inline bfloat16x2_t asc_atomic_sub(bfloat16x2_t *address, bfloat16x2_t val)
```

参数说明

表6-1601参数说明

参数名输入/输出描述

address输出Unified Buffer或Global Memory的地址。

val输入源操作数。

不同数据类型支持的内存范围说明如下：
