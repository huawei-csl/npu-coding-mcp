# GetBasicConfig

> **Section**: 6.2.4.2.1.11  
> **PDF Pages**: 2325–2327  

---

<!-- page 2325 -->

返回值说明

**MatmulConfig结构体。**

约束说明

IBShare模板当前仅适用于MIX场景，不支持纯CUBE场景。

调用示例

// 配置IBShare模板的参数，获取自定义IBShare模板。constexpr MatmulConfig MM_CFG = GetIBShareNormConfig(    /* intrinsicsLimit      */ false,     /* batchLoop            */ false,    /* isVecND2NZ           */ false,    /* bmmMode              */ BatchMode::BATCH_LESS_THAN_L1,    /* isMsgReuse           */ false,    /* enableUBReuse        */ true);// 常规Matmul计算，最后输出使用自定义IBShare模板的计算结果typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> aType; typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half, true/*开启矩阵转置*/, LayoutMode::NONE/*不使能BatchMatmul*/, true/*使能IBShare*/> bType; typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> cType; typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> biasType; AscendC::Matmul<A_TYPE, B_TYPE, C_TYPE, BIAS_TYPE, MM_CFG> mm;REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);mm.SetTensorA(gm_a);mm.SetTensorB(gm_b);if (tiling.isBias) {    mm.SetBias(gmBias);}mm.IterateAll(gm_c);mm.End();

## 6.2.4.2.1.11 GetBasicConfig

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

<!-- page 2326 -->

功能说明

用于配置BasicBlock模板的参数，获取自定义BasicBlock模板。BasicBlock模板的介绍请参考表模板特性。

使用该接口时可以优先考虑使用模板常量化。相比BasicBlock模板仅实现baseM、baseN、baseK常量化，模板常量化可以在此基础上实现singleCoreM、singleCoreN、singleCoreK、baseM、baseN、baseK的常量化，模板常量化的具体使用方式请参考Matmul Tiling常量化。

函数原型

```cpp
__aicore__ constexpr MatmulConfig GetBasicConfig(const uint32_t basicM, const uint32_t basicN, const uint32_t basicK, const bool intrinsicsLimit = false, const bool batchLoop = false, const BatchMode bmmMode = BatchMode::BATCH_LESS_THAN_L1)
```

参数说明

本接口的所有参数用于设置MatmulConfig结构体中的参数，其中互相对应的参数的功能作用相同。

表6-1028接口参数说明

参数名输入/输出

描述

basicM输入用于设置参数basicM。

与TCubeTiling结构体中的baseM参数含义相同，Matmul计算时base块M轴长度，以元素为单位。

basicN输入用于设置参数basicN。

与TCubeTiling结构体中的baseN参数含义相同，Matmul计算时base块N轴长度，以元素为单位。

basicK输入用于设置参数basicK。

与TCubeTiling结构体中的baseK参数含义相同，Matmul计算时base块K轴长度，以元素为单位。

intrinsicsLimit

输入用于设置参数intrinsicsCheck。

当左矩阵或右矩阵在单核上内轴（即尾轴）大于等于65535（元素个数）时，是否使能循环执行数据从GlobalMemory到L1 Buffer的搬入。例如，左矩阵A[M, K]，单核上的内轴数据singleCoreK大于65535，配置该参数为true后，API内部通过循环执行数据的搬入。参数取值如下：

●false：当左矩阵或右矩阵在单核上内轴大于等于65535时，不使能循环执行数据的搬入（默认值）。

●true：当左矩阵或右矩阵在单核上内轴大于等于65535时，使能循环执行数据的搬入。

对于Atlas 350 加速卡，MxMatmul场景不支持此参数。

<!-- page 2327 -->

参数名输入/输出

描述

batchLoop输入用于设置参数isNBatch。

是否多Batch输入多Batch输出。仅对BatchMatmul有效，使能该参数后，仅支持Norm模板，且需调用IterateNBatch实现多Batch输入多Batch输出。参数取值如下：

●false：不使能多Batch（默认值）。

●true：使能多Batch。

bmmMode输入用于设置参数batchMode。该参数用于BatchMatmul场景，关于BatchMatmul的介绍请参考3.3.3.3.14 BatchMatmul基础功能。

BatchMatmul场景中Layout类型为NORMAL时，设置BatchMatmul输入A/B矩阵的多batch数据总和与L1 Buffer的大小关系。参数取值如下：

●BatchMode::BATCH_LESS_THAN_L1：多batch数据总和<L1 Buffer Size；

●BatchMode::BATCH_LARGE_THAN_L1：多batch数据总和>L1 Buffer Size；

●BatchMode::SINGLE_LARGE_THAN_L1：单batch数据总和>L1 Buffer Size。

返回值说明

**MatmulConfig结构体。**

约束说明

●使用本接口时，基本块大小baseM、baseN需满足：singleCoreM能被baseM整除，singleCoreN能被baseN整除。

●本接口的参数basicM、basicN、basicK应与TCubeTiling结构体的baseM、baseN、baseK设置保持一致。

调用示例

BasicBlock模板的完整使用样例请参考basic_block_matmul样例。

// 配置BasicBlock模板的参数，获取自定义BasicBlock模板constexpr MatmulConfig MM_CFG = GetBasicConfig(    /* basicM              */ 128,    /* basicN              */ 256,    /* basicK              */ 64,    /* intrinsicsLimit     */ false,    /* batchLoop           */ false,    /* batchMode           */ BatchMode::BATCH_LESS_THAN_L1);// 常规Matmul计算，最后输出使用自定义BasicBlock模板的计算结果AscendC::Matmul<A_TYPE, B_TYPE, C_TYPE, BIAS_TYPE, MM_CFG> mm;REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);mm.SetTensorA(gm_a);
