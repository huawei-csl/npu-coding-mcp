# aclrtRandomNumTaskInfo

> **Section**: 1.28.102


```
typedef struct { aclDataType dataType; aclrtRandomNumFuncParaInfo randomNumFuncParaInfo; void *randomParaAddr; void *randomResultAddr; void *randomCounterAddr; aclrtRandomParaInfo randomSeed; aclrtRandomParaInfo randomNum; uint8_t rsv[8]; } aclrtRandomNumTaskInfo;
```

| 成员名称                   | 说明                                                                                                                              |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| dataType               | 随机数数据类型。类型定义请参见 aclDataType 。 仅支持如下数据类型： ACL_INT32 、 ACL_INT64 、 ACL_UINT32 、 ACL_UINT64 、 ACL_BF16 、 ACL_FLOAT16 、 ACL_FLOAT 。 |
| randomNumFuncParaIn fo | 随机数函数信息，包括函数类别、参数信息。类型定义 请参见 aclrtRandomNumFuncParaInfo 。                                                                       |

| 成员名称              | 说明                                                                                              |
|-------------------|-------------------------------------------------------------------------------------------------|
| randomParaAddr    | 此处传 NULL 时，由接口内部自行申请 Device 内存，存放 randomNumFuncParaInfo 参数中的数据；否则，由用户 申请 Device 内存，将内存地址作为参数传入。 |
| randomResultAddr  | 存放随机数结果的内存地址。 由用户提前申请 Device 内存，将内存地址作为参数传 入。                                                   |
| randomCounterAddr | 生成随机数的偏移量。 由用户提前申请 Device 内存，读入偏移量数据后，再将 内存地址作为参数传入                                             |
| randomSeed        | 随机种子。类型定义请参见 aclrtRandomParaInfo 。                                                              |
| randomNum         | 随机数个数。类型定义请参见 aclrtRandomParaInfo 。                                                             |
| rsv               | 预留参数。当前固定配置为 0 。                                                                                |
