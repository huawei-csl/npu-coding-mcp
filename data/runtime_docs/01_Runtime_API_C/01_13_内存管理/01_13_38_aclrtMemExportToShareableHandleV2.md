# aclrtMemExportToShareableHandleV2

> **Section**: 1.13.38


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

将本进程通过 aclrtMallocPhysical 接口获取到的 Device 物理内存 handle 导出，以便后 续将 Device 物理内存共享给其它进程。

本接口是在接口 aclrtMemExportToShareableHandle 基础上进行了增强，用户可通 过 shareType 参数指定导出 AI Server 内的共享句柄，或导出跨 AI Server 的共享句柄。 AI Server 通常是多个 Device 组成的服务器形态的统称。

本接口的使用流程可参见 aclrtMemExportToShareableHandle ，但本接口需配合调 用 aclrtMemSetPidToShareableHandleV2 接口设置进程白名单、调用 aclrtMemImportFromShareableHandleV2 接口导入共享句柄。

aclError aclrtMemExportToShareableHandleV2(aclrtDrvMemHandle handle, uint64\_t flags, aclrtMemSharedHandleType shareType, void *shareableHandle)

## 参数说明

## 返回值说明

## 约束说明

| 参数名              | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| handle           | 输入         | 存放物理内存信息的 handle 。类型定义请参见 aclrtDrvMemHandle 。 需先在本进程调用 aclrtMallocPhysical 接口申请物理内 存，该接口调用成功，会返回一个 handle 。 handle 与 shareableHandle 是一一对应的关系，在同一 个进程中，不允许一对多、或多对一，否则报错，例如 重复调用本接口导出时则会返回报错。                                                                                                                                                                                                 |
| flags            | 输入         | 是否启用进程白名单校验。 取值为如下宏： ● ACL_RT_VMM_EXPORT_FLAG_DEFAULT ：默认值， 启用进程白名单校验。 配置为该值时，需单独调用 aclrtMemSetPidToShareableHandleV2 接口将使 用 shareableHandle 的进程 ID 设置为白名单。 ● ACL_RT_VMM_EXPORT_FLAG_DISABLE_PID_VALID ATION ：关闭进程白名单校验。 配置为该值时，则无需调用 aclrtMemSetPidToShareableHandleV2 接口。 宏的定义如下： #define ACL_RT_VMM_EXPORT_FLAG_DEFAULT 0x0UL #define ACL_RT_VMM_EXPORT_FLAG_DISABLE_PID_VALIDATION 0x1UL |
| shareType        | 输入         | 导出的共享句柄类型。类型定义请参见 aclrtMemSharedHandleType 。                                                                                                                                                                                                                                                                                                                                                 |
| shareableHa ndle | 输出         | 指向共享句柄的指针。其指向的内存由调用者提供，大 小根据 shareType 决定： 若 shareType 为 ACL_MEM_SHARE_HANDLE_TYPE_DEFAULT ，则指向 一个 uint64_t 变量。 若 shareType 为 ACL_MEM_SHARE_HANDLE_TYPE_FABRIC ，则指向一 个 aclrtMemFabricHandle 结构体。 typedef struct aclrtMemFabricHandle { uint8_t data[128]; } aclrtMemFabricHandle;                                                                                                            |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 对于 Atlas 200I/500 A2 推理产品， Ascend RC 形态下，不支持调用本接口。

- 支持 AI Server 内跨进程共享物理内存，若跨 Device ，则还需配合 aclrtDeviceEnablePeerAccess 接口使用。
- 仅 Atlas A3 训练系列产品 /Atlas A3 推理系列产品支持跨 AI Server 的跨进程共享物 理内存。
- 不支持 昇 腾虚拟化实例场景。

算力分组的相关接口请参见 算力 查询与设置。

- 不支持算力分组场景。 1.18 Group
