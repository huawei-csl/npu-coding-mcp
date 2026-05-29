# Conv3DBackpropInput Tiling构造函数

> **Section**: 2  
> **PDF Pages**: 3039–3040  

---

<!-- page 3039 -->

1.创建一个单核Tiling对象。

2.设置Input、GradOutput、Weight的参数类型信息以及Shape信息，如果存在Padding、Stride参数，通过SetPadding、SetStride接口设置。

3.调用GetTiling接口，获取Tiling信息。

使用Conv3DBackpropInput Tiling接口获取Tiling参数的样例如下：

```cpp
#include "tiling/conv_backprop/conv3d_bp_input_tiling.h"
optiling::Conv3DBackpropInputTilingData tilingData;auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3DBpInputTiling conv3DBpDxTiling(*ascendcPlatform);conv3DBpDxTiling.SetWeightType(Convolution3DBackprop::TPosition::GM,                                   Convolution3DBackprop::ConvFormat::FRACTAL_Z_3D,                                   Convolution3DBackprop::ConvDtype::FLOAT32);conv3DBpDxTiling.SetGradOutputType(Convolution3DBackprop::TPosition::GM,                                   Convolution3DBackprop::ConvFormat::NDC1HWC0,                                   Convolution3DBackprop::ConvDtype::FLOAT16);conv3DBpDxTiling.SetInputType(Convolution3DBackprop::TPosition::CO1,                                 Convolution3DBackprop::ConvFormat::NDC1HWC0,                                 Convolution3DBackprop::ConvDtype::FLOAT16);conv3DBpDxTiling.SetInputShape(orgN, orgCi, orgDi, orgHi, orgWi);conv3DBpDxTiling.SetGradOutputShape(orgCo, orgDo, orgHo, orgWo);conv3DBpDxTiling.SetWeightShape(orgKd, orgKh, orgKw);conv3DBpDxTiling.SetPadding(padFront, padBack, padUp, padDown, padLeft, padRight);conv3DBpDxTiling.SetStride(strideD, strideH, strideW);conv3DBpDxTiling.SetDilation(dilationD, dilationH, dilationW);int ret = conv3DBpDxTiling.GetTiling(tilingData);    // if ret = -1, get tiling failed
```

需要包含的头文件

```cpp
#include "lib/conv_backprop/conv3d_bp_input_tiling.h"
```

## ?.2. Conv3DBackpropInput Tiling 构造函数

功能说明

用于创建一个Conv3DBackpropInput 单核Tiling对象。

函数原型

●带参构造函数，需要传入硬件平台信息，推荐使用这类构造函数来获得更好的兼容性。

–使用PlatformAscendC类传入信息explicit Conv3DBpInputTiling(const platform_ascendc::PlatformAscendC& ascendcPlatform)

–使用PlatformInfo传入信息

当platform_ascendc::PlatformAscendC无法在Tiling运行时获取时，需要用户自己构造PlatformInfo结构体，透传给Conv3DBpInputTiling构造函数。explicit Conv3DBpInputTiling(const PlatformInfo& platform)

●无参构造函数Conv3DBpInputTiling()

●基类构造函数

Conv3DBpInputTiling继承自基类Conv3DBpInputTilingBase，其构造函数如下：

```cpp
Conv3DBpInputTilingBase()explicit Conv3DBpInputTilingBase(const platform_ascendc::PlatformAscendC& ascendcPlatform)explicit Conv3DBpInputTilingBase(const PlatformInfo& platform)
```

<!-- page 3040 -->

参数说明

表6-1406参数说明

参数名输入/输出

描述

ascendcPlatform

输入传入硬件平台的信息，PlatformAscendC定义请参见6.4.2.1.2 构造及析构函数。

platform输入传入硬件版本以及AI Core中各个硬件单元提供的内存大小。PlatformInfo构造时通过6.4.2.1.2 构造及析构函数获取。

PlatformInfo结构定义如下，socVersion通过6.4.2.1.4GetSocVersion获取并透传，各类硬件存储空间大小通过6.4.2.1.11 GetCoreMemSize获取并透传。struct PlatformInfo {    platform_ascendc::SocVersion socVersion;    uint64_t l1Size = 0;    uint64_t l0CSize = 0;    uint64_t ubSize = 0;    uint64_t l0ASize = 0;    uint64_t l0BSize = 0;};

不推荐通过直接填值构造PlatformInfo的方式调用构造函数，例如PlatformInfo(, 1024, 1024, ..);

在实现Host侧的Tiling函数时，platform_ascendc::PlatformAscendC用于获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。PlatformAscendC类提供获取这些平台信息的功能。

和platform_ascendc::PlatformAscendC不同的是，PlatformInfo则用于获取芯片版本以及AI Core中各个硬件单元提供的内存大小等只针对单个AI Core的信息。

约束说明

无

调用示例

●无参构造函数ConvBackpropApi::Conv3DBpInputTiling tiling;tiling.SetWeightType(ConvCommonApi::TPosition::GM,ConvCommonApi::ConvFormat::FRACTAL_Z_3D,ConvCommonApi::ConvDtype::FLOAT16);...optiling::Conv3DBackpropInputTilingData tilingData; int ret = tiling.GetTiling(tilingData);    // if ret = -1, gen tiling failed...

●带参构造函数auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());ConvBackpropApi::Conv3DBpInputTiling tiling(ascendcPlatform); tiling.SetWeightType(ConvCommonApi::TPosition::GM,ConvCommonApi::ConvFormat::FRACTAL_Z_3D,ConvCommonApi::ConvDtype::FLOAT16);...optiling::Conv3DBackpropInputTilingData tilingData; int ret = tiling.GetTiling(tilingData);    // if ret = -1, gen tiling failed
