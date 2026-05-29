# LocalMemAllocator简介

> **Section**: 1  
> **PDF Pages**: 1816–1816  

---

<!-- page 1816 -->

## ?.1. LocalMemAllocator 简介

LocalMemAllocator是在使用静态Tensor编程方式时用于内存管理的类，用户无需构建TPipe/TQue，而是直接创建LocalTensor对象（也可以直接通过LocalTensor构造函数进行构造）并开发算子，从而减少运行时的开销，实现更优的性能。

LocalMemAllocator仅支持在Ascend C静态Tensor编程方式中使用，不可以与TPipe等接口混用。

需要包含的头文件

```cpp
#include "kernel_operator.h"
```

原型定义

```cpp
template<Hardware hard = Hardware::UB>class LocalMemAllocator {public:    __aicore__ inline LocalMemAllocator();
    __aicore__ inline uint32_t GetCurAddr() const;
    template <class DataType, uint32_t tileSize> LocalTensor<DataType> __aicore__ inline Alloc();
    template <TPosition pos, class DataType, uint32_t tileSize> __aicore__ inline LocalTensor<DataType> Alloc();
    template <class DataType> LocalTensor<DataType> __aicore__ inline Alloc(uint32_t tileSize);
        template <TPosition pos, class DataType> LocalTensor<DataType> __aicore__ inline Alloc(uint32_t tileSize);
    template <class DataType> LocalTensor<DataType> __aicore__ inline Alloc();};
```

模板参数

表6-718模板参数说明

参数名描述

hard用于表示数据的物理位置，Hardware枚举类型，定义如下，合法位置为：UB、L1、L0A、L0B、L0C、BIAS、FIXBUF。enum class Hardware : uint8_t { GM,     // Global MemoryUB,     // Unified BufferL1,     // L1 BufferL0A,    // L0A BufferL0B,    // L0B BufferL0C,    // L0C BufferBIAS,   // BiasTable BufferFIXBUF, // Fixpipe BufferMAX };
