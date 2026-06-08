# aclRecoverAllHcclTasks

> **Section**: 1.15.13


须知：本接口为预留接口，暂不支持。

维测场景下，本接口恢复指定 Device 上的所有集合通信任务。

aclError aclRecoverAllHcclTasks(int32\_t deviceId)

| 参数名      | 输入 / 输 出   | 说明                                                                                                    |
|----------|------------|-------------------------------------------------------------------------------------------------------|
| deviceId | 输入         | Device ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
