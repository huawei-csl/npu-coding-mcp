# __lowhigh2highlow

> **Section**: 6.3.9.233  
> **PDF Pages**: 3642–3642  

---

<!-- page 3642 -->

## 6.3.9.233 __lowhigh2highlow

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

将输入数据的高低16位进行交换并返回。

函数原型

```cpp
inline half2 __lowhigh2highlow(const half2 x)__simt_callee__ inline bfloat16x2_t __lowhigh2highlow(const bfloat16x2_t x)
```

参数说明

表6-1868参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入数据的高低16位进行交换的结果。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用bfloat16x2_t接口需要包含"simt_api/asc_bf16.h"头文件，使用half2接口需要包含"simt_api/asc_fp16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```
