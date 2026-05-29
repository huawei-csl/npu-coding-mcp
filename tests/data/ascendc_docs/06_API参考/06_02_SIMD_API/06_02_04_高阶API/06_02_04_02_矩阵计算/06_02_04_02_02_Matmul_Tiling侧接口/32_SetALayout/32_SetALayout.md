# SetALayout

> **Section**: 32  
> **PDF Pages**: 2446–2447  

---

<!-- page 2446 -->

参数说明

表6-1098参数说明

参数名输入/输出

描述

**dequantType**

输入设置量化或反量化时的模式。DequantType类型，该类型的定义如下方代码所示，其中参数的取值及含义如下：

●SCALAR：表示同一系数的量化或反量化模式。

●TENSOR：表示向量的量化或反量化模式。

```cpp
enum class DequantType {    SCALAR = 0,    TENSOR = 1,};
```

返回值说明

-1表示设置失败；0表示设置成功。

约束说明

本接口支持的同一系数的量化/反量化模式、向量的量化/反量化模式分别与Kernel侧接口SetQuantScalar和SetQuantVector对应，本接口设置的量化/反量化模式必须与Kernel侧使用的接口保持一致。

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_INT8);tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_INT8);   tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_INT32);   tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_INT32);   tiling.SetShape(M, N, K);   tiling.SetOrgShape(M, N, K);tiling.EnableBias(true);tiling.SetDequantType(DequantType::SCALAR);  // 设置同一系数的量化/反量化模式// tiling.SetDequantType(DequantType::TENSOR);  // 设置向量的量化/反量化模式tiling.SetBufferSpace(-1, -1, -1);optiling::TCubeTiling tilingData;   int ret = tiling.GetTiling(tilingData);

## ?.32. SetALayout

功能说明

设置A矩阵的Layout轴信息，包括B、S、N、G、D轴。对于BSNGD、SBNGD、BNGS1S2 Layout格式，调用IterateBatch接口之前，需要在Host侧Tiling实现中通过本接口设置A矩阵的Layout轴信息。

<!-- page 2447 -->

函数原型

```cpp
int32_t SetALayout(int32_t b, int32_t s, int32_t n, int32_t g, int32_t d)
```

参数说明

表6-1099参数说明

参数名输入/输出

描述

b输入A矩阵Layout的B轴信息

s输入A矩阵Layout的S轴信息

n输入A矩阵Layout的N轴信息

g输入A矩阵Layout的G轴信息

d输入A矩阵Layout的D轴信息

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

对于BSNGD、SBNGD、BNGS1S2 Layout格式，调用IterateBatch接口之前，需要在Host侧Tiling实现中通过本接口设置A矩阵的Layout轴信息。

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform);
   int32_t M = 32;int32_t N = 256;int32_t K = 64;tiling.SetDim(1);tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);tiling.SetShape(M, N, K);tiling.SetOrgShape(M, N, K);tiling.SetBias(true);tiling.SetBufferSpace(-1, -1, -1);
constexpr int32_t A_BNUM = 2;constexpr int32_t A_SNUM = 32;constexpr int32_t A_GNUM = 3;constexpr int32_t A_DNUM = 64;constexpr int32_t B_BNUM = 2;constexpr int32_t B_SNUM = 256;constexpr int32_t B_GNUM = 3;constexpr int32_t B_DNUM = 64;constexpr int32_t C_BNUM = 2;
```
