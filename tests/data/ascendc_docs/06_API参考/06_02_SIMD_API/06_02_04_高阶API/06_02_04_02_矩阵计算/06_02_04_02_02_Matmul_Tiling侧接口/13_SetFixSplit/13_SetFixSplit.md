# SetFixSplit

> **Section**: 13  
> **PDF Pages**: 2428–2428  

---

<!-- page 2428 -->

函数原型

```cpp
int32_t SetOrgShape(int32_t orgMIn, int32_t orgNIn, int32_t orgKIn)int32_t SetOrgShape(int32_t orgMIn, int32_t orgNIn, int32_t orgKaIn, int32_t orgKbIn)
```

参数说明

表6-1083参数说明

参数名输入/输出

描述

orgMIn输入设置原始完整的形状M大小，单位为元素。

orgNIn输入设置原始完整的形状N大小，单位为元素。

orgKIn输入设置原始完整的形状K大小，单位为元素。原始完整形状Ka=Kb时可设置。

orgKaIn输入设置矩阵A原始完整的形状Ka大小，单位为元素。

orgKbIn输入设置矩阵B原始完整的形状Kb大小，单位为元素。

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

参数orgKaIn和orgKbIn可以不相等，即原始矩阵形状Ka和Kb不相等，并不是实际Matmul计算时的K，此参数只用于辅助Matmul API搬运时的偏移计算。

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform); tiling.SetShape(1024, 1024, 1024);tiling.SetOrgShape(1024, 1024, 1024);  // 设置原始完整的形状

## ?.13. SetFixSplit

功能说明

设置固定的baseM、baseN、baseK，单位为元素个数。

函数原型

```cpp
int32_t SetFixSplit(int32_t baseMIn = -1, int32_t baseNIn = -1, int32_t baseKIn = -1)
```
