# SetCType

> **Section**: 8  
> **PDF Pages**: 2423–2423  

---

<!-- page 2423 -->

参数说明

表6-1078参数说明

参数名输入/输出

描述

scalePos输入scaleB矩阵的内存逻辑位置。

针对Atlas 350 加速卡，scaleB矩阵可设置为TPosition::GM，TPosition::VECOUT，TPosition::TSCM。

scaleType输入scaleB矩阵的物理排布格式，详细介绍请参考数据格式。

针对Atlas 350 加速卡，scaleB矩阵可设置为CubeFormat::ND，CubeFormat::NZ。

isScaleTrans

输入scaleB矩阵是否转置。参数支持的取值如下：

●true：默认值，scaleB矩阵转置；

●false：scaleB矩阵不转置。

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);  // 设置scaleB矩阵，buffer位置为GM，数据格式为ND，转置tiling.SetScaleBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, true);

## ?.8. SetCType

功能说明

设置C矩阵的位置，数据格式，数据类型等信息，这些信息需要和kernel侧的设置保持一致。

函数原型

```cpp
int32_t SetCType(TPosition pos, CubeFormat type, DataType dataType)
```
