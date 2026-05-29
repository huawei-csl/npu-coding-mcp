# SetBatchNum

> **Section**: 35  
> **PDF Pages**: 2451–2451  

---

<!-- page 2451 -->

## ?.35. SetBatchNum

功能说明

设置多Batch计算的最大Batch数，最大Batch数为A矩阵batchA和B矩阵batchB中的最大值。调用IterateBatch接口之前，需要在Host侧Tiling实现中通过本接口设置多Batch计算的Batch数。

函数原型

```cpp
int32_t SetBatchNum(int32_t batch)
```

参数说明

表6-1102参数说明

参数名输入/输出

描述

batch输入多Batch计算的Batch数，Batch数为A矩阵batchA和B矩阵batchB中的最大值。

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

调用IterateBatch接口之前，需要在Host侧Tiling实现中通过本接口设置多Batch计算的Batch数。

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform);
   int32_t M = 32;int32_t N = 256;int32_t K = 64;tiling.SetDim(1);tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);tiling.SetShape(M, N, K);tiling.SetOrgShape(M, N, K);tiling.SetBias(true);tiling.SetBufferSpace(-1, -1, -1);
constexpr int32_t A_BNUM = 2;constexpr int32_t A_SNUM = 32;constexpr int32_t A_GNUM = 3;constexpr int32_t A_DNUM = 64;constexpr int32_t B_BNUM = 2;constexpr int32_t B_SNUM = 256;
```
