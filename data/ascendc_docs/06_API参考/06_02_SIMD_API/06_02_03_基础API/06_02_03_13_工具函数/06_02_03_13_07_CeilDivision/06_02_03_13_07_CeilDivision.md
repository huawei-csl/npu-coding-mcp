# CeilDivision

> **Section**: 6.2.3.13.7  
> **PDF Pages**: 1975–1975  

---

<!-- page 1975 -->

返回值说明

Vector Length的大小，单位为byte。

约束说明

无

调用示例

如下样例通过GetVecLen获取循环迭代次数：

```cpp
template <typename T>__aicore__ inline void AddCustomImpl(__local_mem__ T *dst, __local_mem__ T *src0, __local_mem__ T *src1,    uint32_t calCount){    AscendC::Reg::RegTensor<T> reg0;
    AscendC::Reg::RegTensor<T> reg1;
    AscendC::Reg::RegTensor<T> reg2;
    AscendC::Reg::MaskReg mask;
    constexpr uint32_t repeatElm = AscendC::GetVecLen() / sizeof(T);
    uint16_t repeatTime = AscendC::CeilDivision(calCount, repeatElm);
    for (uint16_t i = 0;
 i < repeatTime; ++i) {        mask = AscendC::Reg::UpdateMask<T>(calCount);
        AscendC::Reg::LoadAlign(reg0, src0 + i * repeatElm);
        AscendC::Reg::LoadAlign(reg1, src1 + i * repeatElm);
        AscendC::Reg::Add(reg2, reg0, reg1, mask);
        AscendC::Reg::StoreAlign(dst + i * repeatElm, reg2, mask);    }}
```

## 6.2.3.13.7 CeilDivision

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

计算两个整数num1和num2相除后向上取整结果。

函数原型

```cpp
__aicore__ constexpr inline int32_t CeilDivision(int32_t num1, int32_t num2)
```
