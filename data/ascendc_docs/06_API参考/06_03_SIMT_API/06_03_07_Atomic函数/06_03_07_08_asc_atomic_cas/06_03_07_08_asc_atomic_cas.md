# asc_atomic_cas

> **Section**: 6.3.7.8  
> **PDF Pages**: 3314–3314  

---

<!-- page 3314 -->

## 6.3.7.8 asc_atomic_cas

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

对Unified Buffer或Global Memory上address的数值进行原子比较赋值操作，如果address上的数值等于指定数值compare，则对address赋值为指定数值val，否则address的数值不变。

函数原型

```cpp
inline float asc_atomic_cas(float *address, float compare, float val)inline int32_t asc_atomic_cas(int32_t *address, int32_t compare, int32_t val)inline uint32_t asc_atomic_cas(uint32_t *address, uint32_t compare, uint32_t val)inline int64_t asc_atomic_cas(int64_t *address, int64_t compare, int64_t val)inline uint64_t asc_atomic_cas(uint64_t *address, uint64_t compare, uint64_t val)inline half2 asc_atomic_cas(half2 *address, half2 compare, half2 val)inline bfloat16x2_t asc_atomic_cas(bfloat16x2_t *address, bfloat16x2_t compare, bfloat16x2_t val)
```

参数说明

表6-1613参数说明

参数名输入/输出

描述

address输出Unified Buffer或Global Memory的地址。

compare输入源操作数，做比较的值。

val输入源操作数，用于赋值的值。

不同数据类型支持的内存范围说明如下：
