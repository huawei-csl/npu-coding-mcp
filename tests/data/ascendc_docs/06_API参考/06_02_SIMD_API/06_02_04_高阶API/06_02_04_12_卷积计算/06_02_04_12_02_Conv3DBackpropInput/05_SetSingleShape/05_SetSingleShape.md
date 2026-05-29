# SetSingleShape

> **Section**: 5  
> **PDF Pages**: 3033–3033  

---

<!-- page 3033 -->

调用示例

const Conv3DBackpropInputTilingData* tilingData;// ...初始化tilingDataConvBackpropApi::Conv3DBackpropInput<weightDxType, inputSizeDxType, gradOutputDxType, gradInputDxType> gradInput_;// ...设置其它参数gradInput_.SetWeight(weightGm_[offsetB_]);

## ?.5. SetSingleShape

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

设置Conv3DBackpropInput在单核上计算的形状，单位为元素个数。

函数原型

```cpp
__aicore__ inline void SetSingleShape(uint64_t singleShapeM, uint64_t singleShapeK, uint32_t singleShapeN)
```

参数说明

表6-1402接口参数说明

参数名输入/输出

描述

singleShapeM

输入单核上M的大小，单位为元素。

singleShapeK

输入单核上K的大小，单位为元素。

singleShapeN

输入单核上N的大小，单位为元素。
