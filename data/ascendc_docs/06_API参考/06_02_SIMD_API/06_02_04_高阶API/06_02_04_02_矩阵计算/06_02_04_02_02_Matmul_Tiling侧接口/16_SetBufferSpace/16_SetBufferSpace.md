# SetBufferSpace

> **Section**: 16  
> **PDF Pages**: 2431–2431  

---

<!-- page 2431 -->

参数说明

表6-1086参数说明

参数名输入/输出

描述

isBiasIn输入设置是否有Bias参与运算。

true：有Bias参与运算。

false：无Bias参与运算。

返回值说明

-1表示设置失败；0表示设置成功。

约束说明

无

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); tiling.EnableBias(true);  // 设置Bias是否参与运算

## ?.16. SetBufferSpace

功能说明

设置Matmul计算时可用的L1 Buffer/L0C Buffer/Unified Buffer/BiasTable Buffer空间大小，单位为字节。

函数原型

```cpp
int32_t SetBufferSpace(int32_t l1Size = -1, int32_t l0CSize = -1, int32_t ubSize = -1, int32_t btSize = -1)
```

参数说明

表6-1087参数说明

参数名输入/输出

描述

l1Size输入设置Matmul计算时，能够使用的L1 Buffer大小，单位为字节。默认值-1，表示使用AI处理器L1 Buffer大小。

l0CSize输入设置Matmul计算时，能够使用的L0C Buffer大小，单位为字节。默认值-1，表示使用AI处理器L0C Buffer大小。

ubSize输入设置Matmul计算时，能够使用的UB Buffer大小，单位为字节。默认值-1，表示使用AI处理器UB Buffer大小。
