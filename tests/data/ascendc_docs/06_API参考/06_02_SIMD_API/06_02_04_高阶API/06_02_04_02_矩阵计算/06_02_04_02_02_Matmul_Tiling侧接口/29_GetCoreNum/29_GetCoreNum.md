# GetCoreNum

> **Section**: 29  
> **PDF Pages**: 2443–2443  

---

<!-- page 2443 -->

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform);
 tiling.SetDim(1);tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
   tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
   tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
   tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
   tiling.SetShape(1024, 1024, 1024);
   tiling.SetSingleShape(1024, 1024, 1024);tiling.SetOrgShape(1024, 1024, 1024);tiling.SetBias(true);
   tiling.SetBufferSpace(-1, -1, -1);optiling::TCubeTiling tilingData;
   int ret = tiling.GetTiling(tilingData);
```

// 获取计算后的singleCoreM/singleCoreN/singleCoreKint32_t singleM, singleN, singleK;int ret1 = tiling.GetSingleShape(singleM, singleN, singleK);

## ?.29. GetCoreNum

功能说明

获得多核切分所使用的NumBlocks参数。

函数原型

●MultiCoreMatmulTiling类int32_t GetCoreNum(int32_t &dim, int32_t &mDim, int32_t &nDim)

●BatchMatmulTiling类int32_t GetCoreNum(int32_t &dim, int32_t &mDim, int32_t &nDim, int32_t &batchCoreM, int32_t &batchCoreN)

参数说明

表6-1096参数说明

参数名输入/输出

描述

dim输出获取计算时所需要的核数， dim = mDim * nDim

mDim输出获取计算时M方向所需要的核数

nDim输出获取计算时N方向所需要的核数

batchCoreM

输出获取计算时batch M方向所需要的核数，仅BatchMatmulTiling类支持

batchCoreN

输出获取计算时batch N方向所需要的核数，仅BatchMatmulTiling类支持
