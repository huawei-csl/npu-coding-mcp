# Unlock

> **Section**: 3  
> **PDF Pages**: 1833–1834  

---

<!-- page 1833 -->

表6-730参数说明

参数名输入/输出

描述

id输入进行流水同步管理的MutexID。

该id可通过用户自定义（范围为0-27）或者通过AllocMutexID/ReleaseMutexID进行申请释放。

返回值说明

无

约束说明

●用户在使用Lock/Unlock时且自定义MutexID情况时，禁止同时使用TQue、TQueBind、TBufPool中的相关接口。

●对于同一个MutexID，必须按照Lock/Unlock配套使用，且指定的pipe也需相同，即当且只有完成一个流水的Lock/Unlock之后，才能进行其余流水的操作。

●相同流水之间存在数据依赖的场景，这种情况建议使用PipeBarrier接口。

调用示例

// 锁定 MTE2 流水线互斥锁，确保当前线程独占 MTE2 资源进行数据搬运AscendC::Mutex::Lock<PIPE_MTE2>(mutexId);AscendC::DataCopy(xLocal, src0Global[TILE_LENGTH * progress], TILE_LENGTH);AscendC::DataCopy(yLocal, src1Global[TILE_LENGTH * progress], TILE_LENGTH);// 解锁 MTE2 流水线，允许其他线程使用 MTE2AscendC::Mutex::Unlock<PIPE_MTE2>(mutexId);

// 锁定 Vector 流水线互斥锁，确保当前线程独占向量计算资源AscendC::Mutex::Lock<PIPE_V>(mutexId);AscendC::Add(zLocal, xLocal, yLocal, TILE_LENGTH);// 解锁 Vector 流水线，释放计算资源供其他线程使用AscendC::Mutex::Unlock<PIPE_V>(mutexId);

## ?.3. Unlock

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

<!-- page 1834 -->

产品是否支持

Atlas 训练系列产品x

功能说明

直到前置当前流水指令退出后，根据MutexID释放对应Mutex。

函数原型

```cpp
template <pipe_t pipe>static __aicore__ inline void Unlock(MutexID id)
```

参数说明

表6-731模板参数说明

参数名描述

pipe模板参数，表示流水类别。

支持的流水参考硬件流水类型。

表6-732参数说明

参数名输入/输出

描述

id输入进行流水同步管理的MutexID。

该id可通过用户自定义（范围为0-27）或者通过AllocMutexID/ReleaseMutexID进行申请释放。

返回值说明

无

约束说明

●用户在使用Lock/Unlock时且自定义MutexID情况时，禁止同时使用TQue、TQueBind、TBufPool中的相关接口。

●对于同一个MutexID，必须按照Lock/Unlock配套使用，且指定的pipe也需相同，即当且只有完成一个流水的Lock/Unlock之后，才能进行其余流水的操作。

●相同流水之间存在数据依赖的场景，这种情况建议使用PipeBarrier接口。

调用示例

参考调用示例。
