# HasIdleBuffer

> **Section**: 10  
> **PDF Pages**: 1800–1800  

---

<!-- page 1800 -->

产品是否支持

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

查询Que中已入队的Tensor数量。

函数原型

```cpp
__aicore__ inline int32_t GetTensorCountInQue()
```

参数说明

无

约束说明

该接口不支持Tensor原地操作，即TQue的depth设置为0的场景。

返回值说明

Que中已入队的Tensor数量

调用示例

// 通过GetTensorCountInQue查询que中已入队的Tensor数量，当前通过AllocTensor接口分配了内存，并加入que中，num为1。AscendC::TPipe pipe;AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;int num = 4;int len = 1024;pipe.InitBuffer(que, num, len);AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();que.EnQue(tensor1);// 将tensor加入VECOUT的Queue中int32_t numb = que.GetTensorCountInQue();

## ?.10. HasIdleBuffer

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√
