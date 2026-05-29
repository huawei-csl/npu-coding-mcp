# SetGradOutputType

> **Section**: 10  
> **PDF Pages**: 3075–3075  

---

<!-- page 3075 -->

返回值说明

无

约束说明

无

调用示例

```cpp
optiling::Conv3DBackpropFilterTilingData tilingData;auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3dBpFilterTiling conv3dBpDwTiling(*ascendcPlatform);conv3dBpDwTiling.SetInputType(ConvCommonApi::TPosition::GM,                                 ConvCommonApi::ConvFormat::NDC1HWC0,                                 ConvCommonApi::ConvDtype::FLOAT16);
```

## ?.10. SetGradOutputType

功能说明

设置GradOutput的位置、数据格式、数据类型信息，这些信息必须与Kernel侧的设置保持一致。

函数原型

```cpp
void SetGradOutputType(ConvCommonApi::TPosition pos, ConvCommonApi::ConvFormat format, ConvCommonApi::ConvDtype dtype)
```

参数说明

表6-1437参数说明

参数名输入/输出

描述

pos输入GradOutput在内存上的位置。当前仅支持TPosition::GM。

format输入GradOutput的数据格式。当前仅支持ConvFormat::NDC1HWC0。

dtype输入GradOutput的数据类型。当前仅支持ConvDtype::FLOAT16、ConvDtype::BF16。

返回值说明

无

约束说明

无

调用示例

```cpp
optiling::Conv3DBackpropFilterTilingData tilingData;auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();
```
