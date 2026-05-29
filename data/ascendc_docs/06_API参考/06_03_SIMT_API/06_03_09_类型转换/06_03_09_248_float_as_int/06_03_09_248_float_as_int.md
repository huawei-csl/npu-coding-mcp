# __float_as_int

> **Section**: 6.3.9.248  
> **PDF Pages**: 3661–3662  

---

<!-- page 3661 -->

功能说明

将无符号整数中的位重新解释为浮点数，即将无符号整数存储的位按照float的格式进行读取。

函数原型

```cpp
inline float __uint_as_float(const unsigned int x)
```

参数说明

表6-1882参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入的无符号整数中的位重新解释成的浮点数。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/device_functions.h"头文件。

```cpp
#include "simt_api/device_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__uint_as_float(__gm__ float* dst, __gm__ uint32_t* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __uint_as_float(x[idx]);}

## 6.3.9.248 __float_as_int

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

<!-- page 3662 -->

产品是否支持

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

将浮点数中的位重新解释为有符号整数，即将浮点数存储的位按照有符号整数的格式进行读取。

函数原型

```cpp
inline int __float_as_int(const float x)
```

参数说明

表6-1883参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入的浮点数中的位重新解释成的有符号整数。特别场景说明如下：

●当x为nan时，返回值为2143289344。

●当x为inf时，返回值为2139095040。

●当x为-inf时，返回值为-8388608。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/device_functions.h"头文件。

```cpp
#include "simt_api/device_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float_as_int(__gm__ int32_t* dst, __gm__ float* x){
