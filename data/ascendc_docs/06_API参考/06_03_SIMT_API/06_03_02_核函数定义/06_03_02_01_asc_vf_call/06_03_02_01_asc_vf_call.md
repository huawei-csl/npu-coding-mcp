# asc_vf_call

> **Section**: 6.3.2.1  
> **PDF Pages**: 3099–3100  

---

<!-- page 3099 -->

**half、half2类型需要包含的头文件**

**bfloat16_t、bfloatx2_t类型需要包含的头文件**

**hifloat8x2_t、float8_e4m3x2_t、float8_e5m2x2_t类型需要包含的头文件**

类别除half、half2、bfloat16、bfloat16x2_t之外的类型需要包含的头文件

#include"simt_api/math_functions.h"

数学函数

精度转换

**Atomic函数#include"simt_api/device_atomic_functions.h"**

**Warp函数#include"simt_api/device_warp_functions.h"**

#include"simt_api/device_functions.h"

类型转换

**Load/Store函数**

#include"simt_api/vector_functions.h"

向量类型构造函数

## 6.3.2 核函数定义

说明

当前仅展示SIMD与SIMT混合编程场景的核函数定义，SIMT编程场景的核函数定义将在后续版本中发布。

## 6.3.2.1 asc_vf_call

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

<!-- page 3100 -->

产品是否支持

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

在SIMD与SIMT混合编程场景，启动SIMT VF（Vector Function）子任务，通过参数配置，启动指定数目的线程，执行指定的SIMT核函数。

说明

asc_vf_call启动SIMT VF子任务时，子任务函数不能是类的成员函数，推荐使用普通函数或类静态函数，且入口函数必须使用__simt_vf__修饰宏。

asc_vf_call启动SIMT VF子任务时，传递的参数只支持裸指针，常见基本数据类型。不支持传递结构体，数组等。

函数原型

```cpp
template <auto funcPtr, typename... Args>__aicore__ inline void asc_vf_call(dim3 threadNums, Args &&...args)
```

参数说明

表6-1453模板参数说明

参数名描述

funcPtr用于指定SIMT入口核函数。

Args定义可变参数，用于传递实参到SIMT入口核函数。

表6-1454参数说明

参数名输入/输出描述

threadNums

输入dim3结构，定义为{dimx，dimy，dimz}，用于指定SIMT线程块内线程数量。线程总数为dimx * dimy * dimz，该值的大小必须小于等于2048。

args输入可变参数，用于传递实参到SIMT入口核函数。

返回值说明

无
