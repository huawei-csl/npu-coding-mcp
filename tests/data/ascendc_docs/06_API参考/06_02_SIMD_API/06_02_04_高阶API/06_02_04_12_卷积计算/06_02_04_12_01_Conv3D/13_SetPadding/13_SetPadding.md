# SetPadding

> **Section**: 13  
> **PDF Pages**: 3023–3023  

---

<!-- page 3023 -->

参数说明

参数名输入/输出描述

pos输入Output在内存上的位置。当前仅支持TPosition::CO1。

format输入Output的数据格式。当前仅支持ConvFormat::NDC1HWC0。

dtype输入Output的数据类型。当前仅支持ConvDtype::FLOAT16、ConvDtype::BF16。

返回值说明

无

约束说明

在调用GetTiling接口前，本接口可选调用。若未调用本接口，默认Bias为pos=TPosition::CO1，format=ConvFormat::NDC1HWC0，dtype=ConvDtype::FLOAT16。

调用示例

// 实例化Conv3D APIauto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());Conv3dTilingApi::Conv3dTiling conv3dApiTiling(ascendcPlatform);conv3dApiTiling.SetOutputType(ConvCommonApi::TPosition::CO1, ConvCommonApi::ConvFormat::NDC1HWC0, ConvCommonApi::ConvDtype::BF16);

## ?.13. SetPadding

功能说明

设置Pad信息。

函数原型

```cpp
void SetPadding(int64_t padHead, int64_t padTail, int64_t padUp, int64_t padDown, int64_t padLeft, int64_t padRight)
```

参数说明

参数名输入/输出描述

padHead输入D方向前Padding大小。

padTail输入D方向后Padding大小。

padUp输入H方向上Padding大小。

padDown输入H方向下Padding大小。

padLeft输入W方向左Padding大小。
