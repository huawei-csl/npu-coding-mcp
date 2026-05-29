# SetDequantType

> **Section**: 31  
> **PDF Pages**: 2445–2445  

---

<!-- page 2445 -->

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform); tiling.SetDim(1);tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);   tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);   tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);   tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);   tiling.SetShape(1024, 1024, 1024);   tiling.SetAlignSplit(-1, 64, -1);  // 设置singleCoreM/singleCoreN/singleCoreK的对齐值tiling.SetOrgShape(1024, 1024, 1024);tiling.SetBias(true);   tiling.SetBufferSpace(-1, -1, -1);optiling::TCubeTiling tilingData;   int ret = tiling.GetTiling(tilingData);

## ?.31. SetDequantType

功能说明

该接口用于设置量化或反量化的模式。

Matmul反量化场景：在Matmul计算时，左、右矩阵的输入为int8_t或int4b_t类型，输出为half类型；或者左、右矩阵的输入为int8_t类型，输出为int8_t类型。该场景下，输出C矩阵的数据从CO1搬出到Global Memory时，会执行反量化操作，将最终结果反量化为对应的half或int8_t类型。

Matmul量化场景：在Matmul计算时，左、右矩阵的输入为half或bfloat16_t类型，输出为int8_t类型。该场景下，输出C矩阵的数据从CO1搬出到Global Memory时，会执行量化操作，将最终结果量化为int8_t类型。

量化或反量化时有两种模式：一种是同一系数的量化/反量化模式，一种是向量的量化/反量化模式。

●同一系数的量化或反量化模式：对输出矩阵的所有值采用同一系数进行量化或反量化。

●向量的量化或反量化模式：提供一个参数向量，对输出矩阵的每一列都采用该向量中对应列的系数进行量化或反量化。

函数原型

```cpp
int32_t SetDequantType(DequantType dequantType)
```
