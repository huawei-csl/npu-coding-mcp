# GetSsbufBaseAddr

> **Section**: 6.2.3.13.8  
> **PDF Pages**: 1976–1976  

---

<!-- page 1976 -->

参数说明

表6-816模板参数说明

参数名描述

num1参数1，被除数。

num2参数2，除数。

返回值说明

两个整数相除的向上取整结果。

约束说明

●当num2为0时，结果为0。

●该接口仅支持在num1和num2为正数场景下使用。

调用示例

本示例中使用CeilDivision计算迭代次数 repeatTimes，通过对数据量count与单次处理数据量进行向上取整除法，确保所有数据（包括尾块）均被完整处理。

```cpp
template <typename T>__aicore__ inline void AddCustomImpl(__local_mem__ T *dst, __local_mem__ T *src0, __local_mem__ T *src1,    uint32_t count){    AscendC::Reg::RegTensor<T> srcReg0;
    AscendC::Reg::RegTensor<T> srcReg1;
    AscendC::Reg::RegTensor<T> dstReg;
    AscendC::Reg::MaskReg mask;
    constexpr uint32_t oneRepeatSize = AscendC::GetVecLen() / sizeof(T);
    uint16_t repeatTime = AscendC::CeilDivision(count, oneRepeatSize);
    for (uint16_t i = 0;
 i < repeatTime; ++i) {        mask = AscendC::Reg::UpdateMask<T>(calCount);
        AscendC::Reg::LoadAlign(srcReg0, src0 + i * oneRepeatSize );
        AscendC::Reg::LoadAlign(srcReg1, src1 + i * oneRepeatSize );
        AscendC::Reg::Add(dstReg, srcReg0, srcReg1, mask);
        AscendC::Reg::StoreAlign(dst + i * repeatElm, reg2, mask);    }}
```

## 6.2.3.13.8 GetSsbufBaseAddr

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x
