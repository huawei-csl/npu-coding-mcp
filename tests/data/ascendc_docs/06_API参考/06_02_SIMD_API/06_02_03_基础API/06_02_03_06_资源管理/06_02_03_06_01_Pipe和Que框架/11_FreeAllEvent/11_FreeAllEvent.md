# FreeAllEvent

> **Section**: 11  
> **PDF Pages**: 1801–1802  

---

<!-- page 1801 -->

产品是否支持

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

查询Que中是否有空闲的内存块。

函数原型

```cpp
__aicore__ inline bool HasIdleBuffer()
```

参数说明

无

约束说明

该接口不支持Tensor原地操作，即TQue的depth设置为0的场景。

返回值说明

●true - 表示Queue中存在空闲内存

●false - 表示Queue中不存在空闲内存

调用示例

// 当前Que中已经分配了4块内存AscendC::TPipe pipe;AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;int num = 4;int len = 1024;pipe.InitBuffer(que, num, len);bool ret = que.HasIdleBuffer(); // 没有AllocTensor的操作，返回值为trueAscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();ret = que.HasIdleBuffer(); // AllocTensor了一块内存，返回值为trueAscendC::LocalTensor<half> tensor2 = que.AllocTensor<half>();AscendC::LocalTensor<half> tensor3 = que.AllocTensor<half>();AscendC::LocalTensor<half> tensor4 = que.AllocTensor<half>();ret = que.HasIdleBuffer(); // AllocTensor了四块内存，当前无空闲内存，返回值为false，继续AllocTensor会报错

## ?.11. FreeAllEvent

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

<!-- page 1802 -->

产品是否支持

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

释放队列中申请的所有同步事件。队列分配的Buffer关联着同步事件的eventID，因为同步事件的数量有限制，如果同时使用的队列Buffer数量超过限制，将无法继续申请队列，使用本接口释放队列中的事件后，可以再次申请队列。详细介绍请参考TQueBuffer限制。

函数原型

```cpp
__aicore__ inline void FreeAllEvent()
```

参数说明

无

约束说明

该接口不支持Tensor原地操作，即TQue的depth设置为0的场景。

返回值说明

无

调用示例

// 接口: DeQue TensorAscendC::TPipe pipe;AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;int num = 4;int len = 1024;pipe.InitBuffer(que, num, len);AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();que.EnQue(tensor1);tensor1 = que.DeQue<half>(); // 将tensor从VECOUT的Queue中搬出que.FreeTensor<half>(tensor1);que.FreeAllEvent();
