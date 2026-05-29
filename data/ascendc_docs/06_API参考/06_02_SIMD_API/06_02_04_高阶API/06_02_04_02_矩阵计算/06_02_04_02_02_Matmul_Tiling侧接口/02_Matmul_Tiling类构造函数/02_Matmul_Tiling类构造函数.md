# Matmul Tiling类构造函数

> **Section**: 2  
> **PDF Pages**: 2411–2412  

---

<!-- page 2411 -->

接口功能

GetCoreNum

获得多核切分后，使用的numBlocks。

SetSplitK多核场景，使能切K轴。建议使用EnableMultiCoreSplitK接口。

EnableMultiCoreSplitK

多核场景，使能切K轴。

表6-1070 BatchMatmulTiling 其他接口

接口功能

GetCoreNum

获得多核切分后，使用的numBlocks。

需要包含的头文件

●Matmul单核Tiling#include "lib/matmul/matmul_tiling.h"

●Matmul多核Tiling#include "lib/matmul/bmm_tiling.h"

●BatchMatmul Tiling#include "lib/matmul/bmm_tiling.h"

## ?.2. Matmul Tiling 类构造函数

功能说明

用于创建一个Matmul单核Tiling对象，或者多核Tiling对象，或者BatchMatmul Tiling对象。

函数原型

●带参构造函数，需要传入硬件平台信息，推荐使用这类构造函数来获得更好的兼容性。

–使用PlatformAscendC类传入信息explicit MatmulApiTiling(const platform_ascendc::PlatformAscendC& ascendcPlatform)explicit MultiCoreMatmulTiling(const platform_ascendc::PlatformAscendC& ascendcPlatform)explicit BatchMatmulTiling(const platform_ascendc::PlatformAscendC &ascendcPlatform)

–使用PlatformInfo传入信息

当platform_ascendc::PlatformAscendC无法在Tiling运行时获取时，需要用户自行构造PlatformInfo结构体，透传给MatmulApiTiling构造函数。explicit MatmulApiTiling(const PlatformInfo& platform)explicit MultiCoreMatmulTiling(const PlatformInfo &platform)

●无参构造函数MatmulApiTiling()MultiCoreMatmulTiling()BatchMatmulTiling()

无参构造函数只支持如下产品型号：

<!-- page 2412 -->

Atlas A2训练系列产品/Atlas 800I A2推理产品

Atlas A3 训练系列产品

●基类构造函数

MatmulApiTiling、MultiCoreMatmulTiling和BatchMatmulTiling都继承自基类MatmulApiTilingBase，其构造函数如下：

```cpp
MatmulApiTilingBase()explicit MatmulApiTilingBase(const platform_ascendc::PlatformAscendC& ascendcPlatform)explicit MatmulApiTilingBase(const PlatformInfo& platform)
```

参数说明

表6-1071参数说明

参数名输入/输出

描述

ascendcPlatform

输入传入硬件平台的信息，PlatformAscendC定义请参见6.4.2.1.2 构造及析构函数。

platform输入传入硬件版本以及AI Core中各个硬件单元提供的内存大小。PlatformInfo构造时通过6.4.2.1.2 构造及析构函数获取。

PlatformInfo结构定义如下，socVersion通过6.4.2.1.4GetSocVersion获取并透传，各类硬件存储空间大小通过6.4.2.1.11 GetCoreMemSize获取并透传。struct PlatformInfo {    platform_ascendc::SocVersion socVersion;    uint64_t l1Size = 0;    uint64_t l0CSize = 0;    uint64_t ubSize = 0;    uint64_t l0ASize = 0;    uint64_t l0BSize = 0;};

不推荐通过直接填值构造PlatformInfo的方式调用构造函数，例如PlatformInfo(socVersion, 1024, 1024, ..);

在实现Host侧的Tiling函数时，platform_ascendc::PlatformAscendC用于获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。PlatformAscendC类提供获取这些平台信息的功能。

和platform_ascendc::PlatformAscendC不同的是，PlatformInfo则用于获取芯片版本、AI Core中各个硬件单元提供的内存大小等只针对单个AI Core的信息。

约束说明

无

使用样例

●无参构造函数// 单核Tilingmatmul_tiling::MatmulApiTiling tiling;tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
