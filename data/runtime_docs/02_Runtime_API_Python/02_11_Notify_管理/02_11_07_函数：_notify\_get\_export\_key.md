# 函数： notify\_get\_export\_key

> **Section**: 2.11.7


## 产品支持情况

## 功能说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | x      |

将本进程中指定 Notify 设置为 IPC （ Inter-Process Communication ） Notify ，并返回 key （即 Notify 共享名称），用于在多 Device 上不同进程间实现任务同步，调用本接口 前，需调用 acl.rt.device\_enable\_peer\_access 接口开启两个 Device 之间的数据交互。

本接口需与以下其它关键接口配合使用，以便实现多 Device 上不同进程间的任务同 步，此处以 Device 0 上的 A 进程、 Device 1 上的 B 进程为例，说明两个进程间的任务同 步接口调用流程 :

1. 在 A 进程中：

## 函数原型

## 参数说明

## 返回值说明

- a. 调用 acl.rt.create\_notify 接口创建 Notify 。
- b. 调用 acl.rt.notify\_get\_export\_key 接口导出 key （即 Notify 共享名称）。
- c. 获取 B 进程的进程 ID ，并调用 acl.rt.notify\_set\_import\_pid 接口，将 B 进程的 进程 ID 设置为白名单。
- d. 调用 acl.rt.wait\_and\_reset\_notify 接口下发等待任务。
- e. 调用 acl.rt.destroy\_notify 接口销毁 Notify 。涉及 IPC Notify 的进程都需要释 放 Notify ，所有涉及 IPC Notify 的进程都完成释放操作， Notify 才真正释放。

## 2. 在 B 进程中：

- a. 调用 acl.rt.device\_get\_bare\_tgid 接口，获取 B 进程的进程 ID 。本接口内部在 获取进程 ID 时已适配物理机、虚拟机场景，用户只需调用本接口获取进程 ID ，再配合其它接口使用，达到内存共享的目的。若用户不调用本接口、自 行获取进程 ID ，可能会导致后续使用进程 ID 异常。
- b. 调用 acl.rt.notify\_import\_by\_key 获取 key 的信息，并返回本进程可以使用的 Notify 指针。在调用 acl.rt.notify\_import\_by\_key 接口前，需确保 IPC Notify ，不能提前释放。
- c. 调用 acl.rt.record\_notify 接口下发 Record 任务。
- d. 调用 acl.rt.destroy\_notify 接口销毁 Notify 。

## ● C 函数原型

aclError aclrtNotifyGetExportKey(aclrtNotify notify, char *key, size\_t len, uint64\_t flag)

## ● python 函数

key, ret = acl.rt.notify\_get\_export\_key(notify, len, flags)

| 参数名    | 说明                                                                                                                                                                                                                                                                |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| notify | int ，指定 Notify 指针地址。                                                                                                                                                                                                                                              |
| len    | int ， Notify 共享名称的长度，最小长度为 65 。                                                                                                                                                                                                                                   |
| flags  | int ，是否启用进程白名单校验。取值如下： ● 0 ： ACL_RT_NOTIFY_EXPORT_FLAG_DEFAULT ，默认值，启用进 程白名单校验。 配置为该值时，需单独调用 aclrtNotifySetImportPid 接口将使用 Notify 共享名称的进程 ID 设置为白名单。 ● 2 ： ACL_RT_NOTIFY_EXPORT_FLAG_DISABLE_PID_VALIDATION ，关 闭进程白名单校验。 配置为该值时，则无需调用 aclrtNotifySetImportPid 接口。 |

| 返回值   | 说明                 |
|-------|--------------------|
| key   | str ， Notify 共享名称。 |

## 约束说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |

昇 腾虚拟化实例场景不支持该操作。
