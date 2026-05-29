# GetMatmulApiTiling

> **Section**: 6.2.4.2.1.48  
> **PDF Pages**: 2402–2403  

---

<!-- page 2402 -->

```cpp
*dataCopyOutParams, const uint64_t tilingPtr, const uint64_t dataPtr);void CopyA1(const LocalTensor<int8_t> &aMatrix, const __gm__ void *gm, int row, int col, int useM, int useK, const uint64_t tilingPtr, const uint64_t dataPtr);void CopyB1(const LocalTensor<int8_t> &bMatrix, const __gm__ void *gm, int row, int col, int useK, int useN, const uint64_t tilingPtr, const uint64_t dataPtr);
```

typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> aType; typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> bType; typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> cType; typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> biasType; AscendC::Matmul<aType, bType, cType, biasType, CFG_NORM, MatmulCallBackFunc<DataCopyOut, CopyA1, CopyB1>> mm;REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);GlobalTensor<SrcT> dataGM; // 保存有回调函数需使用的计算数据的GMuint64_t dataGMPtr = reinterpret_cast<uint64_t>(dataGM.address_);// 回调函数中需要使用dataPtr参数时，必须调用此接口mm.SetSelfDefineData(dataGMPtr);mm.SetTensorA(gmA);mm.SetTensorB(gmB);mm.IterateAll();

## 6.2.4.2.1.48 GetMatmulApiTiling

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

本接口用于在编译期间获取常量化的Matmul Tiling参数。

Matmul Tiling常量化功能为在编译期期间获取常量化的Matmul Tiling参数并进行算子编译，从而减少Scalar计算开销，提升算子整体性能。具体为，在获取Matmul模板时，可以确定MatmulConfig的singleCore Shape（MatmulConfig中的singleCoreM/singleCoreN/singleCoreK）和Base Shape（MatmulConfig中的basicM/basicN/basicK）参数，或者只确定Base Shape参数；通过指定获取模板的接口中的singleCoreShape和Base Shape参数，或者只指定Base Shape参数，获取自定义模板；然后调用本接口，得到常量化的Matmul Tiling参数。

当在调用获取MatmulConfig模板的接口时，只将(baseM, baseN, baseK)设置为常数值时，称为部分常量化，此时(singleCoreM, singleCoreN, singleCoreK)都保持默认值0，部分常量化场景在Kernel侧使用REGIST_MATMUL_OBJ初始化Matmul对象时，仍需要使用Tiling；将(baseM, baseN, baseK, singleCoreM, singleCoreN, singleCoreK)都设置为常数值时，称为全量常量化，这时可以在REGIST_MATMUL_OBJ的入参传递Tiling参数的位置，使用空指针替代。

<!-- page 2403 -->

经过上述部分常量化或全部常量化后，将得到带有常量化参数的MatmulConfig模板，然后使用本接口将Tiling参数常量化。本接口的返回值包含常量化的Matmul Tiling参数和MatmulConfig模板。

函数原型

```cpp
template<class A_TYPE, class B_TYPE, class C_TYPE, class BIAS_TYPE>__aicore__ constexpr MatmulApiStaticTiling GetMatmulApiTiling(const MatmulConfig& mmCFG, int32_t l1Size = Impl::L1_SIZE)
```

参数说明

表6-1063模板参数说明

参数名描述

A_TYPEA矩阵类型信息，通过MatmulType来定义。

B_TYPEB矩阵类型信息，通过MatmulType来定义。

C_TYPEC矩阵类型信息，通过MatmulType来定义。

BIAS_TYPEBIAS矩阵类型信息，通过MatmulType来定义。

表6-1064参数说明

参数名输入/输出

描述

mmCFG输入获取的MatmulConfig模板。

对于Atlas 350 加速卡，支持常量化的为全部模板：Norm,IBShare, MDL模板。

对于Atlas A3 训练系列产品/Atlas A3 推理系列产品，支持常量化的模板有：Norm, MDL模板。

对于Atlas A2 训练系列产品/Atlas A2 推理系列产品，支持常量化的模板有：Norm, MDL模板。

l1Size输入可用的L1大小，默认值L1_SIZE。

返回值说明

**MatmulApiStaticTiling**
