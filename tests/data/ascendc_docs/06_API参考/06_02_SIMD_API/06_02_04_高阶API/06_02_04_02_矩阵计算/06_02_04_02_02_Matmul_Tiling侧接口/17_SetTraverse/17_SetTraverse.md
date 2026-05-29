# SetTraverse

> **Section**: 17  
> **PDF Pages**: 2432–2432  

---

<!-- page 2432 -->

参数名输入/输出

描述

btSize输入设置Matmul计算时，能够使用的BiasTable Buffer大小，单位为字节。默认值-1，表示使用AI处理器BiasTable Buffer大小。

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); tiling.SetBufferSpace(-1, -1, -1, -1);  // 设置计算时可用的L1/L0C/UB/BT空间大小

## ?.17. SetTraverse

功能说明

设置固定的Matmul计算方向，M轴优先还是N轴优先。

函数原型

```cpp
int32_t SetTraverse(MatrixTraverse traverse)
```

参数说明

表6-1088参数说明

参数名输入/输出

描述

traverse输入设置固定的Matmul计算方向。可选值：MatrixTraverse::FIRSTM/MatrixTraverse::FIRSTN。

FIRSTM代表先往M轴方向偏移再往N轴方向偏移。

FIRSTN代表先往N轴方向偏移再往M轴方向偏移。

返回值说明

-1表示设置失败；0表示设置成功。

约束说明

无
