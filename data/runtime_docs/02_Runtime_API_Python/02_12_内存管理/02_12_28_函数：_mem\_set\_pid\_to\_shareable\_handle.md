# 函数： mem\_set\_pid\_to\_shareable\_handle

> **Section**: 2.12.28


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
| Atlas 200I/500 A2 推理产品            | √      |

设置可共享内存的进程白名单，只有配置了白名单的进程才能用 acl.rt.mem\_export\_to\_shareable\_handle 接口导出的 shareable\_handle 。

本接口需与其它接口配合使用，以便实现内存共享的目的，请参见 acl.rt.mem\_export\_to\_shareable\_handle 接口处的说明。

## ● C 函数原型

aclError aclrtMemSetPidToShareableHandle(uint64\_t shareableHandle, int32\_t *pid, size\_t pidNum)

- python 函数
- ret = acl.rt.mem\_set\_pid\_to\_shareable\_handle(shareable\_handle, pid)

| 参数名               | 说明                                                                                                                        |
|-------------------|---------------------------------------------------------------------------------------------------------------------------|
| shareable_han dle | int ，通过 acl.rt.mem_export_to_shareable_handle 接口导出的 shareable_handle 。                                                    |
| pid               | list ，用于存放白名单进程 ID 的数组。 进程 ID 可调用 acl.rt.device_get_bare_tgid 接口获取， Docker 场 景下获取到的是物理机上的进程 ID ，非 Docker 场景下获取到的是 进程 ID 。 |

## 返回值说明

## 约束说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

在调用 aclrtMemExportToShareableHandle 接口的进程中，调用本接口设置进程白 名单。

Ascend RC 形态不支持调用本接口。
