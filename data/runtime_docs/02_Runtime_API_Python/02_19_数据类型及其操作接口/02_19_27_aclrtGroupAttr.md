# aclrtGroupAttr

> **Section**: 2.19.27


Atlas 200I/500 A2 推理产品，不支持该枚举值。

Atlas 训练系列产品，不支持该枚举值。

Atlas A2 训练系列产品 /Atlas A2 推理系列产品，不支持该枚举值。

Atlas A3 训练系列产品 /Atlas A3 推理系列产品，不支持该枚举值。

| 数据格式                       | 说明                                                                                  |
|----------------------------|-------------------------------------------------------------------------------------|
| ACL_GROUP_AICORE_ INT= 0   | 指定 Group 对应的 aicore 个数，属性值的数据类型为整 型。                                                |
| ACL_GROUP_AIV_INT = 1      | 指定 Group 对应的 vector core 个数，属性值的数据类型为 整型。                                           |
| ACL_GROUP_AIC_INT = 2      | 指定 Group 对应的 aicpu 线程数，属性值的数据类型为整 型。                                                |
| ACL_GROUP_SDMAN UM_INT = 3 | 内存异步拷贝的通道数，属性值的数据类型为整型。                                                             |
| ACL_GROUP_SDMAN UM_INT = 4 | 指定 Group 下可以被同时调度执行的 Stream 个数，小于或 等于 32 ，当前系统级最大一共可以同时调度 32 个 Stream 。属性值的数据类型为整型。 |
| ACL_GROUP_GROUPI D_INT = 5 | 指定 Group 的 ID 。属性值的数据类型为整型。                                                         |
