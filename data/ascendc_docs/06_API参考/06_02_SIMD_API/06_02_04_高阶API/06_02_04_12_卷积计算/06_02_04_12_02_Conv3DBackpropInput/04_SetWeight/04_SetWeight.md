# SetWeight

> **Section**: 4  
> **PDF Pages**: 3032–3032  

---

<!-- page 3032 -->

// 设置GradOutput中GlobalTensor的地址GlobalTensor<gradOutputType> gradOutputGm_;gradOutputGm_.SetGlobalBuffer((__gm__ gradOutputType *)gradOutput);gradInput_.SetGradOutput(gradOutputGm_);

## ?.4. SetWeight

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

设置卷积反向计算的输入矩阵Weight。

函数原型

```cpp
__aicore__ inline void SetWeight(const AscendC::GlobalTensor<SrcT> &weight)
```

参数说明

表6-1401接口参数说明

参数名输入/输出

描述

weight输入Weight矩阵在Global Memory上的首地址。类型为GlobalTensor。SrcT表示Weight矩阵的数据类型，当前支持的数据类型为：half、bfloat16_t。

返回值说明

无

约束说明

无
