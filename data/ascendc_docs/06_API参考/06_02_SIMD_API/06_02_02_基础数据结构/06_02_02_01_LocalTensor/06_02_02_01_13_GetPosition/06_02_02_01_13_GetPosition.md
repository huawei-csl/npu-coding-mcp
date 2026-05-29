# GetPosition

> **Section**: 6.2.2.1.13  
> **PDF Pages**: 828–828  

---

<!-- page 828 -->

调用示例

// 示例// 调用GetPhyAddr()返回LocalTensor地址，CPU上返回的是指针类型(T*)，NPU上返回的是物理存储的地址(uint64_t)#ifdef ASCEND_CPU_DEBUGfloat *inputLocalCpuPtr = inputLocal.GetPhyAddr();uint64_t realAddr = (uint64_t)inputLocalCpuPtr - (uint64_t)(GetTPipePtr()->GetBaseAddr(static_cast<int8_t>(AscendC::TPosition::VECCALC)));#elseuint64_t realAddr = inputLocal.GetPhyAddr();

## 6.2.2.1.13 GetPosition

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品√

功能说明

获取LocalTensor所在的TPosition逻辑位置，支持TPosition为VECIN、VECOUT、VECCALC、A1、A2、B1、B2、CO1、CO2。

函数原型

```cpp
__aicore__ inline int32_t GetPosition() const
```

参数说明

无

返回值说明

LocalTensor所在的TPosition逻辑位置。

约束说明

无

调用示例

// 示例AscendC::TPosition srcPos = (AscendC::TPosition)inputLocal.GetPosition();
