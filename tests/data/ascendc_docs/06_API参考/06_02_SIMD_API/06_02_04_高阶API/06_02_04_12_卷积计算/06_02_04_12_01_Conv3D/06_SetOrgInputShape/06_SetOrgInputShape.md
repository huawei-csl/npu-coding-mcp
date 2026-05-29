# SetOrgInputShape

> **Section**: 6  
> **PDF Pages**: 3018–3018  

---

<!-- page 3018 -->

参数说明

参数名输入/输出描述

orgCo输入原始输出通道的大小。

orgKd输入原始Weight D维度大小。

orgKh输入原始Weight H维度大小。

orgKw输入原始Weight W维度大小。

返回值说明

无

约束说明

无

调用示例

// 实例化Conv3D Apiauto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());Conv3dTilingApi::Conv3dTiling conv3dApiTiling(ascendcPlatform);conv3dApiTiling.SetOrgWeightShape(cout, kd, kh, kw);

## ?.6. SetOrgInputShape

功能说明

设置特征矩阵Input的原始形状。

函数原型

```cpp
void SetOrgInputShape(int64_t orgCi, int64_t orgDi, int64_t orgHi, int64_t orgWi)
```

参数说明

参数名输入/输出描述

orgCi输入原始输入通道的大小。

orgDi输入原始Input D维度大小。

orgHi输入原始Input H维度大小。

orgWi输入原始Input W维度大小。

返回值说明

无
