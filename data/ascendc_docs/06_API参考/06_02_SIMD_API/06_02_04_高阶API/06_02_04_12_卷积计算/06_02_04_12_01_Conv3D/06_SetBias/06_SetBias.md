# SetBias

> **Section**: 6  
> **PDF Pages**: 3006–3006  

---

<!-- page 3006 -->

## ?.6. SetBias

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

设置偏置矩阵Bias。

函数原型

```cpp
__aicore__ inline void SetBias(const AscendC::GlobalTensor<BiasT>& bias)
```

参数说明

参数名输入/输出描述

bias输入Bias在Global Memory上的地址。类型为GlobalTensor。偏置矩阵Bias支持的数据类型为：half、bfloat16_t。

返回值说明

无

约束说明

在卷积计算中，如果涉及偏置矩阵Bias，必须调用此接口；若卷积计算不涉及Bias，则不应调用此接口。

调用示例

```cpp
GlobalTensor<float> biasGm;biasGm.SetGlobalBuffer(reinterpret_cast<__gm__ half *>(bias));if (biasFlag) {    conv3dApi.SetBias(biasGm);}
```
