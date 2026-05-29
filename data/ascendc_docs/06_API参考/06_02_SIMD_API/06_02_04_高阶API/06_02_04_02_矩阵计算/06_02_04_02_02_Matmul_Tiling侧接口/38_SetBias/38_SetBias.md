# SetBias

> **Section**: 38  
> **PDF Pages**: 2456–2456  

---

<!-- page 2456 -->

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16); tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);   tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);   tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);   tiling.SetShape(1024, 1024, 1024);   tiling.SetOrgShape(1024, 1024, 1024);  tiling.SetBias(true);   tiling.SetBufferSpace(-1, -1, -1);tiling.SetMatmulConfigParams(0);  // 额外设置// matmul_tiling::MatmulConfigParams configParams = {1, false, matmul_tiling::ScheduleType::OUTER_PRODUCT, matmul_tiling::MatrixTraverse::FIRSTM};// tiling.SetMatmulConfigParams(configParams);optiling::TCubeTiling tilingData;   int ret = tiling.GetTiling(tilingData);

## ?.38. SetBias

功能说明

**EnableBias接口功能与该接口相同，建议使用EnableBias。**

设置Bias是否参与运算。

函数原型

```cpp
int32_t SetBias(bool isBiasIn = false)
```

参数说明

表6-1106参数说明

参数名输入/输出

描述

isBiasIn输入设置是否有Bias参与运算

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

无

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform);
 tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
```
