# SetStride

> **Section**: 15  
> **PDF Pages**: 3025–3025  

---

<!-- page 3025 -->

```cpp
Conv3dTilingApi::Conv3dTiling conv3dApiTiling(ascendcPlatform);conv3dApiTiling.SetDilation(dilationD, dilationH, dilationW);
```

## ?.15. SetStride

功能说明

设置Stride信息。

函数原型

```cpp
void SetStride(int64_t strideD, int64_t strideH, int64_t strideW)
```

参数说明

参数名输入/输出描述

strideD输入D方向Stride大小。

strideH输入H方向Stride大小。

strideW输入W方向Stride大小。

返回值说明

无

约束说明

在调用GetTiling接口前，本接口可选调用。若未调用本接口，默认strideD=1,strideH=1, strideW=1。

调用示例

// 实例化Conv3D Apiauto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());Conv3dTilingApi::Conv3dTiling conv3dApiTiling(ascendcPlatform);conv3dApiTiling.SetStride(strideD, strideH, strideW);

## ?.16. SetGroups

功能说明

设置分组卷积的分组大小。分组大小为1表示普通卷积。当前Conv3D 高阶API不支持分组卷积。

函数原型

```cpp
void SetGroups(int64_t groups)
```
