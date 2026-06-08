# aclrtStreamWaitEventWithTimeout

> **Section**: 1.9.14


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

阻塞指定 Stream 的运行，直到指定的 Event 完成。异步接口。

该接口是在接口 aclrtStreamWaitEvent 基础上进行了增强，支持用户配置具体的超时 时间。

## 函数原型

## 参数说明

## 返回值说明

aclError aclrtStreamWaitEventWithTimeout(aclrtStream stream, aclrtEvent event, int32\_t timeout)

| 参数名     | 输入 / 输 出   | 说明                                                                                           |
|---------|------------|----------------------------------------------------------------------------------------------|
| stream  | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 多 Stream 同步等待场景下，例如， Stream2 等待 Stream1 的场景，此处配置为 Stream2 。 |
| event   | 输入         | 需等待的 Event 。类型定义请参见 aclrtEvent 。                                                             |
| timeout | 输入         | 超时时间。 取值 >0 ，用于配置具体的超时时间，单位是毫秒。                                                              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
