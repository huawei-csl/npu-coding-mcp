# SetAtomicType

> **Section**: 6.2.3.10.2  
> **PDF Pages**: 1882–1883  

---

<!-- page 1882 -->

// 初始化LocalTensorAscendC::LocalTensor<float> src0Local = inQueueSrc0.AllocTensor<float>();// 清空原子操作的状态AscendC::DisableDmaAtomic();AscendC::DataCopy(src0Local, src0Global, 256);// 手动插入MTE3等待src0Global搬入src0Local同步AscendC::SetFlag<AscendC::HardEvent::MTE2_MTE3>(0);AscendC::WaitFlag<AscendC::HardEvent::MTE2_MTE3>(0);// 开启原子累加AscendC::SetAtomicAdd<float>();AscendC::DataCopy(dstGlobal, src0Local, 256);// 清空原子操作的状态AscendC::DisableDmaAtomic();inQueueSrc0.FreeTensor(src0Local);

结果示例如下：

每个核的输入数据Src0: [1,1,1,1,1,...,1] // 256个1最终输出数据dstGm: [3,3,3,3,3,...,3] // 256个3

## 6.2.3.10.2 SetAtomicType

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

通过设置模板参数来设定原子操作不同的数据类型。

函数原型

```cpp
template <typename T>__aicore__ inline void SetAtomicType()
```

<!-- page 1883 -->

参数说明

表6-760模板参数说明

参数名

描述

T设定不同的数据类型。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，支持int8_t/int16_t/half/bfloat16_t/int32_t/float

Atlas A3 训练系列产品/Atlas A3 推理系列产品，支持int8_t/int16_t/half/bfloat16_t/int32_t/float

Atlas 推理系列产品AI Core，支持int16_t/half/float

Atlas 350 加速卡, 支持int8_t/int16_t/half/bfloat16_t/int32_t/float

Atlas 200I/500 A2 推理产品，支持int16_t/half/int32_t/float

返回值说明

无

约束说明

需要和SetAtomicAdd、SetAtomicMax、SetAtomicMin配合使用。

使用完成后，建议清空原子操作的状态（详见6.2.3.10.3 DisableDmaAtomic），以免影响后续相关指令功能。

调用示例

// 本演示示例使用DataCopy从VECOUT搬出到外部dstGlobal时进行原子最小，并调用SetAtomicType修改原子最小的数据类型。#include "kernel_operator.h"// 初始化dst0Local与dst1Local AscendC::LocalTensor<T> dst0Local = queueDst0.DeQue<T>();AscendC::LocalTensor<T> dst1Local = queueDst1.DeQue<T>();// VECOUT dst1Local搬出到外部dstGlobalAscendC::DataCopy(dstGlobal, dst1Local, size);AscendC::PipeBarrier<PIPE_MTE3>();

// 设置后续传输时原子比较，将待拷贝的内容和GM已有内容进行比较，将最小值写入GM。AscendC::SetAtomicMin<int8_t>();  // 此处设置的类型可随意，此例中以int8_t为例AscendC::SetAtomicType<T>();  // 此处设置真实的数据类型// VECOUT dst0Local原子比较搬出到外部dstGlobalAscendC::DataCopy(dstGlobal, dst0Local, size);queueDst0.FreeTensor(dst0Local);queueDst1.FreeTensor(dst1Local);// 清空原子操作的状态AscendC::DisableDmaAtomic();每个核的输入数据为: Src0: [1,1,1,1,1,...,1] // 256个1Src1: [2,2,2,2,2,...,2] // 256个2最终输出数据: [1,1,1,1,1,...,1] // 256个1
