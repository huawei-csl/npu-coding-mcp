# TBufPool构造函数

> **Section**: 2  
> **PDF Pages**: 1755–1756  

---

<!-- page 1755 -->

## ?.2. TBufPool 构造函数

功能说明

创建TBufPool对象时，初始化数据成员。

函数原型

```cpp
template <TPosition pos, uint32_t bufIDSize = defaultBufIDSize>__aicore__ inline TBufPool();
```

参数说明

表6-675模板参数说明

参数名说明

posTBufPool逻辑位置，可以为VECIN、VECOUT、VECCALC、A1、B1、C1。关于TPosition的具体介绍请参考6.2.6.7 TPosition。

bufIDSizeTBufPool可分配Buffer数量，默认为4，不超过16。对于非共享模式的资源分配，在本TBufPool上再次申请TBufPool时，申请的bufIDSize不能超过原TBufPool剩余可用的Buffer数量；对于共享模式的资源分配，在本TBufPool上再次申请TBufPool时，申请的bufIDSize不能超过原TBufPool设置的Buffer数量。

约束说明

无。

## ?.3. InitBufPool

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

<!-- page 1756 -->

功能说明

通过Tpipe::InitBufPool接口可划分出整块资源，整块TbufPool资源可以继续通过TBufPool::InitBufPool接口划分成小块资源。

函数原型

●非共享模式template <class T>__aicore__ inline bool InitBufPool(T& bufPool, uint32_t len)

●共享模式template <class T, class U>__aicore__ inline bool InitBufPool(T& bufPool, uint32_t len, U& shareBuf)

参数说明

表6-676模板参数说明

参数名说明

TbufPool参数的类型。

UshareBuf参数的类型。

表6-677 InitBufPool(T& bufPool, uint32_t len) 原型定义参数说明

输入/输出

参数名称

含义

bufPool输入新划分的资源池，类型为TBufPool。

len输入新划分资源池长度，单位为字节，非32字节对齐会自动向上补齐至32字节对齐。

表6-678 InitBufPool(T& bufPool, uint32_t len, U& shareBuf) 原型定义参数说明

输入/输出

参数名称

含义

bufPool输入新划分的资源池，类型为TBufPool。

len输入新划分资源池长度，单位为字节，非32字节对齐会自动向上补齐至32字节对齐。

shareBuf

输入被复用资源池，类型为TBufPool，新划分资源池与被复用资源池共享起始地址及长度。

约束说明

1.新划分的资源池与被复用资源池的物理内存需要一致，两者共享起始地址及长度；
