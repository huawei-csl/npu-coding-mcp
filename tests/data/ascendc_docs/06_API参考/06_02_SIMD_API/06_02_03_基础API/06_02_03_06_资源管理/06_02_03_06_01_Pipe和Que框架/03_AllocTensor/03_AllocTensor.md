# AllocTensor

> **Section**: 3  
> **PDF Pages**: 1792–1792  

---

<!-- page 1792 -->

返回值说明

无

## ?.3. AllocTensor

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

从Que中分配Tensor，Tensor所占大小为InitBuffer时设置的每块内存长度。

函数原型

●non-inplace接口：构造新的Tensor作为内存管理的对象template <typename T>__aicore__ inline LocalTensor<T> AllocTensor()

●inplace接口：直接使用传入的Tensor作为内存管理的对象，可以减少Tensor反复创建的开销，具体使用指导可参考2.10.9.5 如何使用Tensor原地操作提升算子性能。template <typename T>__aicore__ inline void AllocTensor(LocalTensor<T>& tensor)

参数说明

表6-698模板参数说明

参数名说明

TTensor的数据类型。
