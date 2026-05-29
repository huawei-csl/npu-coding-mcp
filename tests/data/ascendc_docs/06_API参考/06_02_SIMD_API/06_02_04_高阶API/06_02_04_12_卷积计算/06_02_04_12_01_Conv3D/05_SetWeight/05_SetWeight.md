# SetWeight

> **Section**: 5  
> **PDF Pages**: 3005–3005  

---

<!-- page 3005 -->

## ?.5. SetWeight

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

设置权重矩阵Weight。

函数原型

```cpp
__aicore__ inline void SetWeight(const AscendC::GlobalTensor<WeightT>& weight)
```

参数说明

参数名输入/输出描述

weight输入Weight在Global Memory上的地址。类型为GlobalTensor。权重矩阵Weight支持的数据类型为：half、bfloat16_t。

返回值说明

无

约束说明

无

调用示例

```cpp
GlobalTensor<half> weightGm;weightGm.SetGlobalBuffer(reinterpret_cast<__gm__ half *>(weight));conv3dApi.SetWeight(weightGm);
```
