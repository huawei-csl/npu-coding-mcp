# aclrtNotifySetImportPid

> **Section**: 1.10.8


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

设置共享 Notify 的进程白名单。

本接口需与其它接口配合使用，以便实现多 Device 上不同进程间的任务同步，请参见 1.10.7 aclrtNotifyGetExportKey 接口处的说明。

aclError aclrtNotifySetImportPid(aclrtNotify notify, int32\_t *pid, size\_t num)

| 参数名    | 输入 / 输 出   | 说明                                                                                                            |
|--------|------------|---------------------------------------------------------------------------------------------------------------|
| notify | 输入         | 指定 Notify 。类型定义请参见 aclrtNotify 。 与 aclrtNotifyGetExportKey 接口中的 Notify 保持一致。                                  |
| pid    | 输入         | 用于存放白名单进程 ID 的数组。 进程 ID 可调用 aclrtDeviceGetBareTgid 接口获取， Docker 场景下获取到的是物理机上的进程 ID ，非 Docker 场景下获取 到的是进程 ID 。 |
| num    | 输入         | 白名单进程数量，与 pid 参数数组的大小保持一致。                                                                                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

昇 腾虚拟化实例场景不支持该操作。
