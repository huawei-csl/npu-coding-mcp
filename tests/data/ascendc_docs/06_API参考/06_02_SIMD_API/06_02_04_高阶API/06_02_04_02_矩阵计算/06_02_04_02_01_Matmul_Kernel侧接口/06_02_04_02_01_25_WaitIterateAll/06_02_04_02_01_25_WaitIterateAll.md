# WaitIterateAll

> **Section**: 6.2.4.2.1.25  
> **PDF Pages**: 2367–2367  

---

<!-- page 2367 -->

## 6.2.4.2.1.25 WaitIterateAll

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

等待IterateAll异步接口返回，支持连续输出到Global Memory。

函数原型

```cpp
__aicore__ inline void WaitIterateAll()
```

参数说明

无

返回值说明

无

约束说明

●配套IterateAll异步接口使用。

●仅支持连续输出至Global Memory。

调用示例

详细的使用样例请参考IterateAll异步场景样例。

AscendC::Matmul<aType, bType, cType, biasType> mm;mm.SetTensorA(gm_a[offsetA]);mm.SetTensorB(gm_b[offsetB]);if (tiling.isBias) {    mm.SetBias(gm_bias[offsetBias]);}mm.template IterateAll<false>(gm_c[offsetC], 0, false, true);// do some others computemm.WaitIterateAll(); // 等待IterateAll完成
