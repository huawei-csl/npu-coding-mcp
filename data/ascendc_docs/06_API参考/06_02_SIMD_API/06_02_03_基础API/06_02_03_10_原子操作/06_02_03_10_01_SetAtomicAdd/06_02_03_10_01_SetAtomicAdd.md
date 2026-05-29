# SetAtomicAdd

> **Section**: 6.2.3.10.1  
> **PDF Pages**: 1880–1881  

---

<!-- page 1880 -->

参数说明

表6-758模板参数说明

参数名描述

startBit起始比特位索引。

endBit终止比特位索引。

返回值说明

无

约束说明

仅支持CTRL[8:6]、CTRL[10:9]、CTRL[48]、CTRL[50]、CTRL[53]、CTRL[59]、CTRL[60]比特位。

调用示例

如下示例中重置CTRL[8:6]比特位，不使能原子操作。

```cpp
AscendC::SetCtrlSpr<6, 8>(1);...AscendC::ResetCtrlSpr<6, 8>();
```

## 6.2.3.10 原子操作

## 6.2.3.10.1 SetAtomicAdd

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

<!-- page 1881 -->

功能说明

调用该接口后，可对后续的从VECOUT/L0C/L1到GM的数据传输开启原子累加，通过模板参数设定不同的累加数据类型。

函数原型

```cpp
template <typename T>__aicore__ inline void SetAtomicAdd()
```

参数说明

表6-759模板参数说明

参数名

描述

T设定不同的累加数据类型。

Atlas 训练系列产品，支持的数据类型为：float；支持的数据通路为VECOUT->GM。

Atlas 推理系列产品AI Core，支持的数据类型为int16_t/half/float；支持的数据通路为VECOUT->GM。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，支持的数据类型为int8_t/int16_t/half/bfloat16_t/int32_t/float；支持的数据通路为VECOUT/L0C/L1->GM。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，支持的数据类型为int8_t/int16_t/half/bfloat16_t/int32_t/float；支持的数据通路为VECOUT/L0C/L1->GM。

Atlas 350 加速卡，支持的数据类型为int8_t/int16_t/half/bfloat16_t/int32_t/float；支持的数据通路为VECOUT/L0C Buffer->GM。

Atlas 200I/500 A2 推理产品，支持的数据类型为int16_t/half/int32_t/float；支持的数据通路为VECOUT/L0C/L1->GM

返回值说明

无

约束说明

●累加操作完成后，建议通过DisableDmaAtomic关闭原子累加，以免影响后续相关指令功能。

●该指令执行前不会对GM的数据做清零操作，开发者根据实际的算子逻辑判断是否需要清零，如果需要自行进行清零操作。

调用示例

本示例中，使用DataCopy从VECOUT搬出数据到外部dstGlobal时进行原子累加。为保证原子累加的正确性，在核函数调用前，需要对dstGm清零。

调用示例如下：
