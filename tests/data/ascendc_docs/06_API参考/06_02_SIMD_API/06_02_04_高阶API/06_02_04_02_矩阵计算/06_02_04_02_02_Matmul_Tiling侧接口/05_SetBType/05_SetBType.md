# SetBType

> **Section**: 5  
> **PDF Pages**: 2420–2420  

---

<!-- page 2420 -->

参数名输入/输出

描述

isTrans输入A矩阵是否转置。

参数取值：

●true：A矩阵转置；

●false：A矩阵不转置。

Atlas 推理系列产品AI Core，A矩阵为DataType::DT_INT8数据类型时不支持转置，即不支持该参数设置为true。

返回值说明

-1表示设置失败；0表示设置成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); // 设置A矩阵，buffer位置为GM，数据格式为ND，数据类型为bfloat16，默认不转置tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);  tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);   tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);   tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);   tiling.SetShape(1024, 1024, 1024);   tiling.SetOrgShape(1024, 1024, 1024);  tiling.SetBias(true);   tiling.SetBufferSpace(-1, -1, -1);optiling::TCubeTiling tilingData;   int ret = tiling.GetTiling(tilingData);

## ?.5. SetBType

功能说明

设置B矩阵的位置，数据格式，数据类型，是否转置等信息，这些信息需要和kernel侧的设置保持一致。

函数原型

```cpp
int32_t SetBType(TPosition pos, CubeFormat type, DataType dataType, bool isTrans = false)
```
