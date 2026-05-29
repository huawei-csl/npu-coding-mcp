# SetScaleBType

> **Section**: 7  
> **PDF Pages**: 2422–2422  

---

<!-- page 2422 -->

参数说明

表6-1077参数说明

参数名输入/输出

描述

scalePos输入scaleA矩阵的内存逻辑位置。

针对Atlas 350 加速卡，scaleA矩阵可设置为TPosition::GM，TPosition::VECOUT，TPosition::TSCM。

scaleType输入scaleA矩阵的物理排布格式，详细介绍请参考数据格式。

针对Atlas 350 加速卡，scaleA矩阵可设置为CubeFormat::ND，CubeFormat::NZ。

isScaleTrans

输入scaleA矩阵是否转置。参数支持的取值如下：

●true：scaleA矩阵转置；

●false：默认值，scaleA矩阵不转置。

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);  // 设置scaleA矩阵，buffer位置为GM，数据格式为ND，不转置tiling.SetScaleAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, false);

## ?.7. SetScaleBType

功能说明

**MxMatmul场景，设置scaleB矩阵的位置、数据格式、是否转置等信息，这些信息需要和Kernel侧的设置保持一致。如果不调用本接口，scaleB矩阵的信息将与SetBType中设置的B矩阵的信息保持一致。**

函数原型

```cpp
int32_t SetScaleBType(TPosition scalePos, CubeFormat scaleType, bool isScaleTrans = true)
```
