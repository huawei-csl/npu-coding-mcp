# SetInput

> **Section**: 3  
> **PDF Pages**: 3057–3057  

---

<!-- page 3057 -->

约束说明

Init接口必须在Iterate、GetTensorC、End接口前调用，且只能调用一次Init接口，调用顺序如下。Init(...);...Iterate(...);GetTensorC(...);End();

调用示例

const Conv3DBackpropFilterTilingData* tilingData;// ...初始化tilingData，创建Conv3DBackpropFilter对象，调用init接口ConvBackpropApi::Conv3DBackpropFilter <inputType, weightSizeType, gradOutputType, gradWeightType > gradWeight_;gradWeight_.Init(&(tilingData->dwTiling));

## ?.3. SetInput

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

设置特征矩阵Input。

函数原型

```cpp
__aicore__ inline void SetInput(const AscendC::GlobalTensor<SrcT> &input)
```
