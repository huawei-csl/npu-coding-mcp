# Init

> **Section**: 2  
> **PDF Pages**: 3056–3056  

---

<!-- page 3056 -->

```cpp
gradWeight_.End();
```

**----结束**

需要包含的头文件

```cpp
#include "lib/conv_backprop/conv3d_bp_filter_api.h"
```

## ?.2. Init

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

Init主要用于对Conv3DBackpropFilter对象中的Tiling数据进行初始化，根据Tiling参数进行资源划分，Tiling参数的具体介绍请参考 Conv3DBackpropFilter Tiling侧接口。

函数原型

```cpp
__aicore__ inline void Init(const TConv3DBpFilterTiling *__restrict tiling)
```

参数说明

表6-1421接口参数说明

参数名输入/输出

描述

tiling输入Conv3DBackpropFilter对象的Tiling参数，Conv3DBackpropFilterTilingData结构体定义请参见TConv3DBpFilterTiling结构体。

Tiling参数可以通过Host侧 GetTiling接口获取，并传递到Kernel侧使用。

返回值说明

无
