# Conv3D Tiling构造函数

> **Section**: 2  
> **PDF Pages**: 3012–3012  

---

<!-- page 3012 -->

使用Conv3D Tiling接口获取Tiling参数的样例如下：// 实例化Conv3D Apiauto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());Conv3dTilingApi::Conv3dTiling conv3dApiTiling(ascendcPlatform);// 设置输入输出原始规格、单核规格、参数等conv3dApiTiling.SetGroups(groups);conv3dApiTiling.SetOrgWeightShape(cout, kd, kh, kw);conv3dApiTiling.SetOrgInputShape(cin, di, hi, wi);conv3dApiTiling.SetPadding(padh, padt, padu, padd, padl, padr);conv3dApiTiling.SetDilation(dilationH, dilationW, dilationD);conv3dApiTiling.SetStride(strideH, strideW, strideD);conv3dApiTiling.SetSingleWeightShape(cin, kd, kh, kw);conv3dApiTiling.SetSingleOutputShape(singleCoreCo, singleCoreDo, singleCoreMo);// 设置输入输出typeconv3dApiTiling.SetInputType(TPosition::GM, inputFormat, inputDtype);conv3dApiTiling.SetWeightType(TPosition::GM, weightFormat, weightDtype);conv3dApiTiling.SetOutputType(TPosition::CO1, outputFormat, outputDtype);if (biasFlag) {   conv3dApiTiling.SetBiasType(TPosition::GM, biasFormat, biasDtype);}// 调用GetTiling接口获取核内切分策略，如果返回-1代表获取tiling失败if (conv3dApiTiling.GetTiling(tilingData.conv3dApiTilingData) == -1) {   return false;}

需要包含的头文件

```cpp
#include "lib/conv/conv3d/conv3d_tiling.h"
```

## ?.2. Conv3D Tiling 构造函数

功能说明

用于创建一个Conv3D单核Tiling对象。

函数原型

●带参构造函数，需要传入硬件平台信息，推荐使用这类构造函数来获得更好的兼容性。

–使用PlatformAscendC类传入信息explicit Conv3dTiling(const platform_ascendc::PlatformAscendC& ascendcPlatform)

–使用PlatformInfo传入信息

当platform_ascendc::PlatformAscendC无法在Tiling运行时获取时，需要用户自己构造PlatformInfo结构体，透传给Conv3dTiling构造函数。explicit Conv3dTiling(const PlatformInfo& platform)

●基类构造函数

Conv3dTiling继承自基类Conv3dTilingBase，其构造函数如下：explicit Conv3dTilingBase(const platform_ascendc::PlatformAscendC& ascendcPlatform)explicit Conv3dTilingBase(const PlatformInfo& platform)
