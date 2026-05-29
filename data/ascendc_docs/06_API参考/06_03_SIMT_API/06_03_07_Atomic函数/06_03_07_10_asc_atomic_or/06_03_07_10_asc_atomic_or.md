# asc_atomic_or

> **Section**: 6.3.7.10  
> **PDF Pages**: 3317–3318  

---

<!-- page 3317 -->

需要包含的头文件

使用该接口需要包含"simt_api/device_atomic_functions.h"头文件。

```cpp
#include "simt_api/device_atomic_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：

SIMD与SIMT混合编程场景，需要显式使用地址空间限定符表示地址空间：__gm__表示Global Memory内存空间，__ubuf__表示Unified Buffer内存空间。__simt_vf__ __launch_bounds__(1024) inline void KernelAtomicAnd(__gm__ int32_t* dst, __gm__ int32_t* src){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    asc_atomic_and(dst + idx, src[idx]);}

## 6.3.7.10 asc_atomic_or

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

对Unified Buffer或Global Memory上address的数值与指定数值val进行原子或（|）操作，即将address数值或（|）val的结果赋值到Unified Buffer或Global Memory上。

函数原型

```cpp
inline int32_t asc_atomic_or(int32_t *address, int32_t val)inline uint32_t asc_atomic_or(uint32_t *address, uint32_t val)inline int64_t asc_atomic_or(int64_t *address, int64_t val)inline uint64_t asc_atomic_or(uint64_t *address, uint64_t val)
```

<!-- page 3318 -->

参数说明

表6-1617参数说明

参数名输入/输出描述

address输出Unified Buffer或Global Memory的地址。

val输入源操作数。

不同数据类型支持的内存范围说明如下：

表6-1618不同数据类型支持的内存范围

参数数据类型支持的内存空间

int32_t、uint32_tUnified Buffer、Global Memory

int64_t、uint64_tGlobal Memory

返回值说明

Unified Buffer或Global Memory上的初始数据。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/device_atomic_functions.h"头文件。

```cpp
#include "simt_api/device_atomic_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：

SIMD与SIMT混合编程场景，需要显式使用地址空间限定符表示地址空间：__gm__表示Global Memory内存空间，__ubuf__表示Unified Buffer内存空间。__simt_vf__ __launch_bounds__(1024) inline void KernelAtomicOr(__gm__ int32_t* dst, __gm__ int32_t* src){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    asc_atomic_or(dst + idx, src[idx]);}
