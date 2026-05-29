# GetTensorC

> **Section**: 8  
> **PDF Pages**: 3063–3063  

---

<!-- page 3063 -->

●在多轮循环计算的场景中，在单次循环里计算单核SetSingleShape设置的数据大小。每次单核计算完成后，必须将Conv3DBackpropFilter对象的ctx.isFirstIter_设置为true，以确保下一轮循环中的单核计算能够正确进行。

调用示例

while (gradWeight_.Iterate()) {    gradWeight_.GetTensorC(output);}// SingleShape计算完成后，需要将ctx.isFirstIter_设置为true，确保下一块SingleShape的正确计算gradWeight_.ctx.isFirstIter_ = true;

## ?.8. GetTensorC

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

在完成Iterate操作后调用本接口，获取结果矩阵块，完成数据从L0C到GM的搬运。此接口与Iterate接口配合使用，用于在Iterate执行迭代计算后，获取结果矩阵。

函数原型

```cpp
template <bool sync = true>__aicore__ inline void GetTensorC(const AscendC::GlobalTensor<DstT> &output, uint8_t enAtomic = 1, bool enSequentialWrite = false)
```

参数说明

表6-1427模板参数说明

参数名描述

sync预留参数，用户无需感知。
