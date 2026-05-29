# PairReduceElem

> **Section**: 6.2.3.4.10.3  
> **PDF Pages**: 1680–1681  

---

<!-- page 1680 -->

参数名输入/输出

描述

mask输入源操作数元素操作的有效指示，详细说明请参考MaskReg。

约束说明

无

调用示例

```cpp
template<typename T>__simd_vf__ inline void ReduceDataBlockVF(__ubuf__ T* dstAddr, __ubuf__ T* srcAddr, uint32_t count,  uint32_t oneRepeatSize, uint16_t repeatTimes){    AscendC::Reg::RegTensor<T> srcReg;
    AscendC::Reg::RegTensor<T> dstReg;
    AscendC::Reg::MaskReg mask;
    for (uint16_t i = 0;
 i < repeatTimes;
 i++) {        AscendC::Reg::LoadAlign(srcReg, srcAddr + i * oneRepeatSize);
        mask = AscendC::Reg::UpdateMask<T>(count);        // type = ReduceType::SUM        AscendC::Reg::ReduceDataBlock<AscendC::Reg::ReduceType::SUM>(dstReg, srcReg, mask);        // type = ReduceType::MAX        // AscendC::Reg::ReduceDataBlock<AscendC::Reg::ReduceType::MAX>(dstReg, srcReg, mask);        // type = ReduceType::MIN        // AscendC::Reg::ReduceDataBlock<AscendC::Reg::ReduceType::MIN>(dstReg, srcReg, mask);
        AscendC::Reg::StoreAlign(dstAddr + i * oneRepeatSize, dstReg, mask);     }}
```

## 6.2.3.4.10.3 PairReduceElem

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

将传入的srcReg中相邻两个数值相加，并将产生的结果保存在dstReg中的低位位置。

<!-- page 1681 -->

定义原型

```cpp
template <PairReduce type = PairReduce::SUM, typename T = DefaultType, MaskMergeMode mode = MaskMergeMode::ZEROING, typename U>__simd_callee__ inline void PairReduceElem(U& dstReg, U srcReg, MaskReg mask)
```

参数说明

表6-605模板参数说明

参数名描述

type具体的PairReduce类型，当前仅支持归约求和计算。enum class PairReduce {    SUM = 0,};

T目的操作数和源操作数的数据类型。

Atlas 350 加速卡，支持的数据类型为：half/float

mode选择MERGING模式或ZEROING模式。

●ZEROING，mask未筛选的元素在dst中置零。目前仅支持该模式。

U目的操作数和源操作数的RegTensor类型，由编译器自动推导，用户不需要填写。

表6-606函数参数说明

参数名输入/输出

描述

dstReg输出目的操作数。

类型为RegTensor。

srcReg输入源操作数。

类型为RegTensor。

源操作数的数据类型和目的操作数保持一致。

mask输入源操作数元素操作的有效指示，详细说明请参考MaskReg。

约束说明

无

调用示例

```cpp
template<typename T>__simd_vf__ inline void PairReduceElemVF(__ubuf__ T* dstAddr, __ubuf__ T* srcAddr, uint32_t count,  uint32_t oneRepeatSize, uint16_t repeatTimes){
```
