# SetSingleRange

> **Section**: 27  
> **PDF Pages**: 2441–2441  

---

<!-- page 2441 -->

tiling.SetDim(1);  // 设置参与运算的核数tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);   tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);   tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);   tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);   tiling.SetShape(1024, 1024, 1024);   tiling.SetSingleShape(1024, 1024, 1024);tiling.SetOrgShape(1024, 1024, 1024);tiling.SetBias(true);   tiling.SetBufferSpace(-1, -1, -1);optiling::TCubeTiling tilingData;   int ret = tiling.GetTiling(tilingData);

## ?.27. SetSingleRange

功能说明

设置singleCoreM/singleCoreN/singleCoreK的最大值与最小值。

函数原型

```cpp
int32_t SetSingleRange(int32_t maxM = -1, int32_t maxN = -1, int32_t maxK = -1, int32_t minM = -1, int32_t minN = -1, int32_t minK = -1)
```

参数说明

表6-1094参数说明

参数名输入/输出

描述

maxM输入设置最大的singleCoreM值，默认值为-1，表示不设置指定的singleCoreM最大值，该值由Tiling函数自行计算。

maxN输入设置最大的singleCoreN值，默认值为-1，表示不设置指定的singleCoreN最大值，该值由Tiling函数自行计算。

maxK输入设置最大的singleCoreK值，默认值为-1，表示不设置指定的singleCoreK最大值，该值由Tiling函数自行计算。

minM输入设置最小的singleCoreM值，默认值为-1，表示不设置指定的singleCoreM最小值，该值由Tiling函数自行计算。

minN输入设置最小的singleCoreN值，默认值为-1，表示不设置指定的singleCoreN最小值，该值由Tiling函数自行计算。

minK输入设置最小的singleCoreK值，默认值为-1，表示不设置指定的singleCoreK最小值，该值由Tiling函数自行计算。

返回值说明

-1表示设置失败；0表示设置成功。
