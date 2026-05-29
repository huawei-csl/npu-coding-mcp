# AsyncGetTensorC

> **Section**: 6.2.4.2.1.43  
> **PDF Pages**: 2396–2396  

---

<!-- page 2396 -->

约束说明

无

## 6.2.4.2.1.43 AsyncGetTensorC

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

获取Iterate接口异步计算的结果矩阵。该接口功能已被GetTensorC覆盖，建议直接使用GetTensorC异步接口。

函数原型

```cpp
__aicore__ inline void AsyncGetTensorC(const LocalTensor<DstT>& c)
```

参数说明

表6-1059参数说明

参数名输入/输出描述

c输出结果矩阵

返回值说明

无

约束说明

当使能MixDualMaster（双主模式）场景时，即模板参数enableMixDualMaster设置为true，不支持使用该接口。
