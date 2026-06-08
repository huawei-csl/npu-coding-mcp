# aclrtFloatOverflowMode

> **Section**: 2.19.26


| 数据格式                                 | 说明                                                              |
|--------------------------------------|-----------------------------------------------------------------|
| ACL_RT_OVERFLOW_MODE_S ATURATION = 0 | 饱和模式，设置成该模式，计算精度可能存在误 差。该模式仅为兼容旧版本，后续不演进。 Atlas 350 加速卡不支持饱和模式。 |
| ACL_RT_OVERFLOW_MODE_I NFNAN = 1     | Inf/NaN 模式（符合 IEEE 754 标准），默认值。                                 |
| ACL_RT_OVERFLOW_MODE_U NDEF = 2      | 预留参数。                                                           |
