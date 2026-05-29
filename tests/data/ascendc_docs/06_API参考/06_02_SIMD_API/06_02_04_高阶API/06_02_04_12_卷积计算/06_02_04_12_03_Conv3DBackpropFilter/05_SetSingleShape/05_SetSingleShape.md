# SetSingleShape

> **Section**: 5  
> **PDF Pages**: 3059–3059  

---

<!-- page 3059 -->

函数原型

```cpp
__aicore__ inline void SetGradOutput(const AscendC::GlobalTensor<SrcT> &gradOutput)
```

参数说明

表6-1423接口参数说明

参数名输入/输出

描述

gradOutput输入GradOutput矩阵在Global Memory上的首地址。类型为GlobalTensor。SrcT表示GradOutput矩阵的数据类型，当前支持的数据类型为：half、bfloat16_t。

返回值说明

无

约束说明

无

调用示例

const Conv3DBackpropFilterTilingData* tilingData;// ...初始化tilingDataConvBackpropApi::Conv3DBackpropFilter <inputType, weightSizeType, gradOutputType, gradWeightType> gradWeight_;gradWeight_.Init(&(tilingData->dwTiling));gradWeight_.SetInput(inputGm_[offsetB_]);// 设置 gradOutputgradWeight_.SetGradOutput(gradOutputGm_[offsetA_]);...

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
