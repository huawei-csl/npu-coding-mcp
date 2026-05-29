# SetMadType

> **Section**: 18  
> **PDF Pages**: 2433–2433  

---

<!-- page 2433 -->

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); tiling.SetTraverse(MatrixTraverse::FIRSTM);  // 设置遍历方式

## ?.18. SetMadType

功能说明

设置是否使能HF32模式。当前版本暂不支持。

对于Atlas 350 加速卡，本接口可用于设置是否使能HF32模式（当前版本暂不支持）、设置是否使能MxMatmul场景。在MxMatmul场景，必须调用该接口并配置为使能MxMatmul场景，从而保证该场景下正确计算并返回Tiling参数。

函数原型

```cpp
int32_t SetMadType(MatrixMadType madType)
```

参数说明

表6-1089参数说明

参数名输入/输出

描述

madType输入设置Matmul模式。MatrixMadType类型，定义如下方代码所示，其中参数的含义为：

MatrixMadType::NORMAL：普通模式，即非HF32模式、非MxMatmul场景。

MatrixMadType::HF32：使能HF32模式。

MatrixMadType::MXMODE：使能MxMatmul场景。该参数仅在Atlas 350 加速卡上支持。

```cpp
enum class MatrixMadType : int32_t {NORMAL = 0,HF32 = 1, MXMODE = 2,};
```

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

无

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform);
```
