# VacantInQue

> **Section**: 6  
> **PDF Pages**: 1778–1778  

---

<!-- page 1778 -->

AscendC::LocalTensor<half> tensor2 = que.DeQue<AscendC::TPosition::GM, AscendC::TPosition::VECIN, half>(); // inplace接口AscendC::TPipe pipe;AscendC::TQue<AscendC::TPosition::VECOUT, 0> que;int num = 2;int len = 1024;pipe.InitBuffer(que, num, len);AscendC::LocalTensor<half> tensor1;que.AllocTensor<half>(tensor1);que.EnQue(tensor1);que.DeQue<half>(tensor1); // 将tensor从VECOUT的Queue中搬出que.FreeTensor<half>(tensor1);

## ?.6. VacantInQue

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

查询队列是否已满。

函数原型

```cpp
__aicore__ inline bool VacantInQue()
```

参数说明

无

约束说明

该接口不支持Tensor原地操作，即TQue的depth设置为0的场景。

返回值说明

●true - 表示Queue未满，可以继续Enque操作

●false - 表示Queue已满，不可以继续入队
