# SetAlignSplit

> **Section**: 30  
> **PDF Pages**: 2444–2444  

---

<!-- page 2444 -->

返回值说明

-1表示获取失败； 0表示获取成功。

约束说明

使用创建的Tiling对象调用该接口，且需在完成Tiling计算（GetTiling）后调用。

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

// 获得多核切分后，使用的NumBlocksint32_t dim, mDim, nDim;int ret1 = tiling.GetCoreNum(dim, mDim, nDim);

## ?.30. SetAlignSplit

功能说明

多核切分时，设置singleCoreM/singleCoreN/singleCoreK的对齐值。比如设置singleCoreM的对齐值为64（单位为元素），切分出的singleCoreM为64的倍数。

函数原型

```cpp
int32_t SetAlignSplit(int32_t alignM, int32_t alignN, int32_t alignK)
```

参数说明

表6-1097参数说明

参数名输入/输出

描述

alignM输入singleCoreM的对齐值。若传入-1或0，表示不设置指定的singleCoreM的对齐值，该值由Tiling函数自行计算。

alignN输入singleCoreN的对齐值。若传入-1或0，表示不设置指定的singleCoreN的对齐值，该值由Tiling函数自行计算。

alignK输入singleCoreK的对齐值。若传入-1或0，表示不设置指定的singleCoreK的对齐值，该值由Tiling函数自行计算。
