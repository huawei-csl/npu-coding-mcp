# aclrtIpcMemSetImportPid

> **Section**: 1.13.65


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

设置 IPC 共享内存的进程白名单。

本接口需与其它接口配合使用，以便实现内存共享的目的，配合使用流程请参见 aclrtIpcMemGetExportKey 接口处的说明。

aclError aclrtIpcMemSetImportPid(const char *key, int32\_t *pid, size\_t num)

| 参数名   | 输入 / 输 出   | 说明                                                                                                            |
|-------|------------|---------------------------------------------------------------------------------------------------------------|
| key   | 输入         | 通过 aclrtIpcMemGetExportKey 接口获取的内存 key 。                                                                      |
| pid   | 输入         | 用于存放白名单进程 ID 的数组。 进程 ID 可调用 aclrtDeviceGetBareTgid 接口获取， Docker 场景下获取到的是物理机上的进程 ID ，非 Docker 场景下获取 到的是进程 ID 。 |
| num   | 输入         | 白名单进程数量，与 pid 参数数组的大小保持一致。                                                                                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
