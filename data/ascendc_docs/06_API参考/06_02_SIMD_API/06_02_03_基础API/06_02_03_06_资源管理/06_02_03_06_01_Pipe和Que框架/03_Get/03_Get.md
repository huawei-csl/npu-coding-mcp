# Get

> **Section**: 3  
> **PDF Pages**: 1808–1808  

---

<!-- page 1808 -->

## ?.3. Get

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

从TBuf上获取指定长度的Tensor，或者获取全部长度的Tensor。

函数原型

●获取全部长度的Tensortemplate <typename T>__aicore__ inline LocalTensor<T> Get()

●获取指定长度的Tensortemplate <typename T>__aicore__ inline LocalTensor<T> Get(uint32_t len)

参数说明

表6-710模板参数说明

参数名称

含义

T待获取Tensor的数据类型。

表6-711参数说明

输入/输出

参数名称

含义

len输入需要获取的Tensor元素个数。
