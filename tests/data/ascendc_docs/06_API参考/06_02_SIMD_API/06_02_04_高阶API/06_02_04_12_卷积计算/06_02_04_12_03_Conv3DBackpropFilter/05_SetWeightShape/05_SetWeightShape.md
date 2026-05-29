# SetWeightShape

> **Section**: 5  
> **PDF Pages**: 3071–3071  

---

<!-- page 3071 -->

ConvCommonApi::ConvFormat::NDC1HWC0,                                   ConvCommonApi::ConvDtype::FLOAT16);conv3dBpDwTiling.SetInputShape(n, c, d, h, w);conv3dBpDwTiling.SetGradOutputShape(n, c, d, h, w);conv3dBpDwTiling.SetWeightShape(cout, cin, d, h, w);conv3dBpDwTiling.SetPadding(padFront, padBack, padUp, padDown, padLeft, padRight);conv3dBpDwTiling.SetStride(strideD, strideH, strideW);conv3dBpDwTiling.SetDilation(dilationD, dilationH, dilationW);int ret = conv3dBpDwTiling.GetTiling(tilingData);    // 获取tiling参数// 使用AscendC::tiling命名空间中的Tiling结构体获取tiling参数AscendC::tiling::Conv3DBackpropFilterTilingData tilingDataNotOp;ret = conv3dBpDwTiling.GetTiling(tilingDataNotOp);

## ?.5. SetWeightShape

功能说明

设置权重矩阵Weight的形状。

函数原型

```cpp
void SetWeightShape(int64_t cout, int64_t cin, int64_t d, int64_t h, int64_t w)
```

参数说明

表6-1432参数说明

参数名输入/输出

描述

cout输入设置GradOutput的Channel值。

cin输入设置Input的Channel值。

d输入设置Weight的Depth值。

h输入设置Weight的Height值。

w输入设置Weight的Width值。

返回值说明

无

约束说明

无

调用示例

```cpp
optiling::Conv3DBackpropFilterTilingData tilingData;auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();ConvBackpropApi::Conv3dBpFilterTiling conv3dBpDwTiling(*ascendcPlatform);conv3dBpDwTiling.SetWeightShape(cout, cin, d, h, w);
```
