# LocalMemAllocator构造函数

> **Section**: 2  
> **PDF Pages**: 1817–1817  

---

<!-- page 1817 -->

## ?.2. LocalMemAllocator 构造函数

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品x

功能说明

LocalMemAllocator构造函数。

函数原型

```cpp
template <Hardware hard>__aicore__ inline LocalMemAllocator<hard>::LocalMemAllocator()
```

参数说明

表6-719模板参数说明

参数名描述

hard用于表示数据的物理位置，Hardware枚举类型，定义如下，合法位置为：UB、L1、L0A、L0B、L0C、BIAS、FIXBUF。enum class Hardware : uint8_t { GM,     // Global MemoryUB,     // Unified BufferL1,     // L1 BufferL0A,    // L0A BufferL0B,    // L0B BufferL0C,    // L0C BufferBIAS,   // BiasTable BufferFIXBUF, // Fixpipe BufferMAX };

返回值说明

无
