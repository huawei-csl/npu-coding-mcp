# SetSparse

> **Section**: 40  
> **PDF Pages**: 2458–2458  

---

<!-- page 2458 -->

```cpp
matmul_tiling::DataType::DT_FLOAT16);tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);tiling.SetShape(M, N, K);tiling.SetOrgShape(M, N, K);tiling.SetBias(true);tiling.SetBufferSpace(-1, -1, -1);tiling.SetSplitK(true);
optiling::TCubeTiling tilingData;int ret = tiling.GetTiling(tilingData);
```

## ?.40. SetSparse

功能说明

设置Matmul的使用场景是否为Sparse Matmul场景Sparse Matmul场景。

函数原型

```cpp
int32_t SetSparse(bool isSparseIn = false)
```

参数说明

表6-1108参数说明

参数名输入/输出

描述

isSparseIn输入设置是否为Sparse Matmul稀疏场景。

true：稀疏场景。

false：非稀疏场景。

返回值说明

-1表示设置失败；0表示设置成功。

约束说明

本接口必须在GetTiling接口前调用。

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform);
 tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
 tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
```
