# ReleaseEventID

> **Section**: 8  
> **PDF Pages**: 1742–1742  

---

<!-- page 1742 -->

## ?.8. ReleaseEventID

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

用于释放HardEvent（硬件类型同步事件）的TEventID，通常与AllocEventID搭配使用。

函数原型

```cpp
template <HardEvent evt>__aicore__ inline void ReleaseEventID(TEventID id)
```

参数说明

表6-667模板参数说明

参数名描述

evtHardEvent硬件同步类型。该类型的具体说明请参考 SetFlag/WaitFlag(ISASI)中同步类型的说明。

表6-668参数说明

参数名输入/输出

描述

id输入TEventID类型，调用AllocEventID申请获得的TEventID。

约束说明

AllocEventID、ReleaseEventID需成对出现，ReleaseEventID传入的TEventID需由对应的AllocEventID申请而来。
