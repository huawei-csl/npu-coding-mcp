# GetTensorCountInQue

> **Section**: 8  
> **PDF Pages**: 1780–1780  

---

<!-- page 1780 -->

返回值说明

●true - 表示Queue中存在已入队的Tensor

●false - 表示Queue为完全空闲

调用示例

// 根据VacantInQue判断当前que中是否有已入队的Tensor，当前que的深度为4，无内存Enque动作，返回为falseAscendC::TPipe pipe;AscendC::TQue<AscendC::TPosition::VECOUT, 4> que;int num = 4;int len = 1024;pipe.InitBuffer(que, num, len);bool ret = que.HasTensorInQue();

## ?.8. GetTensorCountInQue

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

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
