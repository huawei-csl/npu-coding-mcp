# aclrtMemSetPidToShareableHandleV2

> **Section**: 1.13.39


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

设置共享内存的进程白名单。

本接口是在接口 aclrtMemSetPidToShareableHandle 基础上进行了增强，用户可通 过 shareType 参数指定导出 AI Server 内的共享句柄，或导出跨 AI Server 的共享句柄。

本接口的使用流程可参见 aclrtMemExportToShareableHandle ，但本接口需配合调 用 aclrtMemExportToShareableHandleV2 接口导出共享句柄、调用 aclrtMemImportFromShareableHandleV2 接口导入共享句柄。

aclError aclrtMemSetPidToShareableHandleV2(void *shareableHandle, aclrtMemSharedHandleType shareType, int32\_t *pid, size\_t pidNum)

| 参数名              | 输入 / 输 出   | 说明                                                                       |
|------------------|------------|--------------------------------------------------------------------------|
| shareableHa ndle | 输入         | 通过 aclrtMemExportToShareableHandleV2 接口导出的 shareableHandle ，表示指向共享句柄的指针。 |
| shareType        | 输入         | 导出的共享句柄类型。类型定义请参见 aclrtMemSharedHandleType 。                             |

## 返回值说明

| 参数名    | 输入 / 输 出   | 说明                                                                                                           |
|--------|------------|--------------------------------------------------------------------------------------------------------------|
| pid    | 输入         | 用于存放白名单进程 ID 的数组。 进程 ID 可调用 aclrtDeviceGetBareTgid 接口获取， Docker 场景下获取到的是物理机上的进程 ID ，非 Docker 场景下获取到的是进程 ID 。 |
| pidNum | 输入         | 白名单进程数量，与 pid 参数数组的大小保持一致。                                                                                   |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
