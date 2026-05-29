# NotifyNextBlock

> **Section**: 6.2.3.7.2.7  
> **PDF Pages**: 1850–1851  

---

<!-- page 1850 -->

返回值说明

无

约束说明

●gmWorkspace申请的空间最少要求为：blockNum * 32Bytes；ubWorkspace申请的空间最少要求为：blockNum * 32 + 32Bytes；其中blockNum为调用的核数，可调用6.2.3.9.1 GetBlockNum获取。

●使用该接口进行多核控制时，算子调用时指定的逻辑numBlocks必须保证不大于实际运行该算子的AI处理器核数，否则框架进行多轮调度时会插入异常同步，导致Kernel“卡死”现象。

调用示例

如下示例模拟8个核进行数据处理，使用确定性计算接口保证核间运行顺序，进行原子累加。

// m_gmWorkspace为初始化核间同步的共享内存，类型为GlobalTensor；ubWorkspace为操作m_gmWorkspace的临时空间，类型为LocalTensorint64_t m_tileCount = 256 * sizeof(int32_t); // 参与计算的元素总数所占的空间，单位为bytes// 初始化GM共享内存的值AscendC::InitDetermineComputeWorkspace(m_gmWorkspace, ubWorkspace);// copy in// srcLocal为int32_t类型的LocalTensor，m_srcGlobal为int32_t的GlobalTensorAscendC::DataCopy(srcLocal, m_srcGlobal[m_tileCount], m_tileCount);// copy out// 调用WaitPreBlock读GM地址中的值，确认是否需要继续等待AscendC::WaitPreBlock(m_gmWorkspace, ubWorkspace);// 开启原子累加AscendC::SetAtomicAdd<int32_t>();// m_dstGlobal为int32_t的GlobalTensorAscendC::DataCopy(m_dstGlobal[m_tileCount], srcLocal, m_tileCount);AscendC::DisableDmaAtomic();// 调用NotifyNextBlock写GM地址，通知下一个核当前核的操作已完成，下一个核可以进行操作AscendC::NotifyNextBlock(m_gmWorkspace, ubWorkspace);//每个核的输入数据为: [1,1,1,1,1,...,1] // 256个1//最终输出数据:[8,8,8,8,8,...,8] // 256个8

## 6.2.3.7.2.7 NotifyNextBlock

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

<!-- page 1851 -->

功能说明

通过写GM地址，通知下一个核当前核的操作已完成，下一个核可以进行操作。使用接口前，请确保已经调用 InitDetermineComputeWorkspace接口，初始化共享内存。

函数原型

```cpp
__aicore__ inline void NotifyNextBlock(GlobalTensor<int32_t>& gmWorkspace, LocalTensor<int32_t>& ubWorkspace)
```

参数说明

表6-745接口参数说明

参数名称输入/输出

含义

gmWorkspace

输入临时空间，通过写gmWorkspace通知其他核当前核已执行完成，其他核可以继续往下执行，类型为GlobalTensor。

ubWorkspace

输入临时空间，用于操作gmWorkspace，类型为LocalTensor。

返回值说明

无

约束说明

●需要保证每个核调用该接口的次数相同。

●gmWorkspace申请的空间最少要求为：blockNum * 32Bytes；ubWorkspace申请的空间最少要求为：blockNum * 32 + 32Bytes；其中blockNum为调用的核数，可调用6.2.3.9.1 GetBlockNum获取。

●分离模式下，使用该接口进行多核同步时，仅对AIV核生效，WaitPreBlock和NotifyNextBlock之间仅支持插入矢量计算相关指令，对矩阵计算相关指令不生效。

●使用该接口进行多核控制时，算子调用时指定的逻辑numBlocks必须保证不大于实际运行该算子的AI处理器核数，否则框架进行多轮调度时会插入异常同步，导致Kernel“卡死”现象。

调用示例

请参考调用示例。
