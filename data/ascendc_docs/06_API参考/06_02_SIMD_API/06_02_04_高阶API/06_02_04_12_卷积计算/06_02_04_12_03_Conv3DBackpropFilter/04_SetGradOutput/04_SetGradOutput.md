# SetGradOutput

> **Section**: 4  
> **PDF Pages**: 3058–3058  

---

<!-- page 3058 -->

参数说明

表6-1422接口参数说明

参数名输入/输出

描述

input输入Input在Global Memory上的首地址。类型为GlobalTensor。特征矩阵Input支持的数据类型SrcT为：half、bfloat16_t。

返回值说明

无

约束说明

无

调用示例

const Conv3DBackpropFilterTilingData* tilingData;// ...初始化tilingDataConvBackpropApi::Conv3DBackpropFilter <inputType, weightSizeType, gradOutputType, gradWeightType > gradWeight_;gradWeight_.Init(&(tilingData->dwTiling));// 设置InputgradWeight_.SetInput(inputGm_[offsetB_]);...

## ?.4. SetGradOutput

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

设置卷积反向计算的输入矩阵GradOutput。
