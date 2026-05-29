# SetOutputPadding

> **Section**: 14  
> **PDF Pages**: 3052–3052  

---

<!-- page 3052 -->

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3DBpInputTiling conv3DBpDxTiling(*ascendcPlatform);conv3DBpDxTiling.SetDilation(dilationD, dilationH, dilationW);
```

## ?.14. SetOutputPadding

功能说明

构建Conv3DTranspose算子时，设置输出的Padding大小，用于推导输出的形状。在构建Conv3DBackpropInput算子时，此接口无实际意义，请勿使用。

函数原型

```cpp
bool SetOutputPadding(int64_t outputPadD, int64_t outputPadH, int64_t outputPadW)
```

参数说明

表6-1418参数说明

参数名输入/输出描述

outputPadD输入输出在Depth方向的Padding值。

outputPadH输入输出在Height方向的Padding值。

outputPadW输入输出在Width方向的Padding值。

返回值说明

true表示设置成功，false表示设置失败。

约束说明

无

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3DBpInputTiling conv3DBpDxTiling(*ascendcPlatform);conv3DBpDxTiling.SetOutputPadding(outputPadD, outputPadH, outputPadW);
```

## 6.2.4.12.3 Conv3DBackpropFilter

## 6.2.4.12.3.1 Conv3DBackpropFilter Kernel 侧接口

