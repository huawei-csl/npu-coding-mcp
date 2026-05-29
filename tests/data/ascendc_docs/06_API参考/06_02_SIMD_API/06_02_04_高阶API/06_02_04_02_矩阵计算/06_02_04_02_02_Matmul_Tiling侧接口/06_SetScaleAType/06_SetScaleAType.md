# SetScaleAType

> **Section**: 6  
> **PDF Pages**: 2421–2421  

---

<!-- page 2421 -->

参数说明

表6-1076参数说明

参数名输入/输出

描述

pos输入B矩阵所在的buffer位置，可设置为：TPosition::GM,TPosition::VECOUT, TPosition::TSCM。

type输入B矩阵的数据格式，可设置为：CubeFormat::ND，CubeFormat::NZ。

dataType输入B矩阵的数据类型，可设置为：DataType::DT_FLOAT/DataType::DT_FLOAT16/DataType::DT_BFLOAT16 /DataType::DT_INT8/DataType::DT_INT4/DataType::DT_FLOAT8_E4M3FN/DataType::DT_FLOAT8_E5M2/DataType::DT_HIFLOAT8。

isTrans输入B矩阵是否转置。

参数取值：

●true：B矩阵转置；

●false：B矩阵不转置。

返回值说明

-1表示设置失败；0表示设置成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); // 设置B矩阵，buffer位置为GM，数据格式为ND，数据类型为bfloat16，默认不转置tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);

## ?.6. SetScaleAType

功能说明

**MxMatmul场景，设置scaleA矩阵的位置、数据格式、是否转置等信息，这些信息需要和Kernel侧的设置保持一致。如果不调用本接口，scaleA矩阵的信息将与SetAType中设置的A矩阵的信息保持一致。**

函数原型

```cpp
int32_t SetScaleAType(TPosition scalePos, CubeFormat scaleType, bool isScaleTrans = false)
```
