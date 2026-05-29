# DisableDmaAtomic

> **Section**: 6.2.3.10.3  
> **PDF Pages**: 1884–1884  

---

<!-- page 1884 -->

## 6.2.3.10.3 DisableDmaAtomic

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

清空原子操作的状态。

函数原型

```cpp
__aicore__ inline void DisableDmaAtomic()
```

参数说明

无

返回值说明

无

约束说明

无

调用示例

constexpr uint32_t totalLength = 256;    // 参与搬运的元素个数AscendC::LocalTensor<float> src0Local;AscendC::GlobalTensor<float> dstGlobal;AscendC::SetAtomicAdd<float>();    // 开启原子累加，累加数据类型为floatAscendC::DataCopy(dstGlobal, src0Local, totalLength * sizeof(float));AscendC::DisableDmaAtomic();    // 清空原子操作的状态
