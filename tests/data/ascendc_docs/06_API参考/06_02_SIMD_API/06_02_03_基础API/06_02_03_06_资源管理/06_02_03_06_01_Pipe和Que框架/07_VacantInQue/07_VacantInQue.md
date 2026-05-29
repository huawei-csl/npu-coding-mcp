# VacantInQue

> **Section**: 7  
> **PDF Pages**: 1797–1797  

---

<!-- page 1797 -->

表6-705参数说明

输入/输出

参数名称

含义

tensor输出inplace接口需要通过出参的方式返回Tensor。

约束说明

●对空队列执行DeQue是一种异常行为，会在CPU调测时报错。

●non-inplace接口，需要将TQueBind的depth模板参数设置为非零值；inplace接口，需要将TQueBind的depth模板参数设置为0。

返回值说明

non-inplace接口的返回值为从队列中取出的LocalTensor；inplace接口没有返回值。

调用示例

●non-inplace接口AscendC::TPipe pipe;AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;int num = 4;int len = 1024;pipe.InitBuffer(que, num, len);AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();que.EnQue(tensor1);AscendC::LocalTensor<half> tensor2 = que.DeQue<half>(); // 将Tensor从VECOUT的Queue中搬出

●inplace接口AscendC::TPipe pipe;AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 0> que;int num = 2;int len = 1024;pipe.InitBuffer(que, num, len);AscendC::LocalTensor<half> tensor1;que.AllocTensor<half>(tensor1);que.EnQue(tensor1);que.DeQue<half>(tensor1); // 将Tensor从VECOUT的Queue中搬出que.FreeTensor<half>(tensor1);

## ?.7. VacantInQue

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex
