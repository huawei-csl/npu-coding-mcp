# Lock

> **Section**: 2  
> **PDF Pages**: 1832–1832  

---

<!-- page 1832 -->

●Unlock：直到前置当前流水指令退出后，根据MutexID释放对应Mutex。

原型定义

```cpp
using MutexID = uint8_t;class Mutex {template <pipe_t pipe>static __aicore__ inline void Lock(MutexID id);template <pipe_t pipe>static __aicore__ inline void Unlock(MutexID id);};
```

## ?.2. Lock

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

根据MutexID获取Mutex，并阻塞当前流水指令队列，直到对应的MutexID被Unlock。

函数原型

```cpp
template <pipe_t pipe>static __aicore__ inline void Lock(MutexID id)
```

参数说明

表6-729模板参数说明

参数名描述

pipe模板参数，表示流水类别。

支持的流水参考硬件流水类型。
