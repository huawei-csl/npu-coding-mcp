# SetStoreAtomicConfig(ISASI)

> **Section**: 6.2.3.10.6  
> **PDF Pages**: 1887–1888  

---

<!-- page 1887 -->

参数说明

表6-762模板参数说明

参数名

描述

T设定不同的数据类型。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，支持int8_t/int16_t/half/bfloat16_t/int32_t/float。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，支持int8_t/int16_t/half/bfloat16_t/int32_t/float。

Atlas 350 加速卡，支持int8_t/int16_t/half/bfloat16_t/int32_t/float。

返回值说明

无

约束说明

使用完后，建议通过DisableDmaAtomic关闭原子最小操作，以免影响后续相关指令功能。

调用示例

```cpp
#include "kernel_operator.h"
uint32_t size = 256;AscendC::LocalTensor<half> dst0Local = queueDst0.DeQue<half>();AscendC::LocalTensor<half> dst1Local = queueDst1.DeQue<half>();AscendC::DataCopy(dstGlobal, dst1Local, size);AscendC::PipeBarrier<PIPE_MTE3>();AscendC::SetAtomicMin<half>();AscendC::DataCopy(dstGlobal, dst0Local, size);queueDst0.FreeTensor(dst0Local);queueDst1.FreeTensor(dst1Local);AscendC::DisableDmaAtomic();
```

每个核的输入数据为: Src0: [1,1,1,1,1,...,1] // 256个1Src1: [2,2,2,2,2,...,2] // 256个2最终输出数据: [1,1,1,1,1,...,1] // 256个1

## 6.2.3.10.6 SetStoreAtomicConfig(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

<!-- page 1888 -->

产品是否支持

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

设置原子操作使能位与原子操作类型。

函数原型

```cpp
template <AtomicDtype type, AtomicOp op>__aicore__ inline void SetStoreAtomicConfig()
```

参数说明

表6-763模板参数说明

参数名输入/输出

描述

type输入原子操作使能位，AtomicDtype枚举类的定义如下：enum class AtomicDtype {    ATOMIC_NONE = 0,  // 无原子操作    ATOMIC_F32,       // 使能原子操作，进行原子操作的数据类型为float    ATOMIC_F16,       // 使能原子操作，进行原子操作的数据类型为half    ATOMIC_S16,       // 使能原子操作，进行原子操作的数据类型为int16_t    ATOMIC_S32,       // 使能原子操作，进行原子操作的数据类型为int32_t    ATOMIC_S8,        // 使能原子操作，进行原子操作的数据类型为int8_t    ATOMIC_BF16       // 使能原子操作，进行原子操作的数据类型为bfloat16_t};

op输入原子操作类型，仅当使能原子操作时有效（即“type”为非“ATOMIC_NONE”的场景），当前仅支持求和操作。enum class AtomicOp {    ATOMIC_SUM = 0   // 求和操作};

返回值说明

无

约束说明

无
