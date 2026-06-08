# 函数： device\_get\_bare\_tgid

> **Section**: 2.12.27


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取当前进程的进程 ID 。

本接口内部在获取进程 ID 时已适配物理机、虚拟机场景，用户只需调用本接口获取进 程 ID ，再配置其它接口使用（配合流程请参见

acl.rt.mem\_export\_to\_shareable\_handle ），达到物理内存共享的目的。若用户不 调用本接口、自行获取进程 ID ，可能会导致后续使用进程 ID 异常。

- C 函数原型

aclError aclrtDeviceGetBareTgid(int32\_t *pid)

- python 函数

pid, ret = acl.rt.device\_get\_bare\_tgid()

无

| 返回值   | 说明                            |
|-------|-------------------------------|
| pid   | int ，进程 ID 。                  |
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
