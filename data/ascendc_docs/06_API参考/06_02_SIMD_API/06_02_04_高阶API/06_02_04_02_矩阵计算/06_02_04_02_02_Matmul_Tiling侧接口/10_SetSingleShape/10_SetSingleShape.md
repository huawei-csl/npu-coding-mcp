# SetSingleShape

> **Section**: 10  
> **PDF Pages**: 2425–2425  

---

<!-- page 2425 -->

参数说明

表6-1080参数说明

参数名输入/输出

描述

pos输入Bias矩阵所在的buffer位置，可设置为：TPosition::GM,TPosition::VECOUT, TPosition::TSCM。

type输入Bias矩阵的数据格式，可设置为：CubeFormat::ND。

dataType输入Bias矩阵的数据类型，可设置为：DataType::DT_FLOAT/DataType::DT_FLOAT16/DataType::DT_INT32/DataType::DT_BFLOAT16 。

其中，仅在A、B的数据类型均为int8_t时，Bias的数据类型可以设置为int32_t。

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);  // 设置Bias矩阵

## ?.10. SetSingleShape

功能说明

设置Matmul单核计算的形状singleMIn，singleNIn，singleKIn，单位为元素。

函数原型

```cpp
int32_t SetSingleShape(int32_t singleMIn = -1, int32_t singleNIn = -1, int32_t singleKIn = -1)
```

参数说明

表6-1081参数说明

参数名输入/输出

描述

singleMIn输入设置的singleMIn大小，单位为元素，默认值为-1。-1表示不设置指定的singleMIn，该值由tiling函数自行计算。
