# SetBiasType

> **Section**: 9  
> **PDF Pages**: 2424–2424  

---

<!-- page 2424 -->

参数说明

表6-1079参数说明

参数名输入/输出

描述

pos输入C矩阵所在的buffer位置，可设置为：TPosition::GM,TPosition::VECIN。

type输入C矩阵的数据格式，可设置为：CubeFormat::ND，CubeFormat::NZ, CubeFormat::ND_ALIGN。

dataType输入C矩阵的数据类型，可设置为：DataType::DT_FLOAT/DataType::DT_FLOAT16/DataType::DT_BFLOAT16 /DataType::DT_INT8/DataType::DT_INT32/DataType::DT_FLOAT8_E4M3FN/DataType::DT_HIFLOAT8。

返回值说明

-1表示设置失败；0表示设置成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); // 设置C矩阵，buffer位置为GM，数据格式为ND，数据类型为float，默认不转置tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);

## ?.9. SetBiasType

功能说明

设置Bias的位置，数据格式，数据类型等信息，这些信息需要和kernel侧的设置保持一致。

函数原型

```cpp
int32_t SetBiasType(TPosition pos, CubeFormat type, DataType dataType)
```
