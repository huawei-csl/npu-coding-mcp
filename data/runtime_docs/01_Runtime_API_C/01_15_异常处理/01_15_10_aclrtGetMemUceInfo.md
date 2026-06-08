# aclrtGetMemUceInfo

> **Section**: 1.15.10


须知：本接口为预留接口，暂不支持。

获取内存 UCE （ Uncorrectable Error ，指系统硬件不能直接处理恢复内存错误）的错误 虚拟地址。

aclError aclrtGetMemUceInfo(int32\_t deviceId, aclrtMemUceInfo *memUceInfoArray, size\_t arraySize, size\_t *retSize)

| 参数名              | 输入 / 输 出   | 说明                                               |
|------------------|------------|--------------------------------------------------|
| deviceId         | 输入         | Device ID 。 与 aclrtSetDevice 接口中 Device ID 保持一致。 |
| memUceInf oArray | 输入 & 输 出   | aclrtMemUceInfo 数组的指针。类型定义请参见 aclrtMemUceInfo 。  |
| arraySize        | 输入         | 传入 aclrtMemUceInfo 数组的长度。                        |
| retSize          | 输出         | 实际返回的 aclrtMemUceInfo 数组的有效长度。                   |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
