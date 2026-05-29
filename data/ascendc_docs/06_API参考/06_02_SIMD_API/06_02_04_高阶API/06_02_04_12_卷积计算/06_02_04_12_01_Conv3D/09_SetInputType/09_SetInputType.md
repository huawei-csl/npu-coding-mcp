# SetInputType

> **Section**: 9  
> **PDF Pages**: 3020–3020  

---

<!-- page 3020 -->

函数原型

```cpp
void SetSingleOutputShape(int64_t singleCo, int64_t singleDo, int64_t singleM)
```

参数说明

参数名输入/输出描述

singleCo输入单核上输出通道的大小。

singleDo输入单核上Output D维度大小。

singleM输入单核上Output M维度大小。

返回值说明

无

约束说明

无

调用示例

// 实例化Conv3D Apiauto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());Conv3dTilingApi::Conv3dTiling conv3dApiTiling(ascendcPlatform);conv3dApiTiling.SetSingleOutputShape(singleCo, singleDo, singleM);

## ?.9. SetInputType

功能说明

设置Input在内存上的位置、数据格式和数据类型。

函数原型

```cpp
void SetInputType(const ConvCommonApi::TPosition pos, const ConvCommonApi::ConvFormat format, const ConvCommonApi::ConvDtype dtype)
```

参数说明

参数名输入/输出描述

pos输入Input在内存上的位置。当前仅支持TPosition::GM。

format输入Input的数据格式。当前仅支持ConvFormat::NDC1HWC0。

dtype输入Input的数据类型。当前仅支持ConvDtype::FLOAT16、ConvDtype::BF16。
