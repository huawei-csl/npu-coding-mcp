# aclrtGroupAttr

> **Section**: 1.28.59


```
typedef enum aclrtGroupAttr { ACL_GROUP_AICORE_INT,     // 指定 Group 对应的 AI Core 个数，属性值的数据类型为整型 ACL_GROUP_AIV_INT,       // 指定 Group 对应的 Vector Core 个数，属性值的数据类型为整型 ACL_GROUP_AIC_INT,       // 指定 Group 对应的 AI CPU 线程数，属性值的数据类型为整型 ACL_GROUP_SDMANUM_INT,   // 内存异步拷贝的通道数，属性值的数据类型为整型 ACL_GROUP_ASQNUM_INT,    // 指定 Group 下可以被同时调度执行的 Stream 个数，小于或等于 32 ，当前系统 级最大一共可以同时调度 32 个 Stream ，属性值的数据类型为整型 ACL_GROUP_GROUPID_INT    // 指定 Group 的 ID ，属性值的数据类型为整型 } aclrtGroupAttr;
```

在 Atlas 推理系列产品的 Control CPU 开放形态下，仅支持配置 ACL\_GROUP\_AICORE\_INT 、 ACL\_GROUP\_GROUPID\_INT 。
