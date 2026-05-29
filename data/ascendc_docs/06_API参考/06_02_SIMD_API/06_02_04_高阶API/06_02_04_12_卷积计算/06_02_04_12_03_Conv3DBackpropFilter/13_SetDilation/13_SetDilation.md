# SetDilation

> **Section**: 13  
> **PDF Pages**: 3077–3077  

---

<!-- page 3077 -->

函数原型

```cpp
void SetStride(int64_t strideD, int64_t strideH, int64_t strideW)
```

参数说明

表6-1439参数说明

参数名输入/输出

描述

strideD输入卷积正向过程中Depth方向Stride的大小。

strideH输入卷积正向过程中Height方向Stride的大小。

strideW输入卷积正向过程中Width方向Stride的大小。

返回值说明

无

约束说明

无

调用示例

```cpp
optiling::Conv3DBackpropFilterTilingData tilingData;auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3dBpFilterTiling conv3dBpDwTiling(*ascendcPlatform);conv3dBpDwTiling.SetStride(strideD, strideH, strideW);
```

## ?.13. SetDilation

功能说明

设置Dilation信息，即卷积核Depth/Height/Width方向的扩张大小。

函数原型

```cpp
void SetDilation(int64_t dilationD, int64_t dilationH, int64_t dilationW)
```

参数说明

表6-1440参数说明

参数名输入/输出

描述

dilationD输入卷积核Weight的Depth方向扩张大小。

dilationH输入卷积核Weight的Height方向扩张大小。

dilationW输入卷积核Weight的Width方向扩张大小。
