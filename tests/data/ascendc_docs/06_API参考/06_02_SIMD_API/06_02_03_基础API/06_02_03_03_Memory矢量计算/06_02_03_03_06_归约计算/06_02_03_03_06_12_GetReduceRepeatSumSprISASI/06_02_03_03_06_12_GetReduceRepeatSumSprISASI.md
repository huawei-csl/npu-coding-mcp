# GetReduceRepeatSumSpr(ISASI)

> **Section**: 6.2.3.3.6.12  
> **PDF Pages**: 1428–1428  

---

<!-- page 1428 -->

]输出数据(dst_gm):[128 256 ... 384]

## 6.2.3.3.6.12 GetReduceRepeatSumSpr(ISASI)

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

获取ReduceSum接口（Tensor前n个数据计算接口，n为接口的count参数）的计算结果。

函数原型

```cpp
template <typename T>__aicore__ inline T GetReduceRepeatSumSpr()
```

参数说明

表6-401模板参数说明

参数名描述

TReduceSum指令的数据类型，支持half、float。

返回值说明

ReduceSum接口（Tensor前n个数据计算接口，n为接口的count参数）的计算结果。

约束说明

无。

调用示例

```cpp
AscendC::LocalTensor<float> src;AscendC::LocalTensor<float> work;
```
