# Alloc

> **Section**: 4  
> **PDF Pages**: 1819–1819  

---

<!-- page 1819 -->

## ?.4. Alloc

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品x

功能说明

根据用户指定的逻辑位置、数据类型、数据长度返回对应的LocalTensor对象。

函数原型

●原型1：tileSize为模板参数// 当tileSize为常量时，建议使用此接口，以获得更优的性能template <class DataType, uint32_t tileSize> LocalTensor<DataType> __aicore__ inline Alloc()template <TPosition pos, class DataType, uint32_t tileSize> __aicore__ inline LocalTensor<DataType> Alloc()

●原型2：tileSize为接口入参// 当tileSize为动态参数时使用此接口template <class DataType> LocalTensor<DataType> __aicore__ inline Alloc(uint32_t tileSize)template <TPosition pos, class DataType> LocalTensor<DataType> __aicore__ inline Alloc(uint32_t tileSize)

●原型3：使用TensorTrait时使用此接口template <class DataType> LocalTensor<DataType> __aicore__ inline Alloc()

参数说明

表6-720原型1 和原型2 模板参数说明

参数名描述

posTPosition位置，需要符合LocalMemAllocator中指定的Hardware物理位置（静态Tensor编程场景下，此参数可以省略）。

DataTypeLocalTensor的数据类型，只支持基础数据类型，不支持TensorTrait类型。

tileSizeLocalTensor的元素个数，其数量不应超过当前物理位置剩余的内存空间。
