# 使能Cache Hints的Load/Store函数

> **Section**: 6.3.11  
> **PDF Pages**: 3696–3703  

---

<!-- page 3696 -->

功能说明

使用给定的两个bfloat16_t类型的数据创建一个bfloat16x2_t类型的向量。对于16位类型的数据，底层指令支持一次完成两个数据的计算，通过构造向量类型可以提高数据计算效率。

函数原型

```cpp
inline bfloat16x2_t make_bfloat162(bfloat16_t x, bfloat16_t y)
```

参数说明

表6-1910参数说明

参数名输入/输出

描述

x输入源操作数。

y输入源操作数。

返回值说明

由两个bfloat16类型数字构成的新bfloat16x2_t向量。

约束说明

SIMT编程场景当前不支持使用该接口。

需要包含的头文件

使用该接口需要包含"simt_api/asc_bf16.h"头文件。

```cpp
#include "simt_api/asc_bf16.h"
```

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel_make_bfloat162(__gm__ bfloat16x2_t* dst, __gm__ bfloat16_t* x, __gm__ bfloat16_t* y){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = make_bfloat162(x[idx], y[idx]);}

## 6.3.11 使能Cache Hints 的Load/Store 函数

