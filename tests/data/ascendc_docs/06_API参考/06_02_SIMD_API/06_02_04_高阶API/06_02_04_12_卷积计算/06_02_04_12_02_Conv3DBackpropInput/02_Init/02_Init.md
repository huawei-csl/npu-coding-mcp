# Init

> **Section**: 2  
> **PDF Pages**: 3029–3030  

---

<!-- page 3029 -->

表6-1398 Conv3DBackpropInput 输入输出数据类型的组合说明

**WeightGradOutputInputSize**

**GradInput**

支持平台

halfhalfint32_thalf●Atlas A3 训练系列产品/Atlas A3 推理系列产品

●Atlas A2 训练系列产品/Atlas A2 推理系列产品

bfloat16_tbfloat16_tint32_tbfloat16_t

●Atlas A3 训练系列产品/Atlas A3 推理系列产品

●Atlas A2 训练系列产品/Atlas A2 推理系列产品

步骤2初始化操作。

// 注册后进行初始化ConvBackpropApi::Conv3DBackpropInput<weightDxType, inputSizeDxType, gradOutputDxType, gradInputDxType> gradInput_;gradInput_.Init(&(tilingData->conv3DDxTiling));

步骤3设置3D卷积的输出反向GradOutput、3D卷积的输入Weight。

gradInput_.SetSingleShape(singleShapeM_, singleShapeK_, singleShapeN_); // 设置单核计算的形状gradInput_.SetStartPosition(dinStartIdx_, curHoStartIdx_); // 设置单核上gradOutput载入的起始位置gradInput_.SetGradOutput(gradOutputGm_[offsetA_]);gradInput_.SetWeight(weightGm_[offsetB_]);

步骤4完成卷积反向操作。

调用Iterate完成单次迭代计算，叠加while循环完成单核全量数据的计算。Iterate方式，可以自行控制迭代次数，完成所需数据量的计算。while (gradInput_.Iterate()) {    gradInput_.GetTensorC(gradInputGm_[offsetC_]); }

步骤5结束卷积反向操作。

```cpp
gradInput_.End();
```

**----结束**

需要包含的头文件

```cpp
#include "lib/conv_backprop/conv3d_bp_input_api.h"
```

## ?.2. Init

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

<!-- page 3030 -->

产品是否支持

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

Init主要用于对Conv3DBackpropInput对象中的Tiling数据进行初始化，根据Tiling参数进行资源划分，Tiling参数的具体介绍请参考 Conv3DBackpropInput Tiling侧接口。

函数原型

```cpp
__aicore__ inline void Init(const TConv3DBackpropInputTiling *__restrict tiling)
```

参数说明

表6-1399接口参数说明

参数名输入/输出

描述

tiling输入Conv3DBackpropInput对象的Tiling参数，TConv3DBackpropInputTiling结构体的定义请参见TConv3DBackpropInputTiling结构体。

Tiling参数可以通过Host侧 GetTiling接口获取，并传递到Kernel侧使用。

返回值说明

无

约束说明

Init接口必须在Iterate、GetTensorC、End接口前调用，且只能调用一次Init接口，调用顺序如下。Init(...);...Iterate(...);GetTensorC(...);End();

调用示例

const Conv3DBackpropInputTilingData* tilingData;// ...初始化tilingData后，创建Conv3DBackpropInput对象，调用init接口ConvBackpropApi::Conv3DBackpropInput<weightDxType, inputSizeDxType, gradOutputDxType,
