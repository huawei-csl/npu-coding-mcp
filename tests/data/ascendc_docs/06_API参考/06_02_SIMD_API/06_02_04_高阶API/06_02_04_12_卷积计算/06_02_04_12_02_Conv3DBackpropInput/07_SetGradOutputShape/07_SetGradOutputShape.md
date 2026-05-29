# SetGradOutputShape

> **Section**: 7  
> **PDF Pages**: 3046–3046  

---

<!-- page 3046 -->

参数说明

表6-1410参数说明

参数名输入/输出

描述

n输入输入Input的Batch值。

c输入输入Input的Channel值。

d输入输入Input的Depth值。

h输入输入Input的Height值。

w输入输入Input的Width值。

返回值说明

true表示设置成功，false表示设置失败。

约束说明

无

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3DBpInputTiling conv3DBpDxTiling(*ascendcPlatform);conv3DBpDxTiling.SetInputShape(n, c, d, h, w);
```

## ?.7. SetGradOutputShape

功能说明

设置GradOutput的形状：Batch、Channel、Depth、Height、Width。

函数原型

```cpp
bool SetGradOutputShape(int64_t n, int64_t c, int64_t d, int64_t h, int64_t w)
```

参数说明

表6-1411参数说明

参数名输入/输出

描述

n输入输入GradOutput的Batch值。

c输入输入GradOutput的Channel值。

d输入输入GradOutput的Depth值。
