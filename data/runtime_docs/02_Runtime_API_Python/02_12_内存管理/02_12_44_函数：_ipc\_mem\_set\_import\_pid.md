# 函数： ipc\_mem\_set\_import\_pid

> **Section**: 2.12.44


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | x      |

设置 IPC 共享内存的进程白名单，只有配置了白名单的进程才能用 acl.rt.ipc\_mem\_get\_export\_key 接口导出的 key 。

本接口需与其它接口配合使用，以便实现内存共享的目的，配合使用流程请参见 acl.rt.ipc\_mem\_get\_export\_key 接口处的说明。

- C 函数原型 aclError aclrtIpcMemSetImportPid(const char *key, int32\_t *pid, size\_t num)
- python 函数
- ret = acl.rt.ipc\_mem\_set\_import\_pid(key, pid)

| 参数名   | 说明                                                                                                                       |
|-------|--------------------------------------------------------------------------------------------------------------------------|
| key   | str ，共享内存 key 。                                                                                                          |
| pids  | list ，用于存放白名单进程 ID 的数组。 进程 ID 可调用 acl.rt.device_get_bare_tgid 接口获取， Docker 场景 下获取到的是物理机上的进程 ID ，非 Docker 场景下获取到的是进程 ID 。 |

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其它值表示失败。 |
