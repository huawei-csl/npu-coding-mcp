# GetSpecialMDLConfig

> **Section**: 6.2.4.2.1.9  
> **PDF Pages**: 2320–2321  

---

<!-- page 2320 -->

```cpp
mm.SetBias(gmBias);}mm.IterateAll(gm_c);mm.End();
```

## 6.2.4.2.1.9 GetSpecialMDLConfig

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

用于配置SpecialMDL模板的参数，获取自定义SpecialMDL模板。SpecialMDL模板的介绍请参考表模板特性。

函数原型

```cpp
__aicore__ constexpr MatmulConfig GetSpecialMDLConfig(const bool intrinsicsLimit = false, const bool batchLoop = false, const uint32_t doMTE2Preload = 0, const bool isVecND2NZ = false, bool isPerTensor = false, bool hasAntiQuantOffset = false)
```

参数说明

本接口的所有参数用于设置MatmulConfig结构体中的参数，其中互相对应的参数的功能作用相同。

<!-- page 2321 -->

表6-1026接口参数说明

参数名输入/输出

描述

intrinsicsLimit

输入用于设置参数intrinsicsCheck。

当左矩阵或右矩阵在单核上内轴（即尾轴）大于等于65535（元素个数）时，是否使能循环执行数据从GlobalMemory到L1 Buffer的搬入。例如，左矩阵A[M, K]，单核上的内轴数据singleCoreK大于65535，配置该参数为true后，API内部通过循环执行数据的搬入。参数取值如下：

●false：当左矩阵或右矩阵在单核上内轴大于等于65535时，不使能循环执行数据的搬入（默认值）。

●true：当左矩阵或右矩阵在单核上内轴大于等于65535时，使能循环执行数据的搬入。

对于Atlas 350 加速卡，MxMatmul场景不支持此参数。

batchLoop输入用于设置参数isNBatch。

是否多Batch输入多Batch输出。仅对BatchMatmul有效，使能该参数后，仅支持Norm模板，且需调用IterateNBatch实现多Batch输入多Batch输出。参数取值如下：

●false：不使能多Batch（默认值）。

●true：使能多Batch。

doMTE2Preload

输入用于设置参数doMTE2Preload。

在MTE2流水间隙较大，且M/N数值较大时可通过该参数开启对应M/N方向的预加载功能，开启后能减小MTE2间隙，提升性能。预加载功能仅在MDL模板有效（不支持SpecialMDL模板）。参数取值如下：

●0：不开启（默认值）。

●1：开启M方向preload。

●2：开启N方向preload。

注意：开启M/N方向的预加载功能时需保证K全载且M/N方向开启2.9.5.1 DoubleBuffer；其中，M方向的K全载条件为：singleCoreK/baseK <= stepKa；N方向的K全载条件为：singleCoreK/baseK <= stepKb。

该参数的使用样例请参考M方向预加载Matmul算子样例。

isVecND2NZ输入预留参数，保持默认值false即可。

isPerTensor输入用于设置参数isPerTensor。

A矩阵half类型输入且B矩阵int8_t类型输入场景，使能B矩阵量化时是否为per tensor。

●true：per tensor量化。

●false：per channel量化。

对于Atlas 350 加速卡，MxMatmul场景不支持此参数。
