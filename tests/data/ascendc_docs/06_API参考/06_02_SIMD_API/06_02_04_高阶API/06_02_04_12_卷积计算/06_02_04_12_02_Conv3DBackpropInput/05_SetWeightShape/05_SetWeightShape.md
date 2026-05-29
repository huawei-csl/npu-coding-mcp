# SetWeightShape

> **Section**: 5  
> **PDF Pages**: 3045–3045  

---

<!-- page 3045 -->

## ?.5. SetWeightShape

功能说明

设置权重矩阵Weight的形状。

函数原型

```cpp
bool SetWeightShape(int64_t cout, int64_t cin, int64_t d, int64_t h, int64_t w)
```

参数说明

表6-1409参数说明

参数名输入/输出

描述

cout输入设置卷积正向的输出channel大小，与GradOutput的Channel大小一致。

cin输入设置卷积正向的输入channel大小，与GradInput的Channel大小一致。

d输入设置weight的Depth值。

h输入设置weight的Height值。

w输入设置weight的Width值。

返回值说明

true表示设置成功，false表示设置失败。

约束说明

无

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3DBpInputTiling con3dBpDxTiling(*ascendcPlatform);con3dBpDxTiling.SetWeightShape(cout, cin, d, h, w);
```

## ?.6. SetInputShape

功能说明

设置特征矩阵Input的形状：Batch、Channel、Depth、Height、Width。在构建Conv3DTranspose算子时，此接口无实际意义，请勿使用。

函数原型

```cpp
bool SetInputShape(int64_t n, int64_t c, int64_t d, int64_t h, int64_t w)
```
