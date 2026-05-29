# FreeTensor

> **Section**: 4  
> **PDF Pages**: 1793–1793  

---

<!-- page 1793 -->

表6-699参数说明

输入/输出

参数名称

含义

tensor输入inplace接口需要传入LocalTensor作为内存管理的对象。

约束说明

●non-inplace接口分配的Tensor内容可能包含随机值。

●non-inplace接口，需要将TQueBind的depth模板参数设置为非零值；inplace接口，需要将TQueBind的depth模板参数设置为0。

返回值说明

non-inplace接口返回值为LocalTensor对象，inplace接口没有返回值。

调用示例

●non-inplace接口AscendC::TPipe pipe;AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 2> que;int num = 4;int len = 1024;pipe.InitBuffer(que, num, len); // InitBuffer分配内存块数为4，每块大小为1024BytesAscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>(); // AllocTensor分配Tensor长度为1024Bytes

●inplace接口AscendC::TPipe pipe;AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 0> que;int num = 2;int len = 1024;pipe.InitBuffer(que, num, len); // InitBuffer分配内存块数为2，每块大小为1024BytesAscendC::LocalTensor<half> tensor1;que.AllocTensor<half>(tensor1); // AllocTensor分配Tensor长度为1024Bytes

## ?.4. FreeTensor

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√
