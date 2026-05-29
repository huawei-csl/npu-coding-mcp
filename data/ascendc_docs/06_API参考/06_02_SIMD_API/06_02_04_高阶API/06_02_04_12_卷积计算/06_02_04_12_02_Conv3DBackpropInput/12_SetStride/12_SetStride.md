# SetStride

> **Section**: 12  
> **PDF Pages**: 3050–3050  

---

<!-- page 3050 -->

参数说明

表6-1415参数说明

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
auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3DBpInputTiling conv3DBpDxTiling(*ascendcPlatform);conv3DBpDxTiling.SetPadding(padFront, padBack, padUp, padDown, padLeft, padRight);
```

## ?.12. SetStride

功能说明

设置Stride信息。

函数原型

```cpp
void SetStride(int64_t strideD, int64_t strideH, int64_t strideW)
```

参数说明

表6-1416参数说明

参数名输入/输出

描述

strideD输入卷积正向过程中Depth方向Stride的大小。

strideH输入卷积正向过程中Height方向Stride的大小。
