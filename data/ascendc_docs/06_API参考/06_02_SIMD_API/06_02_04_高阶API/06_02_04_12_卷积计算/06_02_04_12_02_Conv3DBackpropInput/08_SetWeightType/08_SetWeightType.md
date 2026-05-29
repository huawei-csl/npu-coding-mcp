# SetWeightType

> **Section**: 8  
> **PDF Pages**: 3047–3047  

---

<!-- page 3047 -->

参数名输入/输出

描述

h输入输入GradOutput的Height值。

w输入输入GradOutput的Width值。

返回值说明

true表示设置成功，false表示设置失败。

约束说明

无

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3DBpInputTiling conv3DBpDxTiling(*ascendcPlatform);conv3DBpDxTiling.SetGradOutputShape(n, c, d, h, w);
```

## ?.8. SetWeightType

功能说明

设置权重矩阵Weight的位置、数据格式、数据类型信息，这些信息必须与Kernel侧的设置保持一致。

函数原型

```cpp
void SetWeightType(ConvCommonApi::TPosition pos, ConvCommonApi::ConvFormat format, ConvCommonApi::ConvDtype dtype)
```

参数说明

表6-1412参数说明

参数名输入/输出

描述

pos输入Weight在内存上的位置。当前仅支持TPosition::GM。

format输入Weight的数据格式。当前仅支持ConvFormat::FRACTAL_Z_3D。

dtype输入Weight的数据类型。当前仅支持ConvDtype::FLOAT16或者ConvDtype::BF16。

返回值说明

无
