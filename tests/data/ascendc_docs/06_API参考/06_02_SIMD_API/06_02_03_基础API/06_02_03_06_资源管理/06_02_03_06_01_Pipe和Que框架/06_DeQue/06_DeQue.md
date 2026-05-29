# DeQue

> **Section**: 6  
> **PDF Pages**: 1796–1796  

---

<!-- page 1796 -->

int num = 4;int len = 1024;pipe.InitBuffer(que, num, len);AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();que.EnQue(tensor1);// 将tensor加入VECOUT的Queue中

## ?.6. DeQue

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

将Tensor从队列中取出，用于后续处理。

函数原型

●non-inplace接口：将入队的LocalTensor地址从队列中取出赋值给新创建的Tensor并返回template <typename T>__aicore__ inline LocalTensor<T> DeQue()

●inplace接口：通过出参的方式返回，可以减少Tensor反复创建的开销，具体使用指导可参考2.10.9.5 如何使用Tensor原地操作提升算子性能。template <typename T>__aicore__ inline void DeQue(LocalTensor<T>& tensor)

参数说明

表6-704模板参数说明

参数名说明

TTensor的数据类型。
