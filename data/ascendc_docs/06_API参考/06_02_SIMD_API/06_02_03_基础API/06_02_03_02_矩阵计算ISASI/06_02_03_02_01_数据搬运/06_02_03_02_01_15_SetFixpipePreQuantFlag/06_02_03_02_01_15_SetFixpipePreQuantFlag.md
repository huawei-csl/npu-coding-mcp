# SetFixpipePreQuantFlag

> **Section**: 6.2.3.2.1.15  
> **PDF Pages**: 1059–1059  

---

<!-- page 1059 -->

## 6.2.3.2.1.15 SetFixpipePreQuantFlag

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

**DataCopy（CO1->GM、CO1->A1）过程中进行随路量化时，通过调用该接口设置量化流程中标量量化参数。**

函数原型

```cpp
template<template T>__aicore__ inline void SetFixpipePreQuantFlag(uint64_t config)
```

参数说明

表6-202参数说明

参数名称输入/输出

含义

config输入量化过程中使用到的标量量化参数。

返回值说明

无

约束说明

无

调用示例

完整示例可参考完整示例。

float tmp = (float)0.5;// 将float的tmp转换成uint64_t的deqScalar
