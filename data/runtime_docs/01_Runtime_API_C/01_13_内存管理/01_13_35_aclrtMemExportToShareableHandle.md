# aclrtMemExportToShareableHandle

> **Section**: 1.13.35


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

将本进程通过 aclrtMallocPhysical 接口获取到的 Device 物理内存 handle 导出，以便后 续将 Device 物理内存共享给其它进程。

本接口需与以下其它关键接口配合使用，以便实现内存共享，此处以 A 、 B 进程为例， 说明两个进程间的物理内存共享接口调用流程：

## 1. 在 A 进程中：

- a. 调用 aclrtMallocPhysical 接口，申请物理内存。

先调用 aclrtMemGetAllocationGranularity 接口获取内存申请粒度，然后 再调用 aclrtMallocPhysical 接口申请物理内存时 size 按获取到的内存申请粒 度对齐，以便节约内存。

若需申请地址连续的虚拟内存、最大化利用物理内存，此处可配合

aclrtReserveMemAddress 、 aclrtMapMem 、 aclrtMemSetAccess 等接口 申请虚拟内存、建立虚拟内存与物理内存之间的映射、设置虚拟内存的访问 权限。

- b. 调用 aclrtMemExportToShareableHandle 接口，导出物理内存 handle ，输 出 shareableHandle 。

调用 aclrtMemExportToShareableHandle 接口时，可指定是否启用进程白 名单校验，若启用，则需单独调用 aclrtMemSetPidToShareableHandle 接 口将 B 进程的进程 ID 设置为白名单；反之，则无需调用

aclrtMemSetPidToShareableHandle 接口。

- c. 调用 aclrtFreePhysical 接口，释放物理内存。

内存使用完成后，要及时调用 aclrtFreePhysical 接口释放物理内存，实现销 毁 shareableHandle 。若有进程还在使用 shareableHandle ，则等待 shareableHandle 使用完成后再执行销毁任务。

所有涉及共享内存的进程都必须释放其物理内存，只有当所有相关进程都完 成释放操作后，物理内存才能真正被释放。释放物理内存后，原先分配的内 存将被归还给操作系统，此后使用该 handle 将导致未定义的行为。

## 2. 在 B 进程中：

- a. 调用 aclrtDeviceGetBareTgid 接口，获取 B 进程的进程 ID 。

本接口内部在获取进程 ID 时已适配物理机、虚拟机场景，用户只需调用本接 口获取进程 ID ，再配合其它接口使用，达到物理内存共享的目的。若用户不 调用本接口、自行获取进程 ID ，可能会导致后续使用进程 ID 异常。

- b. 调用 aclrtMemImportFromShareableHandle ，获取 shareableHandle 里的 信息，并返回本进程中的 handle 。

在调用 aclrtMemImportFromShareableHandle 接口前，需确保待共享的物 理内存存在，不能提前释放。

若需申请地址连续的虚拟内存、最大化利用物理内存地址，此处可配合 aclrtReserveMemAddress 、 aclrtMapMem 、 aclrtMemSetAccess 等接口 申请虚拟内存、建立虚拟内存与物理内存之间的映射、设置虚拟内存的访问 权限，请参见对应接口的说明。

- c. 调用 aclrtFreePhysical 接口，释放物理内存。

aclError aclrtMemExportToShareableHandle(aclrtDrvMemHandle handle, aclrtMemHandleType handleType, uint64\_t flags, uint64\_t *shareableHandle)

## 参数说明

## 返回值说明

## 约束说明

| 参数名              | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| handle           | 输入         | 存放物理内存信息的 handle 。类型定义请参见 aclrtDrvMemHandle 。 需先在本进程调用 aclrtMallocPhysical 接口申请物理内 存，该接口调用成功，会返回一个 handle 。 handle 与 shareableHandle 是一一对应的关系，在同一 个进程中，不允许一对多、或多对一，否则报错，例如 重复调用本接口导出时则会返回报错。                                                                                                                                                                                            |
| handleType       | 输入         | 预留参数，当前固定填 ACL_MEM_HANDLE_TYPE_NONE 。 类型定义请参见 aclrtMemHandleType 。                                                                                                                                                                                                                                                                                                                      |
| flags            | 输入         | 是否启用进程白名单校验。 取值为如下宏： ● ACL_RT_VMM_EXPORT_FLAG_DEFAULT ：默认值， 启用进程白名单校验。 配置为该值时，需单独调用 aclrtMemSetPidToShareableHandle 接口将使用 shareableHandle 的进程 ID 设置为白名单。 ● ACL_RT_VMM_EXPORT_FLAG_DISABLE_PID_VALID ATION ：关闭进程白名单校验。 配置为该值时，则无需调用 aclrtMemSetPidToShareableHandle 接口。 宏的定义如下： #define ACL_RT_VMM_EXPORT_FLAG_DEFAULT 0x0UL #define ACL_RT_VMM_EXPORT_FLAG_DISABLE_PID_VALIDATION 0x1UL |
| shareableHa ndle | 输出         | 标识共享给其它进程的 shareableHandle 。                                                                                                                                                                                                                                                                                                                                                            |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 对于 Atlas 200I/500 A2 推理产品， Ascend RC 形态下，不支持调用本接口。
- 支持 AI Server 内跨进程共享物理内存。若跨 Device ，则还需配合 aclrtDeviceEnablePeerAccess 接口使用。 AI Server 通常是多个 Device 组成的服 务器形态的统称。
- 不支持 昇 腾虚拟化实例场景。
- 不支持算力分组场景。 算力分组的相关接口请参见 1.18 算力 Group

查询与设置。

## 接口调用示例

接口调用示例，参见进程间通信。
