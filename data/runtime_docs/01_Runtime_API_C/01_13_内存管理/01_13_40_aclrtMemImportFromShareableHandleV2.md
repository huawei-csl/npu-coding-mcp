# aclrtMemImportFromShareableHandleV2

> **Section**: 1.13.40


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

在本进程中获取 shareableHandle 里的信息，并返回本进程中的 handle ，用于在本进程 中建立虚拟地址与物理地址之间的映射关系。

本接口是在接口 aclrtMemImportFromShareableHandle 基础上进行了增强，用户可 通过 shareType 参数指定导出 AI Server 内的共享句柄，或导出跨 AI Server 的共享句柄。

本接口的使用流程可参见 aclrtMemExportToShareableHandle ，但本接口需配合调 用 aclrtMemExportToShareableHandleV2 接口导出共享句柄、调用 aclrtMemSetPidToShareableHandleV2 接口设置进程白名单。

aclError aclrtMemImportFromShareableHandleV2(void *shareableHandle, aclrtMemSharedHandleType shareType, uint64\_t flags, aclrtDrvMemHandle *handle);

## 参数说明

## 返回值说明

## 约束说明

| 参数名              | 输入 / 输 出   | 说明                                                                                                                                             |
|------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| shareableHa ndle | 输入         | 待共享的 shareableHandle ，与 aclrtMemExportToShareableHandleV2 接口中导出的 shareableHandle 保持一致。 handle 与 shareableHandle 是一一对应的关系，在同一个 进程中，不允许一对多、或多对一。 |
| shareType        | 输入         | 导出的共享句柄类型。类型定义请参见 aclrtMemSharedHandleType 。                                                                                                   |
| flags            | 输入         | 预留参数，当前固定设置为 0 。                                                                                                                               |
| handle           | 输出         | 本进程的物理内存 handle 。类型定义请参见 aclrtDrvMemHandle 。                                                                                                   |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 在调用本接口前，需确保待共享的物理内存存在，不能提前释放。
- 不支持同一个进程中调用 aclrtMemImportFromShareableHandleV2 、 aclrtMemExportToShareableHandle V2 这两个接口，只支持跨进程调用。
- 内存使用完成后，要及时调用 aclrtFreePhysical 销毁 handle ，并且需所有调用本 接口的进程都销毁 shareableHandle 的情况下， handle 才会真正销毁。
