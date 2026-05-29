# __float2float_rn

> **Section**: 6.3.9.2  
> **PDF Pages**: 3350–3351  

---

<!-- page 3350 -->

输入数据类型

输出数据类型

精度转换规则示例

int64_tfloat示例1：输入225 + 3，写成float的表示形式：225 * (1 + 2-24 +2-25)，要求E = 25 + 127 = 152，M = 2-24 + 2-25。

由于float只有23bit尾数位，因此要进行舍入。

CAST_RINT模式舍入得尾数00000000000000000000001，E= 152，M = 2-23，最终表示的结果为225 + 4；

CAST_FLOOR模式舍入得尾数00000000000000000000000，E = 152，M = 0，最终表示的结果为225；

CAST_CEIL模式舍入得尾数00000000000000000000001，E =152，M = 2-23，最终表示的结果为225 + 4；

CAST_ROUND模式舍入得尾数00000000000000000000001，E = 152，M = 2-23，最终表示的结果为225 + 4；

CAST_TRUNC模式舍入得尾数00000000000000000000000，E = 152，M = 0，最终表示的结果为225。

uint64_tfloat示例1：输入225 + 3，写成float的表示形式：225 * (1 + 2-24 +2-25)，要求E = 25 + 127 = 152，M = 2-24 + 2-25。

由于float只有23bit尾数位，因此要进行舍入。

CAST_RINT模式舍入得尾数00000000000000000000001，E= 152，M = 2-23，最终表示的结果为225 + 4；

CAST_FLOOR模式舍入得尾数00000000000000000000000，E = 152，M = 0，最终表示的结果为225；

CAST_CEIL模式舍入得尾数00000000000000000000001，E =152，M = 2-23，最终表示的结果为225 + 4；

CAST_ROUND模式舍入得尾数00000000000000000000001，E = 152，M = 2-23，最终表示的结果为225 + 4；

CAST_TRUNC模式舍入得尾数00000000000000000000000，E = 152，M = 0，最终表示的结果为225。

## 6.3.9.2 __float2float_rn

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

<!-- page 3351 -->

产品是否支持

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

将浮点数四舍五入取整，并遵循CAST_RINT模式。

函数原型

```cpp
inline float __float2float_rn(const float x)
```

参数说明

表6-1637参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_RINT模式取整后的浮点数。

约束说明

float转float只支持非饱和行为。

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/device_functions.h"头文件。

```cpp
#include "simt_api/device_functions.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel__float2float_rn(__gm__ float* dst, __gm__ float* x){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = __float2float_rn(x[idx]);}
