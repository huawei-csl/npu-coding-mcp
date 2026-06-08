# aclrtNotifyGetExportKey

> **Section**: 1.10.7


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 训练系列产品 | √      |

将本进程中的指定 Notify 设置为 IPC （ Inter-Process Communication ） Notify ，并返回 key （即 Notify 共享名称），用于在多 Device 上不同进程间实现任务同步。

本接口需与以下其它关键接口配合使用，以便实现多 Device 上不同进程间的任务同 步，此处以 Device 0 上的 A 进程、 Device 1 上的 B 进程为例，说明两个进程间的任务同 步接口调用流程 :

## 1. 在 A 进程中：

- a. 调用 aclrtCreateNotify 接口创建 Notify 。
- b. 调用 aclrtNotifyGetExportKey 接口导出 key （即 Notify 共享名称）。 调用 aclrtNotifyGetExportKey 接口时，可指定是否启用进程白名单校验， 若启用，则需单独调用 aclrtNotifySetImportPid 接口将 B 进程的进程 ID

设置 为白名单；反之，则无需调用 aclrtNotifySetImportPid 接口。

- c. 调用 aclrtWaitAndResetNotify 接口下发等待任务。
- d. 调用 aclrtDestroyNotify 接口销毁 Notify 。 涉及 IPC Notify 的进程都需要释放 Notify ，所有涉及 IPC Notify 的进程都完成
3. 释放操作， Notify 才真正释放。

## 2. 在 B 进程中：

- a. 调用 aclrtDeviceGetBareTgid 接口，获取 B 进程的进程 ID 。 本接口内部在获取进程 ID 时已适配物理机、虚拟机场景，用户只需调用本接 口获取进程 ID ，再配合其它接口使用，达到内存共享的目的。若用户不调用

本接口、自行获取进程 ID ，可能会导致后续使用进程 ID 异常。

- b. 调用 aclrtNotifyImportByKey 获取 key
2. 的信息，并返回本进程可以使用的 Notify 指针。建议fl ag 使用 ACL\_RT\_NOTIFY\_IMPORT\_FLAG\_ENABLE\_PEER\_ACCESS 开启两个 Device 间的数据交互。

调用 aclrtIpcMemImportByKey 接口前，需确保 IPC Notify ，不能提前释 放。

- c. 调用 aclrtRecordNotify 接口下发 Record 任务。
- d. 调用 aclrtDestroyNotify 接口销毁 Notify 。

aclError aclrtNotifyGetExportKey(aclrtNotify notify, char *key, size\_t len, uint64\_t flags)

| 参数名    | 输入 / 输 出   | 说明                               |
|--------|------------|----------------------------------|
| notify | 输入         | 指定 Notify 。类型定义请参见 aclrtNotify 。 |

- 之

| 参数名   | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                |
|-------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| key   | 输出         | Notify 共享名称。                                                                                                                                                                                                                                                                                                                                                                      |
| len   | 输入         | Notify 共享名称的长度，最小长度为 65 。                                                                                                                                                                                                                                                                                                                                                         |
| flags | 输入         | 是否启用进程白名单校验。 取值为如下宏： ● ACL_RT_NOTIFY_EXPORT_FLAG_DEFAULT ：默认值， 启用进程白名单校验。 配置为该值时，需单独调用 aclrtNotifySetImportPid 接 口将使用 Notify 共享名称的进程 ID 设置为白名单。 ● ACL_RT_NOTIFY_EXPORT_FLAG_DISABLE_PID_VALIDA TION ：关闭进程白名单校验。 配置为该值时，则无需调用 aclrtNotifySetImportPid 接 口。 宏的定义如下： #define ACL_RT_NOTIFY_EXPORT_FLAG_DEFAULT 0x0UL #define ACL_RT_NOTIFY_EXPORT_FLAG_DISABLE_PID_VALIDATION 0x02UL |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 约束说明

昇 腾虚拟化实例场景不支持该操作。

## 接口调用示例

接口调用示例，参见进程间通信。
