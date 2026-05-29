# SetInputType

> **Section**: 9  
> **PDF Pages**: 3074–3074  

---

<!-- page 3074 -->

参数名输入/输出

描述

format输入Weight的数据格式。当前仅支持ConvFormat::FRACTAL_Z_3D。

dtype输入Weight的数据类型。当前仅支持ConvDtype::FLOAT32。

返回值说明

无

约束说明

无

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3dBpFilterTiling conv3dBpDwTiling(*ascendcPlatform);conv3dBpDwTiling.SetWeightType(ConvCommonApi::TPosition::GM,                                   ConvCommonApi::ConvFormat::FRACTAL_Z_3D,                                   ConvCommonApi::ConvDtype::FLOAT32);
```

## ?.9. SetInputType

功能说明

设置特征矩阵Input的位置、数据格式、数据类型信息，这些信息必须与Kernel侧的设置保持一致。

函数原型

```cpp
void SetInputType(ConvCommonApi::TPosition pos, ConvCommonApi::ConvFormat format, ConvCommonApi::ConvDtype dtype)
```

参数说明

表6-1436参数说明

参数名输入/输出

描述

pos输入Input在内存上的位置。当前仅支持TPosition::GM。

format输入Input的数据格式。当前仅支持ConvFormat::NDC1HWC0。

dtype输入Input的数据类型。当前仅支持ConvDtype::FLOAT16、ConvDtype::BF16。
