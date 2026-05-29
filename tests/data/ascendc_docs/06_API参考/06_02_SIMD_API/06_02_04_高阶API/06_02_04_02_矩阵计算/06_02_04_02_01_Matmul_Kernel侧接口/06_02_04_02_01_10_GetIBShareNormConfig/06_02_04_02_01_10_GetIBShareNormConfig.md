# GetIBShareNormConfig

> **Section**: 6.2.4.2.1.10  
> **PDF Pages**: 2322–2324  

---

<!-- page 2322 -->

参数名输入/输出

描述

hasAntiQuantOffset

输入用于设置参数hasAntiQuantOffset。

A矩阵half类型输入且B矩阵int8_t类型输入场景，使能B矩阵量化时是否使用offset系数。

对于Atlas 350 加速卡，MxMatmul场景不支持此参数。

返回值说明

**MatmulConfig结构体。**

约束说明

无

调用示例

// 配置SpecialMDL模板的参数，获取自定义SpecialMDL模板constexpr MatmulConfig MM_CFG = GetSpecialMDLConfig(    /* intrinsicsLimit      */ false,    /* batchLoop            */ false,    /* doMTE2Preload        */ 0,    /* isVecND2NZ           */ false,    /* isPerTensor          */ false,    /* hasAntiQuantOffset   */ false);// 常规Matmul计算，最后输出使用自定义SpecialMDL模板的计算结果AscendC::Matmul<A_TYPE, B_TYPE, C_TYPE, BIAS_TYPE, MM_CFG> mm;REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);mm.SetTensorA(gm_a);mm.SetTensorB(gm_b);if (tiling.isBias) {    mm.SetBias(gmBias);}mm.IterateAll(gm_c);mm.End();

## 6.2.4.2.1.10 GetIBShareNormConfig

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

<!-- page 2323 -->

产品是否支持

Atlas 训练系列产品x

功能说明

用于配置IBShare模板的参数，获取自定义IBShare模板。IBShare模板的介绍请参考表模板特性。

函数原型

```cpp
__aicore__ constexpr MatmulConfig GetIBShareNormConfig(const bool intrinsicsLimit = false, const bool batchLoop = false, const bool isVecND2NZ = false, const BatchMode bmmMode = BatchMode::BATCH_LESS_THAN_L1, const bool isDoubleCache = false, const bool enUnitFlag = true)
```

参数说明

本接口的所有参数用于设置MatmulConfig结构体中的参数，其中互相对应的参数的功能作用相同。

表6-1027接口参数说明

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

<!-- page 2324 -->

参数名输入/输出

描述

isVecND2NZ输入用于设置参数enVecND2NZ。

使能通过vector指令进行ND2NZ。使能时需要设置SetLocalWorkspace。参数取值如下：

●false：不使能通过vector指令进行ND2NZ（默认值）。

●true：使能通过vector指令进行ND2NZ。

针对Atlas 推理系列产品AI Core，在Unified Buffer空间足够的条件下（Unified Buffer空间大于2倍TCubeTiling的transLength参数），建议优先使能该参数，搬运性能更好。

对于Atlas 350 加速卡，MxMatmul场景不支持此参数。

bmmMode输入用于设置参数batchMode。该参数用于BatchMatmul场景，关于BatchMatmul的介绍请参考3.3.3.3.14 BatchMatmul基础功能。

BatchMatmul场景中Layout类型为NORMAL时，设置BatchMatmul输入A/B矩阵的多batch数据总和与L1 Buffer的大小关系。参数取值如下：

●BatchMode::BATCH_LESS_THAN_L1：多batch数据总和<L1 Buffer Size；

●BatchMode::BATCH_LARGE_THAN_L1：多batch数据总和>L1 Buffer Size；

●BatchMode::SINGLE_LARGE_THAN_L1：单batch数据总和>L1 Buffer Size。

isDoubleCache

输入用于设置参数enableDoubleCache。

开启IBShare模板后，在L1 Buffer上是否同时缓存两块数据。参数取值如下：

●false：L1 Buffer上同时缓存一块数据（默认值）。

●true：使能L1 Buffer上同时缓存两块数据。

注意：该参数取值为true时，需要控制基本块大小，防止两块数据的缓存超过L1 Buffer大小限制。

包括MxMatmul场景，Atlas 350 加速卡不支持此参数。

enUnitFlag输入用于设置参数enUnitFlag。

使能UnitFlag功能，使计算与搬运流水并行，提高性能。Norm, IBShare下默认使能，MDL下默认不使能。参数取值如下：

●false：不使能UnitFlag功能。

●true：使能UnitFlag功能。

注意：对于Atlas 350 加速卡，MxMatmul场景，仅在NORM/MDL模板、A和scaleA不转置、 B和scaleB转置、C为ND格式，输出到GM场景下，使能UnitFlag功能有性能收益。
