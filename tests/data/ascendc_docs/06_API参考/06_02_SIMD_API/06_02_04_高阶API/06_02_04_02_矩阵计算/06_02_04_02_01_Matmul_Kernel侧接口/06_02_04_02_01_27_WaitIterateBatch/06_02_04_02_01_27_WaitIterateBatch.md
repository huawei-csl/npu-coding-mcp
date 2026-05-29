# WaitIterateBatch

> **Section**: 6.2.4.2.1.27  
> **PDF Pages**: 2375–2375  

---

<!-- page 2375 -->

## 6.2.4.2.1.27 WaitIterateBatch

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

等待IterateBatch异步接口或IterateNBatch异步接口返回，支持连续输出到GlobalMemory。

函数原型

```cpp
__aicore__ inline void WaitIterateBatch()
```

参数说明

无

返回值说明

无

约束说明

●配套IterateBatch或IterateNBatch异步接口使用。

●仅支持连续输出至Global Memory。

●当使能MixDualMaster（双主模式）场景时，即模板参数enableMixDualMaster设置为true，不支持使用该接口。

调用示例

AscendC::Matmul<aType, bType, cType, biasType> mm;mm.SetTensorA(gm_a[offsetA]);mm.SetTensorB(gm_b[offsetB]);if (tiling.isBias) {    mm.SetBias(gm_bias[offsetBias]);}mm.IterateBatch(gm_c[offsetC], batchA, batchB, false);// do some other compute tasksmm.WaitIterateBatch(); // 等待IterateBatch完成
