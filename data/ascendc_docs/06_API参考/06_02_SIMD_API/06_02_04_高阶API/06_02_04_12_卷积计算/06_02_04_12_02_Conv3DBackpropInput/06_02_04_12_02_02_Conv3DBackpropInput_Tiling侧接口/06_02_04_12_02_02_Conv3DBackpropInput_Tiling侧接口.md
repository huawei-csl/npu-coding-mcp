# Conv3DBackpropInput Tiling侧接口

> **Section**: 6.2.4.12.2.2  
> **PDF Pages**: 3038–3038  

---

<!-- page 3038 -->

产品是否支持

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

在Conv3DBackpropInput卷积反向计算完成后，必须调用一次End，以清除EventID并释放内部申请的临时内存。

函数原型

```cpp
__aicore__ inline void End()
```

参数说明

无

返回值说明

无

约束说明

End接口必须在Iterate和GetTensorC接口后调用。

调用示例

const Conv3DBackpropInputTilingData* tilingData;// ...初始化tilingDataConvBackpropApi::Conv3DBackpropInput<weightDxType, inputSizeDxType, gradOutputDxType, gradInputDxType> gradInput_;// ...其它调用gradInput_.End();

## 6.2.4.12.2.2 Conv3DBackpropInput Tiling 侧接口

## ?.1. Conv3DBackpropInput Tiling 使用说明

Ascend C提供一组Conv3DBackpropInput Tiling API，方便用户获取Conv3DBackpropInput Kernel计算时所需的Tiling参数。用户只需要传入Input/GradOutput/Weight的Position位置、Format格式和DType数据类型及相关参数等信息，调用API接口，即可获取Init中TConv3DBackpropInputTiling结构体中的相关参数。

Conv3DBackpropInput Tiling API提供一个GetTiling接口获取Tiling参数，获取Tiling参数的流程如下：
