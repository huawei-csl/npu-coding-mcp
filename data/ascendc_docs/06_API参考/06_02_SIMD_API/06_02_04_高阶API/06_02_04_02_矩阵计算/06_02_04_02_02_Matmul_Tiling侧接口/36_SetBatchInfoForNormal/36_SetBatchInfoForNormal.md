# SetBatchInfoForNormal

> **Section**: 36  
> **PDF Pages**: 2452–2452  

---

<!-- page 2452 -->

constexpr int32_t B_GNUM = 3;constexpr int32_t B_DNUM = 64;constexpr int32_t C_BNUM = 2;constexpr int32_t C_SNUM = 32;constexpr int32_t C_GNUM = 3;constexpr int32_t C_DNUM = 256;constexpr int32_t BATCH_NUM = 3;tiling.SetALayout(A_BNUM, A_SNUM, 1, A_GNUM, A_DNUM);tiling.SetBLayout(B_BNUM, B_SNUM, 1, B_GNUM, B_DNUM);tiling.SetCLayout(C_BNUM, C_SNUM, 1, C_GNUM, C_DNUM);tiling.SetBatchNum(BATCH_NUM);  // 设置Batch数tiling.SetBufferSpace(-1, -1, -1);

```cpp
optiling::TCubeTiling tilingData;int ret = tiling.GetTiling(tilingData);
```

## ?.36. SetBatchInfoForNormal

功能说明

设置A/B矩阵的M/N/K轴信息，以及A/B矩阵的Batch数。Layout类型为NORMAL的场景，调用IterateBatch或者IterateNBatch接口之前，需要在Host侧Tiling实现中通过本接口设置A/B矩阵的M/N/K轴等信息。

函数原型

```cpp
int32_t SetBatchInfoForNormal(int32_t batchA, int32_t batchB, int32_t m, int32_t n, int32_t k)
```

参数说明

表6-1103参数说明

参数名输入/输出

描述

batchA输入A矩阵的batch数

batchB输入B矩阵的batch数

m输入A矩阵的M轴信息

n输入B矩阵的N轴信息

k输入A/B矩阵的K轴信息

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

Layout类型为NORMAL的场景，调用IterateBatch或者IterateNBatch接口之前，需要在Host侧Tiling实现中通过本接口设置A/B矩阵的M/N/K轴等信息。

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform);
```
