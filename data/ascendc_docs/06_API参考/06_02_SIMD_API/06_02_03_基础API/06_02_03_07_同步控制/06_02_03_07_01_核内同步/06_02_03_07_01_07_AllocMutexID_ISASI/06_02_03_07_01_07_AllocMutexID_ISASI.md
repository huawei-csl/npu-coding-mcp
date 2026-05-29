# AllocMutexID (ISASI)

> **Section**: 6.2.3.7.1.7  
> **PDF Pages**: 1835–1835  

---

<!-- page 1835 -->

## 6.2.3.7.1.7 AllocMutexID (ISASI)

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

从框架获取并占用一个MutexID，与ReleaseMutexID配合使用，管理MutexID的获取和释放。获取的MutexID可以传入Mutex::Lock/Unlock接口使用，此时Mutex::Lock/Unlock可以与TQue等其他接口配合使用。

函数原型

```cpp
__aicore__ inline MutexID AllocMutexID()
```

参数说明

无

返回值说明

返回MutexID，其类型定义如下，每个ID表示一个Mutex锁。

```cpp
using MutexID = uint8_t;
```

约束说明

MutexID有数量限制，使用结束应该立刻调用ReleaseMutexID释放，防止MutexID耗尽。

调用示例

```cpp
MutexID id = AllocMutexID();Mutex::Lock<PIPE_MTE2>(id);DataCopy(local, gm, 1024);Mutex::Unlock<<PIPE_MTE2>(id);Mutex::Lock<PIPE_V>(id);Adds(local, local, 1, 1024);Mutex::Unlock<PIPE_V>(id);ReleaseMutexID(id);
```
