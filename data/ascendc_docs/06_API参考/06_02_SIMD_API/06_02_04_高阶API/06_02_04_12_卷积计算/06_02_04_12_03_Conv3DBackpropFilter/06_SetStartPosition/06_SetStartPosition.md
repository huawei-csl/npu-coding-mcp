# SetStartPosition

> **Section**: 6  
> **PDF Pages**: 3060–3060  

---

<!-- page 3060 -->

功能说明

设置Conv3DBackpropFilter在单核上计算的形状。用于运行时修改shape。

函数原型

```cpp
__aicore__ inline void SetSingleShape(uint64_t singleCoreM, uint64_t singleCoreN, uint64_t singleCoreK)
```

参数说明

表6-1424接口参数说明

参数名输入/输出

描述

singleCoreM输入单核上M的大小，单位为元素个数。

singleCoreN输入单核上N的大小，单位为元素个数。

singleCoreK输入单核上K的大小，单位为元素个数。

返回值说明

无

约束说明

无

调用示例

const Conv3DBackpropFilterTilingData* tilingData;// ...初始化tilingDataConvBackpropApi::Conv3DBackpropFilter <inputType, weightSizeType, gradOutputType, gradWeightType > gradWeight_;....gradWeight_.Init(&(tilingData->dwTiling));gradWeight_.SetInput(inputGm_[offsetB_]);gradWeight_.SetGradOutput(gradOutputGm_[offsetA_]);gradWeight_.SetSingleShape(singleCoreM, singleCoreN, singleCoreK);// 设置单核计算量....

## ?.6. SetStartPosition

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x
