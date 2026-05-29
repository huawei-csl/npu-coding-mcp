# asc_threadfence

> **Section**: 6.3.3.2  
> **PDF Pages**: 3102–3102  

---

<!-- page 3102 -->

函数原型

```cpp
inline void asc_syncthreads()
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

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void KernelSyncThreads(__gm__ float* dst, int count){     int idx = threadIdx.x;     if (idx > 0 && idx < count) {         dst[idx] = 1;     }     // 等待block内所有thread都执行到当前代码     asc_syncthreads();     if (idx == 0) {         dst[0] = 0;         for(int i = 1023; i > 0; i--) {             dst[0] += dst[i];         }     }}输出结果:[1023, 1, 1, 1 …]

## 6.3.3.2 asc_threadfence

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x
