# SetBLayout

> **Section**: 33  
> **PDF Pages**: 2448–2448  

---

<!-- page 2448 -->

constexpr int32_t C_SNUM = 32;constexpr int32_t C_GNUM = 3;constexpr int32_t C_DNUM = 256;constexpr int32_t BATCH_NUM = 3;tiling.SetALayout(A_BNUM, A_SNUM, 1, A_GNUM, A_DNUM);  // 设置A矩阵排布tiling.SetBLayout(B_BNUM, B_SNUM, 1, B_GNUM, B_DNUM);tiling.SetCLayout(C_BNUM, C_SNUM, 1, C_GNUM, C_DNUM);tiling.SetBatchNum(BATCH_NUM);tiling.SetBufferSpace(-1, -1, -1);

```cpp
optiling::TCubeTiling tilingData;int ret = tiling.GetTiling(tilingData);
```

## ?.33. SetBLayout

功能说明

设置B矩阵的Layout轴信息，包括B、S、N、G、D轴。对于BSNGD、SBNGD、BNGS1S2 Layout格式，调用IterateBatch接口之前，需要在Host侧Tiling实现中通过本接口设置B矩阵的Layout轴信息。

函数原型

```cpp
int32_t SetBLayout(int32_t b, int32_t s, int32_t n, int32_t g, int32_t d)
```

参数说明

表6-1100参数说明

参数名输入/输出

描述

b输入B矩阵Layout的B轴信息

s输入B矩阵Layout的S轴信息

n输入B矩阵Layout的N轴信息

g输入B矩阵Layout的G轴信息

d输入B矩阵Layout的D轴信息

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

对于BSNGD、SBNGD、BNGS1S2 Layout格式，调用IterateBatch接口之前，需要在Host侧Tiling实现中通过本接口设置B矩阵的Layout轴信息。

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform);
   int32_t M = 32;int32_t N = 256;
```
