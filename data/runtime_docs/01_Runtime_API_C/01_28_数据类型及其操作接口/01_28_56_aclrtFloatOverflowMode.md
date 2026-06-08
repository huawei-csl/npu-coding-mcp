# aclrtFloatOverflowMode

> **Section**: 1.28.56


```
typedef enum aclrtFloatOverflowMode { ACL_RT_OVERFLOW_MODE_SATURATION = 0, // 溢出检测饱和模式 ACL_RT_OVERFLOW_MODE_INFNAN,         // 溢出检测 Inf/NaN 模式，默认值 ACL_RT_OVERFLOW_MODE_UNDEF, } aclrtFloatOverflowMode;
```

对比于 Inf/NaN 模式，饱和模式下，计算结果如果是 Inf ，最终结果是一个极大值；计 算结果如果是 NaN ，最终结果是 0 。若设置成饱和模式，计算精度可能存在误差，该模 式仅为兼容旧版本，后续不演进。

Atlas 350 加速卡不支持饱和模式。
