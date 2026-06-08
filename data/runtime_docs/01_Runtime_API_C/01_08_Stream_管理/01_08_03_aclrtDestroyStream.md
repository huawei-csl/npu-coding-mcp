# aclrtDestroyStream

> **Section**: 1.8.3


## 产品支持情况

- 上调用。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

## 接口调用示例

销毁 Stream ，销毁通过 aclrtCreateStream 或 aclrtCreateStreamWithConfig 或 aclrtCreateStreamV2 接口创建的 Stream ，若 Stream 上有未完成的任务，会等待任务 完成后再销毁 Stream 。

aclError aclrtDestroyStream(aclrtStream stream)

| 参数名    | 输入 / 输 出   | 说明                                 |
|--------|------------|------------------------------------|
| stream | 输入         | 待销毁的 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 在调用 aclrtDestroyStream 接口销毁指定 Stream 前，需要先调用 aclrtSynchronizeStream 接口确保 Stream 中的任务都已完成。
- 调用 aclrtDestroyStream 接口销毁指定 Stream 时，需确保该 Stream 在当前 Context 下。
- 在调用 aclrtDestroyStream 接口销毁指定 Stream 时，需确保其它接口没有正在使 用该 Stream 。

接口调用示例，参见 Stream 创建与销毁。
