# ReleaseMutexID (ISASI)

> **Section**: 6.2.3.7.1.8  
> **PDF Pages**: 1836–1836  

---

<!-- page 1836 -->

## 6.2.3.7.1.8 ReleaseMutexID (ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

从框架释放一个MutexID，与AllocMutexID配合使用。

函数原型

```cpp
__aicore__ inline void ReleaseMutexID(MutexID id)
```

参数说明

表6-733参数说明

参数名输入/输出

描述

id输入MutexID类型，应传入调用AllocMutexID获得的MutexID。

返回值说明

无

约束说明

无

调用示例

请参考调用示例。

## 6.2.3.7.2 核间同步

