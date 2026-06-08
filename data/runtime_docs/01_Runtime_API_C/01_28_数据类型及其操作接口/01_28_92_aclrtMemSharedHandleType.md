# aclrtMemSharedHandleType

> **Section**: 1.28.92


typedef enum aclrtMemSharedHandleType {

```
ACL_MEM_SHARE_HANDLE_TYPE_DEFAULT = 0x1, ACL_MEM_SHARE_HANDLE_TYPE_FABRIC = 0x2, } aclrtMemSharedHandleType;
```

表 1-11 枚举项说明

| 枚举项                                | 说明                                                                                                  |
|------------------------------------|-----------------------------------------------------------------------------------------------------|
| ACL_MEM_SHARE_HANDLE _TYPE_DEFAULT | 默认值， AI Server 内跨进程共享内存。                                                                            |
| ACL_MEM_SHARE_HANDLE _TYPE_FABRIC  | 跨 AI Server 跨进程共享内存，包含一个 AI Server 内 的场景。 仅 Atlas A3 训练系列产品 /Atlas A3 推理系列产品支 持该选项。 其它产品型号当前不支持该选项。 |
