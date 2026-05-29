# __float2float_rz

> **Section**: 6.3.9.3  
> **PDF Pages**: 3352–3352  

---

<!-- page 3352 -->

## 6.3.9.3 __float2float_rz

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

将浮点数四舍五入取整，并遵循CAST_TRUNC模式。

函数原型

```cpp
inline float __float2float_rz(const float x)
```

参数说明

表6-1638参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_TRUNC模式取整后的浮点数。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/device_functions.h"头文件。

```cpp
#include "simt_api/device_functions.h"
```
