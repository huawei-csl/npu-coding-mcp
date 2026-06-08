# aclrtServerPid

> **Section**: 1.28.107


```
typedef struct { uint32_t sdid; int32_t *pid; size_t num; } aclrtServerPid;
```

| 成员名称   | 说明                                                                                                                          |
|--------|-----------------------------------------------------------------------------------------------------------------------------|
| sdid   | 针对 Atlas A3 训练系列产品 /Atlas A3 推理系列产品中的 超节点产品， sdid （ SuperPOD Device ID ）表示超节点 产品中的 Device 唯一标识，可提前调用 aclGetDeviceInfo 接口获取。 |
| pid    | Host 侧进程 ID 白名单数组。                                                                                                          |
| num    | pid 数组长度。                                                                                                                   |
