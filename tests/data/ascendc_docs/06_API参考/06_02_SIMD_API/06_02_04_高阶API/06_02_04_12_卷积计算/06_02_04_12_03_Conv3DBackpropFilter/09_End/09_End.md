# End

> **Section**: 9  
> **PDF Pages**: 3064–3064  

---

<!-- page 3064 -->

表6-1428接口参数说明

参数名输入/输出

描述

output输入将计算结果搬至Global Memory的GM地址。

enAtomic输入预留参数，用户无需感知。

enSequentialWrite

输入预留参数，用户无需感知。

返回值说明

无

约束说明

GetTensorC接口必须在Iterate后进行调用，完成卷积反向实现，调用顺序如下。while (Iterate()) {       GetTensorC(); }

调用示例

```cpp
while (gradWeight_.Iterate()) {    gradWeight_.GetTensorC(gradWeightGm_[offsetC_]);}
```

## ?.9. End

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

在Conv3DBackpropFilter卷积反向计算完成后，必须调用一次End，以清除EventID并释放内部申请的临时内存。
