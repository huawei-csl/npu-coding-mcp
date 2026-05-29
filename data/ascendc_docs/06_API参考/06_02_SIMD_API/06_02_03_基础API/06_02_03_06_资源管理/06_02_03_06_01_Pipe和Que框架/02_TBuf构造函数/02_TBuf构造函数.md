# TBuf构造函数

> **Section**: 2  
> **PDF Pages**: 1807–1807  

---

<!-- page 1807 -->

●为TBuf分配的内存空间只能参与计算，无法执行队列的入队出队操作。

●调用一次内存初始化接口，TPipe只会为TBuf分配一块内存，为队列可以通过参数设置申请多块内存。如果要使用多个临时变量，需要定义多个TBuf数据结构，对每个TBuf数据结构分别调用 InitBuffer接口进行内存初始化。

●TBuf获取的Tensor无需释放。

## ?.2. TBuf 构造函数

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

创建TBuf对象时，初始化数据成员。

函数原型

```cpp
template <TPosition pos = TPosition::LCM>__aicore__ inline TBuf();
```

参数说明

表6-709模板参数说明

参数名称含义

posTBuf所在的逻辑位置，取值为VECCALC。关于TPosition的具体介绍请参考6.2.6.7 TPosition。

约束说明

无。
