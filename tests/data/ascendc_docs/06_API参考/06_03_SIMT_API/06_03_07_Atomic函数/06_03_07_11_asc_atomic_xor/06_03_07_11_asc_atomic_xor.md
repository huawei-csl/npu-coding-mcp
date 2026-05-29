# asc_atomic_xor

> **Section**: 6.3.7.11  
> **PDF Pages**: 3319–3319  

---

<!-- page 3319 -->

## 6.3.7.11 asc_atomic_xor

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

对Unified Buffer或Global Memory上address的数值与指定数值val进行原子异或（^）操作，即将address数值异或（^）val的结果赋值到Unified Buffer或Global Memory上。

函数原型

```cpp
inline int32_t asc_atomic_xor(int32_t *address, int32_t val)inline uint32_t asc_atomic_xor(uint32_t *address, uint32_t val)inline int64_t asc_atomic_xor(int64_t *address, int64_t val)inline uint64_t asc_atomic_xor(uint64_t *address, uint64_t val)
```

参数说明

表6-1619参数说明

参数名输入/输出

描述

address输出Unified Buffer或Global Memory的地址。

val输入源操作数。

不同数据类型支持的内存范围说明如下：

表6-1620不同数据类型支持的内存范围

参数数据类型支持的内存空间

int32_t、uint32_tUnified Buffer、Global Memory
