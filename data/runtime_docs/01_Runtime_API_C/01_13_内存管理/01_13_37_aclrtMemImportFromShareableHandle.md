# aclrtMemImportFromShareableHandle

> **Section**: 1.13.37


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

在本进程中获取 shareableHandle 里的信息，并返回本进程中的 handle ，用于在本进程 中建立虚拟地址与物理地址之间的映射关系。本接口还支持生成指定 Device 上的 handle 。

本接口需与其它接口配合使用，以便实现内存共享的目的，配合使用流程请参见 aclrtMemExportToShareableHandle 接口处的说明。

aclError aclrtMemImportFromShareableHandle(uint64\_t shareableHandle, int32\_t deviceId, aclrtDrvMemHandle *handle)

| 参数名              | 输入 / 输 出   | 说明                                                                                                                                           |
|------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| shareableHa ndle | 输入         | 待共享的 shareableHandle ，与 aclrtMemExportToShareableHandle 接口中导出的 shareableHandle 保持一致。 handle 与 shareableHandle 是一一对应的关系，在同一个 进程中，不允许一对多、或多对一。 |
| deviceId         | 输入         | 用于生成指定 Device ID 上的 handle 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数 量后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数 量 -1)]                      |
| handle           | 输出         | 本进程的物理内存 handle 。类型定义请参见 aclrtDrvMemHandle 。                                                                                                 |

## 返回值说明

## 约束说明

## 接口调用示例

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 在调用本接口前，需确保待共享的物理内存存在，不能提前释放。
- 不支持同一个进程中调用 aclrtMemImportFromShareableHandle 、 aclrtMemExportToShareableHandle 这两个接口，只支持跨进程调用。
- 支持在一个 Device 上调用 aclrtMemExportToShareableHandle 接口导出 handle ，然后调用本接口生成另一个 Device 上的 handle 。
- 内存使用完成后，要及时调用 aclrtFreePhysical 销毁 handle ，并且需所有调用本 接口的进程都销毁 shareableHandle 的情况下， handle 才会真正销毁。

接口调用示例，参见进程间通信。
