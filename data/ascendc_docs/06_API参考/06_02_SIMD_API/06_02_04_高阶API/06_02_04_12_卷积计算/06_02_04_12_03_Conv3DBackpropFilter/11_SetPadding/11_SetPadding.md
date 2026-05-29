# SetPadding

> **Section**: 11  
> **PDF Pages**: 3076–3076  

---

<!-- page 3076 -->

```cpp
ConvBackpropApi::Conv3dBpFilterTiling conv3dBpDwTiling(*ascendcPlatform);conv3dBpDwTiling.SetGradOutputType(ConvCommonApi::TPosition::GM,                                   ConvCommonApi::ConvFormat::NDC1HWC0,                                   ConvCommonApi::ConvDtype::FLOAT16);
```

## ?.11. SetPadding

功能说明

设置Pad信息。

函数原型

```cpp
void SetPadding(int64_t padFront, int64_t padBack, int64_t padUp, int64_t padDown, int64_t padLeft, int64_t padRight)
```

参数说明

表6-1438参数说明

参数名输入/输出

描述

padFront输入卷积正向过程中Input Depth维度的前方向Padding大小。

padBack输入卷积正向过程中Input Depth维度的后方向Padding大小。

padUp输入卷积正向过程中Input Height维度的上方向Padding大小。

padDown输入卷积正向过程中Input Height维度的下方向Padding大小。

padLeft输入卷积正向过程中Input Width维度的左方向Padding大小。

padRight输入卷积正向过程中Input Width维度的右方向Padding大小。

返回值说明

无

约束说明

无

调用示例

```cpp
optiling::Conv3DBackpropFilterTilingData tilingData;auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3dBpFilterTiling conv3dBpDwTiling(*ascendcPlatform);conv3dBpDwTiling.SetPadding(padFront, padBack, padUp, padDown, padLeft, padRight);
```

## ?.12. SetStride

功能说明

设置Stride信息。
