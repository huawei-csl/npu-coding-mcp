# SetSingleWeightShape

> **Section**: 7  
> **PDF Pages**: 3019–3019  

---

<!-- page 3019 -->

约束说明

无

调用示例

// 实例化Conv3D Apiauto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());Conv3dTilingApi::Conv3dTiling conv3dApiTiling(ascendcPlatform);conv3dApiTiling.SetOrgInputShape(orgCi, orgDi, orgHi, orgWi);

## ?.7. SetSingleWeightShape

功能说明

设置单核上权重矩阵Weight的形状。

函数原型

```cpp
void SetSingleWeightShape(int64_t singleCi, int64_t singleKd, int64_t singleKh, int64_t singleKw)
```

参数说明

参数名输入/输出描述

singleCi输入单核上输入通道的大小。

singleKd输入单核上Weight D维度大小。

singleKh输入单核上Weight H维度大小。

singleKw输入单核上Weight W维度大小。

返回值说明

无

约束说明

无

调用示例

// 实例化Conv3D Apiauto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());Conv3dTilingApi::Conv3dTiling conv3dApiTiling(ascendcPlatform );conv3dApiTiling.SetSingleWeightShape(singleCi, singleKd, singleKh, singleKw);

## ?.8. SetSingleOutputShape

功能说明

设置单核上结果矩阵Output的形状。
