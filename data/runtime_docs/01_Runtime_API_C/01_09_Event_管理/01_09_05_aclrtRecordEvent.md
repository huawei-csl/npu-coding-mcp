# aclrtRecordEvent

> **Section**: 1.9.5


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

在指定 Stream 中记录一个 Event 。异步接口。

aclrtRecordEvent 接口与 aclrtStreamWaitEvent 接口配合使用时，主要用于多 Stream 之 间同步等待的场景。

调用 aclrtRecordEvent 接口时，会捕获当前 Stream 上已下发的任务，并记录到 Event 事 件中，因此后续若调用 aclrtQueryEventStatus 或 aclrtStreamWaitEvent 接口时，会 检查或等待该 Event 事件中所捕获的任务都已经完成。

另外，对于使用 aclrtCreateEventExWithFlag 创建的 Event ：

- aclrtRecordEvent 接口支持对同一个 Event 多次 record 实现 Event 复用，每次 Record 会重新捕获当前 Stream 上已下发的任务，并覆盖保存到 Event 中。在调用 aclrtStreamWaitEvent 接口时，会使用最近一次 Event 中所保存的任务，且不会被 后续的 aclrtRecordEvent 调用影响。
- 在首次调用 aclrtRecordEvent 接口前，由于 Event 中没有任务，因此调用 aclrtQueryEventStatus 接口时会返回 ACL\_EVENT\_RECORDED\_STATUS\_COMPLETE 。

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

## 功能说明

## 函数原型

aclError aclrtRecordEvent(aclrtEvent event, aclrtStream stream)

| 参数名    | 输入 / 输 出   | 说明                                                                                            |
|--------|------------|-----------------------------------------------------------------------------------------------|
| event  | 输入         | 待记录的 Event 。类型定义请参见 aclrtEvent 。                                                              |
| stream | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 多 Stream 同步等待场景下，例如， Stream2 等待 Stream1 的 场景，此处配置为 Stream1 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见 Event 等待。
