# aclrtCreateEventExWithFlag

> **Section**: 1.9.3


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

创建带fl ag 的 Event ，不同fl ag 的 Event 用于不同的功能。支持创建 Event 时携带多个fl ag （按位进行或操作），从而同时使能对应fl ag 的功能。创建 Event 时， Event 资源不受硬 件限制。

aclError aclrtCreateEventExWithFlag(aclrtEvent *event, uint32\_t flag)

| 参数名   | 输入 / 输 出   | 说明                             |
|-------|------------|--------------------------------|
| event | 输出         | Event 的指针。类型定义请参见 aclrtEvent 。 |

## 返回值说明

## 约束说明

| 参数名   | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| flag  | 输入         | Event 指针的fl ag 。 当前支持将fl ag 设置为如下宏： ● ACL_EVENT_TIME_LINE ：使能该 bit 表示创建的 Event 需 要记录时间戳信息。注意：使能时间戳功能会影响 Event 相关接口的性能。 ● ACL_EVENT_SYNC ：使能该 bit 表示创建的 Event 支持多 Stream 间的同步。 ● ACL_EVENT_CAPTURE_STREAM_PROGRESS ：使能该 bit 表示创建的 Event 用于跟踪 stream 的任务执行进度。 ● ACL_EVENT_IPC ：使能该 bit 表示创建的 Event 用于进程 间通信，详细说明请参见 1.9.19 aclrtIpcGetEventHandle 。注意：该fl ag 不支持与其他 flag 进行位或操作。本fl ag 创建出来的 Event 不支持在以 下接口或场景中使用： aclrtResetEvent 、 aclrtQueryEvent 、 aclrtQueryEventWaitStatus 、 aclrtEventElapsedTime 、 aclrtEventGetTimestamp 、 aclrtGetEventId 、模型捕 获场景（参见 1.17.1 aclmdlRICaptureBegin 中的说 明），否则返回报错。 宏的定义如下： #define ACL_EVENT_TIME_LINE 0x00000008U #define ACL_EVENT_SYNC 0x00000001U #define ACL_EVENT_CAPTURE_STREAM_PROGRESS 0x00000002U #define ACL_EVENT_IPC 0x00000040U |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

采用本 API 创建的 Event ，不支持在以下接口中使用： aclrtResetEvent 、 aclrtQueryEvent 、 aclrtQueryEventWaitStatus ，否则返回报错。

调用本接口创建 Event 时，fl ag 为 bitmap ，支持将fl ag 设置为单个宏、或者对多个宏进 行或操作。若fl ag 参数值不包含 ACL\_EVENT\_SYNC 宏，则不支持在 aclrtStreamWaitEvent 接口中使用本接口创建的 Event 。若fl ag 参数值包含 ACL\_EVENT\_SYNC 宏，并不会实际申请 Event 资源，只有在调用 aclrtRecordEvent 接 口时，才会进行资源申请，因此在调用 aclrtRecordEvent 时，可能会出现线程阻塞， 等待 Event 资源的释放。

不同型号的硬件支持的 Event 数量不同，如下表所示：

| 型号           |   单个 Device 支持的 Event 最大数 |
|--------------|---------------------------|
| Atlas 推理系列产品 |                      1023 |

## 接口调用示例

| 型号                                                                                                       |   单个 Device 支持的 Event 最大数 |
|----------------------------------------------------------------------------------------------------------|---------------------------|
| Atlas 训练系列产品                                                                                             |                     65535 |
| Atlas 350 加速卡 Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 Atlas 200I/500 A2 推理产品 |                     65536 |

接口调用示例，参见 Event 的创建与销毁。
