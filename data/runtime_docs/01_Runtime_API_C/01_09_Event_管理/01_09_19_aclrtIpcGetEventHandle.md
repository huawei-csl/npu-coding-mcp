# aclrtIpcGetEventHandle

> **Section**: 1.9.19


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | ☓      |
| Atlas 训练系列产品 | ☓      |

将本进程中的指定 Event 设置为 IPC （ Inter-Process Communication ） Event ，并返回 其 handle （即 Event 句柄），用于在跨进程场景下实现任务同步，支持同一个 Device 内 的多个进程以及跨 Device 的多个进程。

## 本接口需与以下其它关键接口配合使用，此处以 A 进程、 B 进程为例：

## 1. A 进程中：

- a. 调用 aclrtCreateEventExWithFlag 接口创建fl ag 为 ACL\_EVENT\_IPC 的 Event 。
- b. 调用 aclrtIpcGetEventHandle 接口获取用于进程间通信的 Event 句柄。
- c. 调用 aclrtRecordEvent 接口在 Stream 中插入 1.a 中创建的 Event 。

## 2. B 进程中：

- a. 调用 aclrtIpcOpenEventHandle 接口获取 A 进程中的 Event 句柄信息，并返回 本进程可以使用的 Event 指针。
- b. 调用 aclrtStreamWaitEvent 接口阻塞指定 Stream 的运行，直到指定的 Event 完成。
- c. Event 使用完成后，调用 aclrtDestroyEvent 接口销毁 Event 。

aclError aclrtIpcGetEventHandle(aclrtEvent event, aclrtIpcEventHandle *handle)

| 参数名    | 输入 / 输出   | 说明                                                                                                    |
|--------|-----------|-------------------------------------------------------------------------------------------------------|
| event  | 输入        | 指定 Event 。类型定义请参见 aclrtEvent 。 仅支持通过 aclrtCreateEventExWithFlag 接口创建的、 flag 为 ACL_EVENT_IPC 的 Event 。 |
| handle | 输出        | 进程间通信的 Event 句柄。类型定义请参见 aclrtIpcEventHandle 。                                                         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见进程间通信。
