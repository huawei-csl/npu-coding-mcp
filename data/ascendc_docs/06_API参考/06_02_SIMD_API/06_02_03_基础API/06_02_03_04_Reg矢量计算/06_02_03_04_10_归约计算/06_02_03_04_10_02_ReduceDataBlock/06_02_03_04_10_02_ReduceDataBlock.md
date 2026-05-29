# ReduceDataBlock

> **Section**: 6.2.3.4.10.2  
> **PDF Pages**: 1678–1679  

---

<!-- page 1678 -->

●对于归约求最小值，当所有元素均不参与计算时，将该数据类型的最大值写入dstReg，当存在多个最小值时，会将第一个最小值的索引保存在dstReg中。

●当归约求最小值或者归约求最大值时，源操作数的数据类型和目的操作数相同。

调用示例

●归约求和：template<typename T, typename U>__simd_vf__ inline void ReduceVF(__ubuf__ T* dstAddr, __ubuf__ U* srcAddr, uint32_t count,  uint32_t srcRepeatSize, uint32_t dstRepeatSize, uint16_t repeatTimes){    AscendC::Reg::RegTensor<U> srcReg;    AscendC::Reg::RegTensor<T> dsrReg;    AscendC::Reg::MaskReg mask;    for (uint16_t i = 0; i < repeatTimes; i++) {        AscendC::Reg::LoadAlign(srcReg, srcAddr + i * srcRepeatSize);        mask = AscendC::Reg::UpdateMask<U>(count);        AscendC::Reg::Reduce<AscendC::Reg::ReduceType::SUM>(dsrReg, srcReg, mask);        AscendC::Reg::StoreAlign(dstAddr + i * dstRepeatSize, dsrReg, mask);    }}

●归约求最大值或者最小值template<typename T>__aicore__ inline void ReduceVF(__ubuf__ T* dstAddr, __ubuf__ T* srcAddr, uint32_t count, uint32_t oneRepeatSize, uint16_t repeatTimes){    AscendC::Reg::RegTensor<T> srcReg;    AscendC::Reg::RegTensor<T> dstReg;    AscendC::Reg::MaskReg mask;    for (uint16_t i = 0; i < repeatTimes; i++) {        AscendC::Reg::LoadAlign(srcReg, srcAddr + i * oneRepeatSize);        mask = AscendC::Reg::UpdateMask<T>(count);        // type = ReduceType::MAX        AscendC::Reg::Reduce<AscendC::Reg::ReduceType::MAX>(dstReg, srcReg, mask);        // type = ReduceType::MIN        // AscendC::Reg::Reduce<AscendC::Reg::ReduceType::MIN>(dstReg, srcReg, mask);        AscendC::Reg::StoreAlign(dstAddr + i * oneRepeatSize, dstReg, maskReg);    }}

## 6.2.3.4.10.2 ReduceDataBlock

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

<!-- page 1679 -->

功能说明

当ReduceType 为SUM，将每个DataBlock（32B）中参与计算的元素相加，并将最终的计算结果依次保存在dstReg的最低位。

当ReduceType 为MAX，将每个DataBlock（32B）中的最大值，并将最终的计算结果依次保存在dstReg中的最低位。

当ReduceType 为MIN，将每个DataBlock（32B）中的最小值，并将最终的计算结果依次保存在dstReg中的最低位。

定义原型

```cpp
template <ReduceType type = ReduceType::SUM, typename T = DefaultType, MaskMergeMode mode = MaskMergeMode::ZEROING, typename U>__simd_callee__ inline void ReduceDataBlock(U& dstReg, U srcReg, MaskReg mask)
```

参数说明

表6-603模板参数说明

参数名描述

typeReduceType类型，支持SUM、MAX、MIN。enum class ReduceType {    SUM = 0,    MAX,    MIN,};

T目的操作数和源操作数的数据类型。

Atlas 350 加速卡, 支持的数据类型为：int16_t/uint16_t/half/int32_t/uint32_t/float

mode选择MERGING模式或ZEROING模式。当前仅支持ZEROING模式。

●ZEROING，mask未筛选的元素在dst中置零。

U目的操作数和源操作数的RegTensor类型，例如RegTensor<int32_t>，由编译器自动推导，用户不需要填写。

表6-604函数参数说明

参数名输入/输出

描述

dstReg输出目的操作数。

类型为RegTensor。

srcReg输入源操作数。

类型为RegTensor
