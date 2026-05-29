# TPipe构造函数

> **Section**: 2  
> **PDF Pages**: 1734–1734  

---

<!-- page 1734 -->

●内存资源管理：通过TPipe的InitBuffer接口，可以为TQue和TBuf分配内存，分别用于队列的内存初始化和临时变量内存的初始化。

●同步事件管理：通过TPipe的AllocEventID、ReleaseEventID等接口，可以申请和释放事件ID，用于同步控制。

## ?.2. TPipe 构造函数

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

构造用来管理内存和同步的TPipe对象。

函数原型

```cpp
__aicore__ inline TPipe()
```

约束说明

●避免TPipe在对象内创建和初始化，TPipe在对象内创建时，可能会影响编译器对对象内常量的优化，引起scalar性能劣化，具体原理请参考3.8.3.3 避免TPipe在对象内创建和初始化。

●TPipe对象同一时刻全局只能存在一份，同时定义多个TPipe对象，会出现卡死等随机行为。如果需要使用多个TPipe时，请先调用Destroy接口释放前一个TPipe。

返回值说明

无

调用示例

```cpp
template <typename ComputeT> class KernelExample {public:    __aicore__ inline KernelExample() {}    __aicore__ inline void Init(..., TPipe* pipeIn)    {        ...        pipe = pipeIn;
        pipe->InitBuffer(xxxBuf, BUFFER_NUM, xxxSize);
```
