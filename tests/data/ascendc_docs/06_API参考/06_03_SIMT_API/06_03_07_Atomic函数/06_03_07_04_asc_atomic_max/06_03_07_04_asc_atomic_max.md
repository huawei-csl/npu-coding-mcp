# asc_atomic_max

> **Section**: 6.3.7.4  
> **PDF Pages**: 3307–3308  

---

<!-- page 3307 -->

需要包含的头文件

使用除half2、bfloat16x2_t类型之外的接口需要包含"simt_api/device_atomic_functions.h"头文件，使用half2类型接口需要包含"simt_api/asc_fp16.h"头文件，使用bfloat16x2_t类型接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/device_atomic_functions.h"#include "simt_api/asc_fp16.h"#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：

SIMD与SIMT混合编程场景，需要显式使用地址空间限定符表示地址空间：__gm__表示Global Memory内存空间，__ubuf__表示Unified Buffer内存空间。__simt_vf__ __launch_bounds__(1024) inline void KernelAtomicExch(__gm__ int32_t* dst, __gm__ int32_t* src){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    asc_atomic_exch(dst + idx, src[idx]);}

## 6.3.7.4 asc_atomic_max

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

对Unified Buffer或Global Memory数据做原子求最大值操作，即将Unified Buffer或Global Memory的数据与指定数据中的最大值赋值到Unified Buffer或Global Memory地址中。

函数原型

```cpp
inline int32_t asc_atomic_max(int32_t *address, int32_t val)inline uint32_t asc_atomic_max(uint32_t *address, uint32_t val)inline float asc_atomic_max(float *address, float val)inline int64_t asc_atomic_max(int64_t *address, int64_t val)inline uint64_t asc_atomic_max(uint64_t *address, uint64_t val)inline half asc_atomic_max(half *address, half val)
```

<!-- page 3308 -->

```cpp
inline bfloat16_t asc_atomic_max(bfloat16_t *address, bfloat16_t val)inline half2 asc_atomic_max(half2 *address, half2 val)inline bfloat16x2_t asc_atomic_max(bfloat16x2_t *address, bfloat16x2_t val)
```

参数说明

表6-1605参数说明

参数名输入/输出

描述

address输出Unified Buffer或Global Memory的地址。

val输入源操作数。

不同数据类型支持的内存范围说明如下：

表6-1606不同数据类型支持的内存范围

参数数据类型支持的内存空间

int32_t、uint32_t、float、half、bfloat16_t、half2、bfloat16x2_t

Unified Buffer、Global Memory

int64_t、uint64_tGlobal Memory

返回值说明

Unified Buffer或Global Memory上的初始数据。

注意，由于底层硬件约束，half和bfloat16_t类型的返回值不准确，避免直接使用这些类型的返回值。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用除half、half2、bfloat16_t、bfloat16x2_t类型之外的接口需要包含"simt_api/device_atomic_functions.h"头文件，使用half和half2类型接口需要包含"simt_api/asc_fp16.h"头文件，使用bfloat16_t和bfloat16x2_t类型接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/device_atomic_functions.h"#include "simt_api/asc_fp16.h"#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：
