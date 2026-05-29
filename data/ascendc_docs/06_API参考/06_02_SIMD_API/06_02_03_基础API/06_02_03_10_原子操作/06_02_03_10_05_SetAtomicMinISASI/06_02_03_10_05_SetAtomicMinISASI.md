# SetAtomicMin(ISASI)

> **Section**: 6.2.3.10.5  
> **PDF Pages**: 1886–1886  

---

<!-- page 1886 -->

约束说明

●使用完后，建议通过DisableDmaAtomic关闭原子最大操作，以免影响后续相关功能。

●对于Atlas A2 训练系列产品/Atlas A2 推理系列产品，目前无法对bfloat16_t类型设置inf/nan模式。

调用示例

```cpp
#include "kernel_operator.h"
uint32_t size = 256;AscendC::LocalTensor<half> dst0Local = queueDst0.DeQue<half>();AscendC::LocalTensor<half> dst1Local = queueDst1.DeQue<half>();AscendC::DataCopy(dstGlobal, dst1Local, size);AscendC::PipeBarrier<PIPE_MTE3>();AscendC::SetAtomicMax<half>();AscendC::DataCopy(dstGlobal, dst0Local, size);queueDst0.FreeTensor(dst0Local);queueDst1.FreeTensor(dst1Local);AscendC::DisableDmaAtomic();
```

每个核的输入数据为: Src0: [1,1,1,1,1,...,1] // 256个1Src1: [2,2,2,2,2,...,2] // 256个2最终输出数据: [2,2,2,2,2,...,2] // 256个2

## 6.2.3.10.5 SetAtomicMin(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

原子操作函数，设置后续从VECOUT传输到GM的数据是否执行原子比较，将待拷贝的内容和GM已有内容进行比较，将最小值写入GM。

可通过设置模板参数来设定不同的数据类型。

函数原型

```cpp
template <typename T>__aicore__ inline void SetAtomicMin()
```
