# Iterate

> **Section**: 7  
> **PDF Pages**: 3061–3062  

---

<!-- page 3061 -->

产品是否支持

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

设置单核上GradOutput载入数据的起始位置。

函数原型

```cpp
__aicore__ inline void SetStartPosition(uint32_t hoStartIdx)
```

参数说明

参数名输入/输出描述

hoStartIdx输入当前核GradOutput Height方向起始位置。

返回值说明

无

约束说明

无

调用示例

...gradWeight_.SetSingleShape(singleShapeM, singleShapeN, singleShapeK);gradWeight_.SetStartPosition(hoStartIdx); // 设置单核上GradOutput载入的起始位置...

## ?.7. Iterate

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

<!-- page 3062 -->

产品是否支持

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

每次调用Iterate时，会计算出一个baseM * baseN的结果矩阵，并将该结果写入L0CBuffer。接口内部会维护迭代进度，每次调用后，矩阵的起始地址将进行偏移。如果传入的数据未对齐存在尾块，则在最后一次迭代中输出尾块的计算结果。本接口需与GetTensorC接口配合使用；在调用本接口后，再调用GetTensorC接口，L0C Buffer中的数据将被写入目标地址。

函数原型

```cpp
template <bool sync = true>__aicore__ inline bool Iterate(bool enPartialSum = false)
```

参数说明

表6-1425模板参数说明

参数名描述

sync预留参数，用户无需感知。

表6-1426接口参数说明

参数名输入/输出

描述

enPartialSum

输入预留参数，用户无需感知。

返回值说明

false：设置的SingleShape上的所有数据已经算完。

true：数据仍在迭代计算中。

约束说明

●Iterate接口必须在初始化接口及输入输出配置接口之后进行调用，完成卷积反向实现，调用顺序如下。Init(...);... // 输入输出配置while (Iterate()) {       GetTensorC(); }End();
