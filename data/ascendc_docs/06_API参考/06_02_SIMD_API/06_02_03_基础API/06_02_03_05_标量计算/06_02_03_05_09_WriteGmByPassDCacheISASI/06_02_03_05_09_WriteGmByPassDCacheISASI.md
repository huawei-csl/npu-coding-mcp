# WriteGmByPassDCache(ISASI)

> **Section**: 6.2.3.5.9  
> **PDF Pages**: 1731–1731  

---

<!-- page 1731 -->

## 6.2.3.5.9 WriteGmByPassDCache(ISASI)

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

不经过DCache向GM地址上写数据。

当多核操作GM地址时，如果数据无法对齐到Cache Line，经过DCache的方式下，由于按照Cache Line大小进行读写，会导致多核数据随机覆盖的问题。此时，可以采用不经过DCache直接读写GM地址的方式，从而避免上述随机覆盖的问题。

函数原型

```cpp
template <typename T>__aicore__ inline void WriteGmByPassDCache(__gm__ T* addr, T value)
```

参数说明

表6-656模板参数说明

参数名描述

T操作数的数据类型。

Atlas 350 加速卡，支持的数据类型为：int8_t、uint8_t、int16_t、uint16_t、int32_t、uint32_t、int64_t、uint64_t。

表6-657接口参数说明

参数名输入/输出

含义

addr输入目标GM地址。

value输入待写入目标数据。
