# 函数： notify\_set\_import\_pid

> **Section**: 2.11.8


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | x      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | x      |

设置共享 Notify 的进程白名单，只有配置了白名单的进程才能使用 acl.rt.notify\_get\_export\_key 接口导出的 Notify 共享名称。

- C 函数原型

aclError aclrtNotifySetImportPid(aclrtNotify notify, int32\_t *pid, size\_t num)

- python 函数

ret = acl.rt.notify\_set\_import\_pid(notify, pid)

| 参数名    | 说明                                                                   |
|--------|----------------------------------------------------------------------|
| notify | int ，指定 Notify 指针地址，与 acl.rt.notify_get_export_key 接口中的 Notify 保持一致。 |

## 返回值说明

## 约束说明

| 参数名   | 说明                                                                                                                                                   |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| pid   | list ，用于存放白名单进程 ID 的列表。 定义： pid=[pid_1, pid_2, ...] 进程 ID 可调用 acl.rt.device_get_bare_tgid 接口获取， Docker 场景下 获取到的是物理机上的进程 ID ，非 Docker 场景下获取到的是进程 ID 。 |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |

昇 腾虚拟化实例场景不支持该操作。
