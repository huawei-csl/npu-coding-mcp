# MatmulGetTmpBufSize

> **Section**: 5  
> **PDF Pages**: 2463–2463  

---

<!-- page 2463 -->

## ?.5. MatmulGetTmpBufSize

功能说明

本接口用于在调用GetTiling接口获取Tiling参数后，根据Tiling结构体信息获取L1Buffer/Unified Buffer/L0C Buffer的使用大小。

函数原型

```cpp
int32_t MatmulGetTmpBufSize(optiling::TCubeTiling &tiling, matmul_tiling::SysTilingTempBufSize &bufSize)
```

参数说明

表6-1113参数说明

参数名输入/输出

描述

tiling输入Matmul单核Tiling的结构体，即MatmulTiling对象得到的TCubeTiling结构体。

bufSize输出Tiling中L1 Buffer/Unified Buffer/L0C Buffer的使用大小。

SysTilingTempBufSize结构定义如下方代码所示。

struct SysTilingTempBufSize {    int32_t ubSize = 0; // Unified Buffer大小    int32_t l1Size = 0; // L1 Buffer大小    int32_t l0cSize = 0; // L0C Buffer大小};

返回值说明

-1表示获取失败； 0表示获取成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); optiling::TCubeTiling tilingData;...  // 初始化tilingData，详见MatmulTiling类使用说明int ret = tiling.GetTiling(tilingData);    // 获取Tiling参数SysTilingTempBufSize bufSize;MatmulGetTmpBufSize(tilingData, bufSize);

## ?.6. MatmulGetTmpBufSizeV2

功能说明

单核Matmul Tiling调用GetTiling接口获取Tiling参数后，根据Tiling结构体信息获取L1 Buffer/Unified Buffer/L0C Buffer的使用大小。
