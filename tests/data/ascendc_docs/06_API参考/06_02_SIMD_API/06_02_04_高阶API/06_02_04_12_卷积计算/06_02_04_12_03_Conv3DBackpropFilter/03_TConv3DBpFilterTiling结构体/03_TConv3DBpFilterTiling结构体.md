# TConv3DBpFilterTiling结构体

> **Section**: 3  
> **PDF Pages**: 3067–3069  

---

<!-- page 3067 -->

参数名输入/输出

描述

platform输入传入硬件版本以及AI Core中各个硬件单元提供的内存大小。PlatformInfo构造时通过6.4.2.1.2 构造及析构函数获取。

PlatformInfo结构定义如下，socVersion通过6.4.2.1.4GetSocVersion获取并透传，各类硬件存储空间大小通过6.4.2.1.11 GetCoreMemSize获取并透传。struct PlatformInfo {    platform_ascendc::SocVersion socVersion;    uint64_t l1Size = 0;    uint64_t l0CSize = 0;    uint64_t ubSize = 0;    uint64_t l0ASize = 0;    uint64_t l0BSize = 0;};

不推荐通过直接填值构造PlatformInfo的方式调用构造函数，例如PlatformInfo(, 1024, 1024, ..);

在实现Host侧的Tiling函数时，platform_ascendc::PlatformAscendC用于获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。PlatformAscendC类提供获取这些平台信息的功能。

和platform_ascendc::PlatformAscendC不同的是，PlatformInfo则用于获取芯片版本以及AI Core中各个硬件单元提供的内存大小等只针对单个AI Core的信息。

约束说明

无

使用样例

●无参构造函数Convolution3DBackprop::Conv3dBpFilterTiling tiling;tiling.SetWeightType(ConvCommonApi::TPosition::GM,ConvCommonApi::ConvFormat::FRACTAL_Z_3D,ConvCommonApi::ConvDtype::FLOAT32);...optiling::Conv3DBackpropFilterTilingData tilingData; int ret = tiling.GetTiling(tilingData);    // if ret = -1, gen tiling failed...

●带参构造函数auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());ConvBackpropApi::Conv3dBpFilterTiling tiling(ascendcPlatform); tiling.SetWeightType(ConvCommonApi::TPosition::GM,Convolution3DBackprop::ConvFormat::FRACTAL_Z_3D,ConvCommonApi::ConvDtype::FLOAT32);...optiling::Conv3DBackpropFilterTilingData tilingData; int ret = tiling.GetTiling(tilingData);    // if ret = -1, gen tiling failed

## ?.3. TConv3DBpFilterTiling 结构体

TConv3DBpFilterTiling结构体包含Conv3dBackpropFilter算子规格信息及Tiling切分算法的相关参数，被传递给Conv3dBackpropFilter Kernel侧，用于数据切分、数据搬运和计算等。TConv3DBpFilterTiling结构体的参数说明见表6-1430。

用户通过调用GetTiling接口获取TConv3DBpFilterTiling结构体，具体流程请参考使用说明。当前暂不支持用户自定义配置TConv3DBpFilterTiling结构体中的参数。

<!-- page 3068 -->

表6-1430 TConv3DBpFilterTiling 结构说明

参数名称说明

batch输入GradOutput的Batch，单位元素。

cin输入Input的Channel，单位元素。

cout输入GradOutput的Channel，单位元素。

cin1G预留参数，用户无需感知。

cout1G预留参数，用户无需感知。

dout输入GradOutput的Depth，单位元素。

ho输入GradOutput的Height，单位元素。

wo输入GradOutput的Width，单位元素。

di输入Input的Depth，单位元素。

hi输入Input的Height，单位元素。

wi输入Input的Width，单位元素。

dk输出Weight的Depth，单位元素。

hk输出Weight的Height，单位元素。

wk输出Weight的Width，单位元素。

group预留参数，用户无需感知。

strideD卷积反向计算中Stride的Depth，单位元素。

strideH卷积反向计算中Stride的Height，单位元素。

strideW卷积反向计算中Stride的Width，单位元素。

padFront卷积反向计算中Padding的Depth维度的前方向，单位元素。

padBack卷积反向计算中Padding的Depth维度的后方向，单位元素。

padUp卷积反向计算中Padding的Height维度的上方向，单位元素。

padDown卷积反向计算中Padding的Height维度的下方向，单位元素。

padLeft卷积反向计算中Padding的Width维度的左方向，单位元素。

padRight卷积反向计算中Padding的Width维度的右方向，单位元素。

dilationD卷积反向计算中Dilation的Depth，单位元素。

dilationH卷积反向计算中Dilation的Height，单位元素。

dilationW卷积反向计算中Dilation的Width，单位元素。

channelSize

当前输入数据类型下C0的大小。该参数目前只支持取值为16。

al0Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

<!-- page 3069 -->

参数名称说明

bl0Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

cl0Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

al1Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

bl1Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

baseML0上M方向大小，单位元素。

baseKL0上K方向大小，单位元素。

baseNL0上N方向大小，单位元素。

m0L0上最小分形M方向大小。

k0L0上最小分形K方向大小。

n0L0上最小分形N方向大小。

stepM矩阵在L1中缓存的buffer M方向上baseM的倍数。

stepN矩阵在L1中缓存的buffer N方向上baseN的倍数。

stepKa矩阵在L1中缓存的buffer K方向上baseK的倍数。

stepKb矩阵在L1中缓存的buffer K方向上baseK的倍数。

iterateOrder

预留参数，用户无需感知。

bl1BoundL1中载入GradOutput矩阵的最大数据量。

hf32Flag预留参数，用户无需感知。

singleCoreDK

预留参数，用户无需感知。

singleCoreGroup

预留参数，用户无需感知。

singleCoreCout

单核M方向上计算cout数据量的大小，单位元素。

singleCoreHo

单核K方向上计算ho数据量的大小，单位元素。

singleCoreBatch

单核上batch的大小，单位元素。

singleCoreCin

单核N方向上计算cin数据量的大小，单位元素。

totalL1SizeL1 size大小，单位元素。

singleCoreM

单核上M的大小，单位元素。
