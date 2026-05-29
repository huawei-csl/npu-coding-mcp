# SetStartPosition

> **Section**: 6  
> **PDF Pages**: 3034–3034  

---

<!-- page 3034 -->

返回值说明

无

约束说明

无

调用示例

const Conv3DBackpropInputTilingData* tilingData;// ...初始化tilingDataConvBackpropApi::Conv3DBackpropInput<weightDxType, inputSizeDxType, gradOutputDxType, gradInputDxType> gradInput_;// ...设置其它参数gradInput_.SetSingleShape(singleShapeM_, singleShapeK_, singleShapeN_); // 设置单核计算的形状

## ?.6. SetStartPosition

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

设置单核上GradOutput载入数据的起始位置。

函数原型

```cpp
__aicore__ inline void SetStartPosition(uint32_t curDinStartIdx, int32_t curHoStartIdx)
```

参数说明

参数名输入/输出描述

curDinStartIdx

输入当前核D方向起始位置。

curHoStartIdx

输入当前核H方向起始位置。
