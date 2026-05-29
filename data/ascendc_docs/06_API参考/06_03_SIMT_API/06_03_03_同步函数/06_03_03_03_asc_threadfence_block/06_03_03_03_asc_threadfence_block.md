# asc_threadfence_block

> **Section**: 6.3.3.3  
> **PDF Pages**: 3103–3103  

---

<!-- page 3103 -->

产品是否支持

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

在SIMT编程范式中，来自不同线程对同一份内存的读写操作可能造成数据竞争（DataRace）。asc_threadfence接口用于保证不同线程对同一份全局、共享内存的访问过程中，写入操作的时序性。它不会阻塞线程，仅保证内存操作的可见性顺序。

函数原型

```cpp
inline void asc_threadfence()
```

参数说明

无

返回值说明

无

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/device_sync_functions.h"头文件。

```cpp
#include "simt_api/device_sync_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void KernelThreadFence(__gm__ float* dst, __gm__ float* src){    src[0] = src[0] + 1;    asc_threadfence(); // asc_threadfence()保证本线程的写操作顺序对全局可见    dst[0] = src[0];}

## 6.3.3.3 asc_threadfence_block

产品支持情况

产品是否支持

Atlas 350 加速卡√
