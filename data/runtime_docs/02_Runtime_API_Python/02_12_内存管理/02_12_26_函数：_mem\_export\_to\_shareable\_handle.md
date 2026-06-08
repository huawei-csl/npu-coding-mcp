# 函数： mem\_export\_to\_shareable\_handle

> **Section**: 2.12.26


## 产品支持情况

## 功能说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

将本进程通过 acl.rt.malloc\_physical 接口获取到的 Device 物理内存 handle 导出，以便 后续将 Device 物理内存共享给其它进程。

## 函数原型

本接口需与以下其它接口配合使用，以便实现内存共享的目的（此处以 A 、 B 进程为 例，说明两个进程间的物理内存共享接口调用流程）：

## 1. 在 A 进程中：

- a. 调用 acl.rt.malloc\_physical 接口，申请物理内存。

先调用 acl.rt.mem\_get\_allocation\_granularity 接口获取内存申请粒度，然 后在调用 acl.rt.malloc\_physical 接口申请物理内存时 size 按获取到的内存申 请粒度对齐，以便节约内存。

若需申请地址连续的虚拟内存、最大化利用物理内存地址的目的，此处可配 合 acl.rt.reserve\_mem\_address 、 acl.rt.map\_mem 等接口申请虚拟内存、 建立虚拟内存与物理内存之间的映射，请参见对应接口的说明。

- b. 调用 acl.rt.mem\_export\_to\_shareable\_handle 接口，导出物理内存 handle ，输出 shareable\_handle 。

调用 acl.rt.mem\_export\_to\_shareable\_handle 接口时，可指定是否启用进 程白名单校验，若启用，则需单独调用

acl.rt.mem\_set\_pid\_to\_shareable\_handle 接口将 B 进程的进程 ID 设置为白 名单；反之，则无需调用 acl.rt.mem\_set\_pid\_to\_shareable\_handle 接口。

- c. 调用 acl.rt.free\_physical 接口，释放物理内存。

内存使用完成后，要及时调用 acl.rt.free\_physical 接口释放物理内存，实现 销毁 shareableHandle 。若有进程还在使用 shareableHandle ，则等待 shareableHandle 使用完成后再执行销毁任务。

所有涉及共享内存的进程都必须释放其物理内存，只有当所有相关进程都完 成释放操作后，物理内存才能真正被释放。释放物理内存后，原先分配的内 存将被归还给操作系统，此后使用该 handle 将导致未定义的行为。

## 2. 在 B 进程中：

- a. 调用 acl.rt.device\_get\_bare\_tgid 接口，获取 B 进程的进程 ID 。 本接口内部在获取进程 ID 时已适配物理机、虚拟机场景，用户只需调用本接 ，再配置其它接口使用，达到物理内存共享的目的。若用户不

口获取进程 ID 调用本接口、自行获取进程 ID ，可能会导致后续使用进程 ID 异常。

- b. 调用 acl.rt.mem\_import\_from\_shareable\_handle ，获取 shareable\_handle 里的信息，并返回本进程中的 handle 。（在调用 acl.rt.mem\_import\_from\_shareable\_handle 接口前，需确保待共享的物理 内存存在，不能提前释放。） 若需申请地址连续的虚拟内存、最大化利用物理内存地址的目的，此处可配 合 acl.rt.reserve\_mem\_address 、 acl.rt.map\_mem 等接口申请虚拟内存、 建立虚拟内存与物理内存之间的映射，请参见对应接口的说明。
- c. 调用 acl.rt.free\_physical 接口，释放物理内存。
- C 函数原型

aclError aclrtMemExportToShareableHandle(aclrtDrvMemHandle handle, aclrtMemHandleType handleType, uint64\_t flags, uint64\_t *shareableHandle)

- python 函数
- shareable\_handle, ret = acl.rt.mem\_export\_to\_shareable\_handle(handle, handle\_type, flags)

## 参数说明

## 返回值说明

## 约束说明

| 参数名         | 说明                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| handle      | int ，存放物理内存信息的 handle 。 需先在本进程调用 acl.rt.malloc_physical 接口申请物理内存，该 接口调用成功，会返回一个 handle 。 handle 与 shareableHandle 是一一对应的关系，在同一个进程中， 不允许一对多、或多对一，否则报错，例如重复调用本接口导出 时则会返回报错。                                                                                                                                                                                                                                       |
| handle_type | int ，预留参数，当前固定输入 ACL_MEM_HANDLE_TYPE_NONE = 0 。                                                                                                                                                                                                                                                                                                                                                                 |
| flags       | int ，是否启用进程白名单校验。 取值为如下宏： ● ACL_RT_VMM_EXPORT_FLAG_DEFAULT ：默认值，启用进程 白名单校验。 配置为该值时，需单独调用 acl.rt.mem_set_pid_to_shareable_handle 接口将使用 shareable_handle 的进程 ID 设置为白名单。 ● ACL_RT_IPC_MEM_EXPORT_FLAG_DISABLE_PID_VALIDATIO N ：关闭进程白名单校验。 配置为该值时，则无需调用 acl.rt.mem_set_pid_to_shareable_handle 接口。 宏的定义如下： #define ACL_RT_VMM_EXPORT_FLAG_DEFAULT 0x0UL #define ACL_RT_VMM_EXPORT_FLAG_DISABLE_PID_VALIDATION 0x1UL |

| 返回值               | 说明                                 |
|-------------------|------------------------------------|
| shareable_han dle | int ，标识共享给其它进程的 shareable_handle 。 |
| ret               | int ，错误码，返回 0 表示成功，返回其它值表示失败。      |

- Atlas 200I/500 A2 推理产品上， Ascend RC 形态不支持调用本接口。
- 支持 AI Server 内跨进程共享物理内存的产品型号如下，若跨 Device 还需配合 acl.rt.device\_enable\_peer\_access 接口使用。 AI Server 通常多个 NPU 设备组成的 服务器形态的统称。

Atlas 350 加速卡

Atlas A3 训练系列产品 /Atlas A3 推理系列产品

Atlas A2 训练系列产品 /Atlas A2 推理系列产品

Atlas 训练系列产品

Atlas 推理系列产品

- 不支持 昇 腾虚拟化实例场景。
