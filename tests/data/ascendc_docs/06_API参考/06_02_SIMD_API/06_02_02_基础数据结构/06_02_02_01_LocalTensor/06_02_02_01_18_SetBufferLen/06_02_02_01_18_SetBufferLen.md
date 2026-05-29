# SetBufferLen

> **Section**: 6.2.2.1.18  
> **PDF Pages**: 833–833  

---

<!-- page 833 -->

```cpp
AscendC::LocalTensor<float> tmpBuffer1 = tempBmm2Queue.AllocTensor<float>();AscendC::LocalTensor<half> tmpHalfBuffer;tmpHalfBuffer.SetAddrWithOffset(tmpBuffer1, calcSize * 2);
```

## 6.2.2.1.18 SetBufferLen

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

设置Buffer长度。当用户调用operator[]函数创建新LocalTensor时，建议调用该接口设置新LocalTensor长度，便于编译器对内存及同步进行自动优化。

函数原型

```cpp
__aicore__ inline void SetBufferLen(uint32_t dataLen)
```

参数说明

表6-63参数说明

参数名输入/输出

描述

dataLen输入Buffer的元素个数。

返回值说明

无

约束说明

无
