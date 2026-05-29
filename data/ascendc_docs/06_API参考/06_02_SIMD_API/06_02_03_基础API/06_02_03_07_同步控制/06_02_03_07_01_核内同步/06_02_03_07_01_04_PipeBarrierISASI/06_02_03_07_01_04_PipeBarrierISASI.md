# PipeBarrier(ISASI)

> **Section**: 6.2.3.7.1.4  
> **PDF Pages**: 1829–1829  

---

<!-- page 1829 -->

```cpp
// AscendC::SetFlag<AscendC::HardEvent::S_MTE3>(EVENT_ID0);// AscendC::WaitFlag<AscendC::HardEvent::S_MTE3>(EVENT_ID0);AscendC::DataCopy(dstGlobal, dstLocal, dataSize);
```

## 6.2.3.7.1.4 PipeBarrier(ISASI)

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

阻塞相同流水，具有数据依赖的相同流水之间需要插入此同步。

函数原型

```cpp
template <pipe_t pipe>__aicore__ inline void PipeBarrier()
```

参数说明

表6-727模板参数说明

参数名描述

pipe模板参数，表示阻塞的流水类别。

支持的流水参考硬件流水类型。

如果不关注流水类别，希望阻塞所有流水，可以传入PIPE_ALL。

返回值说明

无

约束说明

Scalar流水之间的同步由硬件自动保证，调用PipeBarrier<PIPE_S>()会引发硬件错误。
