# __int2float_rna

> **Section**: 6.3.9.171  
> **PDF Pages**: 3565–3565  

---

<!-- page 3565 -->

参数说明

表6-1805参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_CEIL模式转换成的浮点数。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/device_functions.h"头文件。

```cpp
#include "simt_api/device_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__int2float_ru(__gm__ float* dst, __gm__ int32_t* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __int2float_ru(x[idx]);}

## 6.3.9.171 __int2float_rna

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x
