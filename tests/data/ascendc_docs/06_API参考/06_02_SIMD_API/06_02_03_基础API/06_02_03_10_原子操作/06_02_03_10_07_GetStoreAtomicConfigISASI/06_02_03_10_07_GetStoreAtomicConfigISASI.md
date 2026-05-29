# GetStoreAtomicConfig(ISASI)

> **Section**: 6.2.3.10.7  
> **PDF Pages**: 1889–1889  

---

<!-- page 1889 -->

调用示例

// 设置原子操作为求和操作，支持的数据类型为halfAscendC::SetStoreAtomicConfig<AscendC::AtomicDtype::ATOMIC_F16, AscendC::AtomicOp::ATOMIC_SUM>();

## 6.2.3.10.7 GetStoreAtomicConfig(ISASI)

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

获取原子操作使能位与原子操作类型的值，详细说明见表6-763。

函数原型

```cpp
__aicore__ inline void GetStoreAtomicConfig(uint16_t& atomicType, uint16_t& atomicOp)
```

参数说明

表6-764参数说明

参数名输入/输出

描述

atomicType输出原子操作使能位。

0：无原子操作

1：使能原子操作，进行原子操作的数据类型为float

2：使能原子操作，进行原子操作的数据类型为half

3：使能原子操作，进行原子操作的数据类型为int16_t

4：使能原子操作，进行原子操作的数据类型为int32_t

5：使能原子操作，进行原子操作的数据类型为int8_t

6：使能原子操作，进行原子操作的数据类型为bfloat16_t

atomicOp输出原子操作类型。

0：求和操作
