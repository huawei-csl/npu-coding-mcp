# IterateNBatch

> **Section**: 6.2.4.2.1.28  
> **PDF Pages**: 2376–2377  

---

<!-- page 2376 -->

## 6.2.4.2.1.28 IterateNBatch

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

调用一次IterateNBatch，会进行N次IterateBatch计算，计算出N个多Batch的singleCoreM * singleCoreN大小的C矩阵。在调用该接口前，需将MatmulConfig中的isNBatch参数设为true，使能多Batch输入多Batch输出功能，并调用SetWorkspace接口申请临时空间，用于缓存计算结果，即IterateNBatch的结果输出至SetWorkspace指定的Global Memory内存中。

对于BSNGD、SBNGD、BNGS1S2的Layout格式，调用该接口之前需要在tiling中使用SetALayout/SetBLayout/SetCLayout/SetBatchNum设置A/B/C的Layout轴信息和最大BatchNum数；对于Normal数据格式则需使用SetBatchInfoForNormal设置A/B/C的M/N/K轴信息和A/B矩阵的BatchNum数。实例化Matmul时，通过MatmulType设置Layout类型，当前支持3种Layout类型：BSNGD、SBNGD、BNGS1S2。

函数原型

```cpp
template <bool sync = true, bool waitIterateBatch = false>__aicore__ inline void IterateNBatch(const uint32_t batchLoop, uint32_t batchA, uint32_t batchB, bool enSequentialWrite, const uint32_t matrixStrideA = 0, const uint32_t matrixStrideB = 0, const uint32_t matrixStrideC = 0)
```

参数说明

表6-1055模板参数说明

参数名描述

sync获取C矩阵过程分为同步和异步两种模式：

●同步：需要同步等待IterateNBatch执行结束，后续由开发者自行获取输出到Global Memory上的计算结果。

●异步：不需要同步等待IterateNBatch执行结束。

通过该参数设置同步或者异步模式：同步模式设置为true；异步模式设置为false。默认为同步模式。

<!-- page 2377 -->

参数名描述

waitIterateBatch

是否需要通过WaitIterateBatch接口等待IterateNBatch执行结束，仅在异步场景下使用。默认为false。

true：需要通过WaitIterateBatch接口等待IterateNBatch执行结束，然后由开发者自行获取输出到Global Memory上的计算结果。

false：不需要通过WaitIterateBatch接口等待IterateNBatch执行结束。调用本接口后，需要调用GetBatchTensorC接口获取C矩阵，或者由开发者自行处理等待IterateNBatch执行结束的过程。

参数名输入/输出

描述

batchLoop

输入当前计算的BMM个数。

batchA输入当前单次BMM调用计算左矩阵的batch数。

batchB输入当前单次BMM调用计算右矩阵的batch数，brc场景batchA/B不相同。

enSequentialWrite

输入输出是否连续存放数据。

matrixStrideA

输入A矩阵源操作数相邻nd矩阵起始地址间的偏移，默认值是0。

matrixStrideB

输入B矩阵源操作数相邻nd矩阵起始地址间的偏移，默认值是0。

matrixStrideC

输入该参数预留，保持默认值0即可。

返回值说明

无

约束说明

●单BMM内计算遵循之前的约束条件。

●对于BSNGD、SBNGD、BNGS1S2 Layout格式，输入A、B矩阵多Batch数据总和应小于L1 Buffer的大小。

●当使能MixDualMaster（双主模式）场景时，即模板参数enableMixDualMaster设置为true，不支持使用该接口。

调用示例

实例功能：完成aGM、bGM矩阵乘，结果保存到cGm上，其中aGM数据的layout格式为BSNGD，bGM数据的layout格式为BSNGD，cGM的layout格式为BNGS1S2，左矩
