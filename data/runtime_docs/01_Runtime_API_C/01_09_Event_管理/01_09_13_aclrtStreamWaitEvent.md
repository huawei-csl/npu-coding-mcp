# aclrtStreamWaitEvent

> **Section**: 1.9.13


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

阻塞指定 Stream 的运行，直到指定的 Event 完成，支持多个 Stream 等待同一个 Event 的 场景。异步接口。

提交到 Stream 上的所有后续任务都需要等待 Event 捕获的任务都完成后才能开始执行。 具体见 aclrtRecordEvent 接口了解 Event 捕获的细节。

aclError aclrtStreamWaitEvent(aclrtStream stream, aclrtEvent event)

## 参数说明

## 返回值说明

## 约束说明

## 接口调用示例

| 参数名    | 输入 / 输 出   | 说明                                                                                            |
|--------|------------|-----------------------------------------------------------------------------------------------|
| stream | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 多 Stream 同步等待场景下，例如， Stream2 等待 Stream1 的 场景，此处配置为 Stream2 。 |
| event  | 输入         | 需等待的 Event 。类型定义请参见 aclrtEvent 。                                                              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

一个进程内，调用 aclInit 接口初始化后，若再调用 aclrtSetOpWaitTimeout 接口设置 超时时间，那么本进程内后续调用 aclrtStreamWaitEvent 接口下发的任务支持在所设 置的超时时间内等待，若等待的时间超过所设置的超时时间，则在调用同步等待接口 （例如， aclrtSynchronizeStream ）后，会返回报错。

接口调用示例，参见 Event 等待。
