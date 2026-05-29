# __float2ull_rn

> **Section**: 6.3.9.61  
> **PDF Pages**: 3427–3427  

---

<!-- page 3427 -->

返回值说明

输入遵循CAST_ROUND模式转换成的有符号整数。特别场景说明如下：

●当x为nan时，返回值为0。

●当x为inf时，返回值为2147483647。

●当x为-inf时，返回值为-2147483648。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/device_functions.h"头文件。

```cpp
#include "simt_api/device_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2int_rna(__gm__ int32_t* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2int_rna(x[idx]);}

## 6.3.9.61 __float2ull_rn

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

遵循CAST_RINT模式，将浮点数转换为64位无符号整数，返回转换后的值。

函数原型

```cpp
inline unsigned long long int __float2ull_rn(const float x)
```
