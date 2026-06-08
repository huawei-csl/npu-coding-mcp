# aclrtRepairError

> **Section**: 1.15.15


须知：本接口为预留接口，暂不支持。

基于 aclrtGetErrorVerbose 接口获取的详细信息进行故障恢复，此接口应该在提交任 务中止之后调用。

aclError aclrtRepairError(int32\_t deviceId, const aclrtErrorInfo *errorInfo)

## 参数说明

## 返回值说明

| 参数名       | 输入 / 输 出   | 说明                                                    |
|-----------|------------|-------------------------------------------------------|
| deviceId  | 输入         | Device ID 。 与 aclrtSetDevice 接口中 Device ID 保持一致。      |
| errorInfo | 输入         | 错误信息。 aclrtErrorInfo 结构体的描述请参见 aclrtGetErrorVerbose 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
