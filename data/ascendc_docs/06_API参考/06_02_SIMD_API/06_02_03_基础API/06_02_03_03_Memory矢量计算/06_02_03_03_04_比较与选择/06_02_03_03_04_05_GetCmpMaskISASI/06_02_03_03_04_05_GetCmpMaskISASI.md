# GetCmpMask(ISASI)

> **Section**: 6.2.3.3.4.5  
> **PDF Pages**: 1322–1323  

---

<!-- page 1322 -->

●左操作数及右操作数中，必须有一个为矢量；当前不支持左右操作数同时为标量。

●本接口传入LocalTensor单点数据作为标量时，idx参数需要传入编译期已知的常量，传入变量时需要声明为constexpr。

调用示例

对于灵活标量位置接口，支持直接传入立即数或单点LocalTensor作为标量，并且支持标量在前和在后两种调用方式，调用示例如下；

●tensor前n个数据计算接口样例// 标量在后，src1Local[0]作为标量AscendC::Compares(dstLocal, src0Local, src1Local[0], AscendC::CMPMODE::LT, srcDataSize);

// 标量在前，src0Local[0]作为标量static constexpr AscendC::BinaryConfig config = { 0 };AscendC::Compares<BinaryDefaultType, BinaryDefaultType, true, config>(dstLocal, src0Local[0], src1Local, AscendC::CMPMODE::LT, srcDataSize);

●tensor高维切分计算-mask连续模式uint64_t mask = 256 / sizeof(float); // 256为每个迭代处理的字节数int repeat = 4;AscendC::UnaryRepeatParams repeatParams = { 1, 1, 8, 8 };// repeat = 4, 64 elements one repeat, 256 elements total// dstBlkStride, srcBlkStride = 1, no gap between blocks in one repeat// dstRepStride, srcRepStride = 8, no gap between repeats// 标量在后，src1Local[0]作为标量AscendC::Compares(dstLocal, src0Local, src1Local[0], AscendC::CMPMODE::LT, mask, repeat, repeatParams);

// 标量在前，src0Local[0]作为标量static constexpr AscendC::BinaryConfig config = { 0 };AscendC::Compares<BinaryDefaultType, BinaryDefaultType, true, config>(dstLocal, src0Local[0], src1Local, AscendC::CMPMODE::LT, mask, repeat, repeatParams);

●tensor高维切分计算-mask逐bit模式uint64_t mask[2] = { UINT64_MAX, 0};int repeat = 4;AscendC::UnaryRepeatParams repeatParams = { 1, 1, 8, 8 };// repeat = 4, 64 elements one repeat, 256 elements total// srcBlkStride, = 1, no gap between blocks in one repeat// dstRepStride, srcRepStride = 8, no gap between repeats// 标量在后，src1Local[0]作为标量AscendC::Compares(dstLocal, src0Local, src1Local[0], AscendC::CMPMODE::LT, mask, repeat, repeatParams);

// 标量在前，src0Local[0]作为标量static constexpr AscendC::BinaryConfig config = { 0 };AscendC::Compares<BinaryDefaultType, BinaryDefaultType, true, config>(dstLocal, src0Local[0], src1Local, AscendC::CMPMODE::LT, mask, repeat, repeatParams);

## 6.2.3.3.4.5 GetCmpMask(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

<!-- page 1323 -->

产品是否支持

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

此接口用于获取Compare（结果存入寄存器）指令的比较结果。

**Compare（结果存入寄存器）指令会将比较后的结果写入CmpMask寄存器中，使用GetCmpMask接口可以获取到CmpMask寄存器的值从而得到Compare的结果。**

函数原型

```cpp
template<typename T>__aicore__ inline void GetCmpMask(const LocalTensor<T>& dst)
```

参数说明

表6-357模板参数说明

参数名

描述

T操作数的数据类型。

表6-358参数说明

输入/输出

参数名

描述

dst输出Compare（结果存入寄存器）指令的比较结果。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要16字节对齐。

返回值说明

无

约束说明

dst的空间大小不能少于128字节。
