# SetAtomicMax(ISASI)

> **Section**: 6.2.3.10.4  
> **PDF Pages**: 1885–1885  

---

<!-- page 1885 -->

## 6.2.3.10.4 SetAtomicMax(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

原子操作函数，设置后续从VECOUT传输到GM的数据是否执行原子比较：将待拷贝的内容和GM已有内容进行比较，将最大值写入GM。

可通过设置模板参数来设定不同的数据类型。

函数原型

```cpp
template <typename T>__aicore__ inline void SetAtomicMax()
```

参数说明

表6-761模板参数说明

参数名

描述

T设定不同的数据类型。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，支持int8_t/int16_t/half/bfloat16_t/int32_t/float

Atlas A3 训练系列产品/Atlas A3 推理系列产品，支持int8_t/int16_t/half/bfloat16_t/int32_t/float

Atlas 350 加速卡，支持int8_t/int16_t/half/bfloat16_t/int32_t/float

返回值说明

无
