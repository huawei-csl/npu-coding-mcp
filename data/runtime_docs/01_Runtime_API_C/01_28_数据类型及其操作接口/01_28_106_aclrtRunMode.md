# aclrtRunMode

> **Section**: 1.28.106


```
typedef enum aclrtRunMode { ACL_DEVICE, ACL_HOST, } aclrtRunMode;
```

## 表 1-12 枚举项说明

| 枚举项        | 说明                                                                                                                                                                     |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_DEVICE | AI 软件栈运行在 Device 的 Control CPU 或板端环境 上。 Atlas 350 加速卡，不支持该选项。 Atlas A3 训练系列产品 /Atlas A3 推理系列产品，不 支持该选项。 Atlas A2 训练系列产品 /Atlas A2 推理系列产品，不 支持该选项。 Atlas 训练系列产品，不支持该选项。 |
| ACL_HOST   | AI 软件栈运行在 Host CPU 上。                                                                                                                                                  |
