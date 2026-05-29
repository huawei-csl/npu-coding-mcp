# SetDilation

> **Section**: 14  
> **PDF Pages**: 3024–3024  

---

<!-- page 3024 -->

参数名输入/输出描述

padRight输入W方向右Padding大小。

返回值说明

无

约束说明

在调用GetTiling接口前，本接口可选调用。若未调用本接口，默认padHead=0,padTail=0, padUp=0, padDown=0, padLeft=0, padRight=0。

调用示例

// 实例化Conv3D Apiauto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());Conv3dTilingApi::Conv3dTiling conv3dApiTiling(ascendcPlatform);conv3dApiTiling.SetPadding(padHead, padTail, padUp, padDown, padLeft, padRight);

## ?.14. SetDilation

功能说明

设置Dilation信息。

函数原型

```cpp
void SetDilation(int64_t dilationD, int64_t dilationH, int64_t dilationW)
```

参数说明

参数名输入/输出描述

dilationD输入D方向Dilation大小。

dilationH输入H方向Dilation大小。

dilationW输入W方向Dilation大小。

返回值说明

无

约束说明

在调用GetTiling接口前，本接口可选调用。若未调用本接口，默认dilationD=1,dilationH=1, dilationW=1。

调用示例

// 实例化Conv3D Apiauto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
