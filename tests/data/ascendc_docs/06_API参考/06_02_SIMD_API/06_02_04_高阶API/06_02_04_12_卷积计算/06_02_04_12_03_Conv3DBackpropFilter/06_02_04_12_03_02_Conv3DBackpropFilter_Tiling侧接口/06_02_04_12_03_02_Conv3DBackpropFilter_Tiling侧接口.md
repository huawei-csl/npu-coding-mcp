# Conv3DBackpropFilter Tiling侧接口

> **Section**: 6.2.4.12.3.2  
> **PDF Pages**: 3065–3065  

---

<!-- page 3065 -->

函数原型

```cpp
__aicore__ inline void End()
```

参数说明

无

返回值说明

无

约束说明

End接口必须在Iterate和GetTensorC接口后调用。

调用示例

const Conv3DBackpropFilterTilingData* tilingData;// ...初始化tilingDataConvBackpropApi::Conv3DBackpropFilter<inputType, weightSizeType, gradOutputType, gradWeightType> gradWeight_;// ...其它调用gradWeight_.End();

## 6.2.4.12.3.2 Conv3DBackpropFilter Tiling 侧接口

## ?.1. Conv3DBackpropFilter Tiling 使用说明

Ascend C提供一组Conv3DBackpropFilter Tiling API，方便用户获取Conv3DBackpropFilter Kernel计算时所需的Tiling参数。用户只需要传入Input/GradOutput/GradWeight的Position位置、Format格式和DType数据类型及相关参数等信息，调用API接口，即可获取Init中TConv3DBpFilterTiling结构体中的相关参数。

Conv3DBackpropFilter Tiling API提供一个GetTiling接口获取Tiling参数，获取Tiling参数的流程如下：

1.创建一个单核Tiling对象。

2.设置Input、GradOutput、GradWeight的参数类型信息以及Shape信息，如果存在Padding、Stride参数，通过SetPadding、SetStride接口设置。

3.调用GetTiling接口，获取Tiling信息。

使用Conv3DBackpropFilter Tiling接口获取Tiling参数的样例如下：

```cpp
#include "tiling/conv_backprop/conv3d_bp_filter_tiling.h"
optiling::Conv3DBackpropFilterTilingData tilingData;auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3dBpFilterTiling conv3dBpDwTiling(*ascendcPlatform);
conv3dBpDwTiling.SetWeightType(ConvCommonApi::TPosition::CO1,                                   ConvCommonApi::ConvFormat::FRACTAL_Z_3D,                                   ConvCommonApi::ConvDtype::FLOAT32);conv3dBpDwTiling.SetInputType(ConvCommonApi::TPosition::GM,                                 ConvCommonApi::ConvFormat::NDC1HWC0,                                 ConvCommonApi::ConvDtype::FLOAT16);conv3dBpDwTiling.SetGradOutputType(ConvCommonApi::TPosition::GM,                                   ConvCommonApi::ConvFormat::NDC1HWC0,                                   ConvCommonApi::ConvDtype::FLOAT16);conv3dBpDwTiling.SetGradOutputShape(n, c, d, h, w);
```
