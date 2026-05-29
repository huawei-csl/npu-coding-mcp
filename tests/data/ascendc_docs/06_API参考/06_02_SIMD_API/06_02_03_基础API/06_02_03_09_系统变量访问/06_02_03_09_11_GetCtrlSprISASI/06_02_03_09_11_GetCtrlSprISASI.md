# GetCtrlSpr(ISASI)

> **Section**: 6.2.3.9.11  
> **PDF Pages**: 1878–1878  

---

<!-- page 1878 -->

●对于CTRL[8:6]和CTRL[10:9]的设置，已封装原子操作API，建议通过这些原子操作API进行配置。

–SetAtomicType

–DisableDmaAtomic

–SetAtomicAdd

–SetAtomicMax

–SetAtomicMin

调用示例

●如下示例中使能原子操作模式，数据类型为float。

```cpp
AscendC::SetCtrlSpr<6, 8>(1);
```

●原子操作中，half类型配置全局非饱和模式示例。AscendC::SetCtrlSpr<6, 8>(2);AscendC::SetAtomicAdd<half>();AscendC::DataCacheCleanAndInvalid<half, AscendC::CacheLine::ENTIRE_DATA_CACHE, AscendC::DcciDst::CACHELINE_ATOMIC>(dstTensor);AscendC::SetCtrlSpr<48, 48>(1);...

## 6.2.3.9.11 GetCtrlSpr(ISASI)

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

读取CTRL寄存器（控制寄存器）特定比特位上的值。

函数原型

```cpp
template <int8_t startBit, int8_t endBit>__aicore__ static inline int64_t GetCtrlSpr()
```
