# asc_atomic_inc

> **Section**: 6.3.7.6  
> **PDF Pages**: 3311–3311  

---

<!-- page 3311 -->

## 6.3.7.6 asc_atomic_inc

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

对Unified Buffer或Global Memory上address的数值进行原子加1操作，如果address上的数值大于等于指定数值val，则对address赋值为0，否则将address上数值加1。

函数原型

```cpp
inline uint32_t asc_atomic_inc(uint32_t *address, uint32_t val)inline uint64_t asc_atomic_inc(uint64_t *address, uint64_t val)
```

参数说明

表6-1609参数说明

参数名输入/输出描述

address输出Unified Buffer或Global Memory的地址。

val输入源操作数。

不同数据类型支持的内存范围说明如下：

表6-1610不同数据类型支持的内存范围

参数数据类型支持的内存空间

uint32_tUnified Buffer、Global Memory

uint64_tGlobal Memory
