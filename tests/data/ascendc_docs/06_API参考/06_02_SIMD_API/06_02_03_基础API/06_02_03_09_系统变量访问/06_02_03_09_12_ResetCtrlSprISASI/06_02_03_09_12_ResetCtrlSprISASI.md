# ResetCtrlSpr(ISASI)

> **Section**: 6.2.3.9.12  
> **PDF Pages**: 1879–1879  

---

<!-- page 1879 -->

参数说明

表6-757模板参数说明

参数名描述

startBit起始比特位索引。

endBit终止比特位索引。

返回值说明

CTRL寄存器对应比特位上的值。

约束说明

无

调用示例

如下为读取CTRL[8:6]比特位数值的示例。

```cpp
int64_t value = AscendC::GetCtrlSpr<6, 8>();
```

## 6.2.3.9.12 ResetCtrlSpr(ISASI)

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

对CTRL寄存器（控制寄存器）的特定比特位做重置。

函数原型

```cpp
template <int8_t startBit, int8_t endBit>__aicore__ static inline void ResetCtrlSpr()
```
