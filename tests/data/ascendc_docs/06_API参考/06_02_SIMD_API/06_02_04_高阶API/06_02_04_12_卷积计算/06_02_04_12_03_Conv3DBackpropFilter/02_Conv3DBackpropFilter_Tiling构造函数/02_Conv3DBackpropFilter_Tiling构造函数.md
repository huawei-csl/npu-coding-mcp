# Conv3DBackpropFilter Tiling构造函数

> **Section**: 2  
> **PDF Pages**: 3066–3066  

---

<!-- page 3066 -->

conv3dBpDwTiling.SetInputShape(n, c, d, h, w);conv3dBpDwTiling.SetWeightShape(cout, cin, d, h, w);conv3dBpDwTiling.SetPadding(padFront, padBack, padUp, padDown, padLeft, padRight);conv3dBpDwTiling.SetStride(strideD, strideH, strideW);conv3dBpDwTiling.SetDilation(dilationD, dilationH, dilationW);int ret = conv3dBpDwTiling.GetTiling(tilingData);    // 如果 ret = -1, 获取tiling 结果失败

需要包含的头文件

```cpp
#include "lib/conv_backprop/conv3d_bp_filter_tiling.h"
```

## ?.2. Conv3DBackpropFilter Tiling 构造函数

功能说明

用于创建一个Conv3DBackpropFilter 单核Tiling对象。

函数原型

●带参构造函数，需要传入硬件平台信息，推荐使用这类构造函数来获得更好的兼容性。

–使用PlatformAscendC类传入信息explicit Conv3dBpFilterTiling(const platform_ascendc::PlatformAscendC& ascendcPlatform)

–使用PlatformInfo传入信息

当platform_ascendc::PlatformAscendC无法在Tiling运行时获取时，需要用户自己构造PlatformInfo结构体，透传给Conv3dBpFilterTiling构造函数。explicit Conv3dBpFilterTiling(const PlatformInfo& platform)

●无参构造函数Conv3dBpFilterTiling()

●基类构造函数

Conv3dBpFilterTiling继承自基类Conv3dBpFilterTilingBase，其构造函数如下：

```cpp
Conv3dBpFilterTilingBase()explicit Conv3dBpFilterTilingBase(const platform_ascendc::PlatformAscendC& ascendcPlatform)explicit Conv3dBpFilterTilingBase(const PlatformInfo& platform)
```

参数说明

表6-1429参数说明

参数名输入/输出

描述

ascendcPlatform

输入传入硬件平台的信息，PlatformAscendC定义请参见6.4.2.1.2 构造及析构函数。
