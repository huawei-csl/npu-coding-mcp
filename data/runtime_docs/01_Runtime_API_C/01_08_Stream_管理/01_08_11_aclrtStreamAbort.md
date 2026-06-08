# aclrtStreamAbort

> **Section**: 1.8.11


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

停止指定 Stream 上正在执行的任务、丢弃指定 Stream 上已下发但未执行的任务。本接 口执行期间，指定 Stream 上新下发的任务不再生效。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

aclError aclrtStreamAbort(aclrtStream stream)

| 参数名    | 输入 / 输出   | 说明                                     |
|--------|-----------|----------------------------------------|
| stream | 输入        | 指定待停止任务的 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 不支持使用 aclmdlRIBindStream 接口来绑定模型运行实例的 Stream 。
- 不支持如下方式创建的 Stream ：调用 aclrtCreateStreamWithConfig 接口，将 flag 设置为 ACL\_STREAM\_DEVICE\_USE\_ONLY （表示该 Stream 仅在 Device 上调 用）。
- Atlas 350 加速卡不支持默认 Stream （即 stream 参数传入 NULL ）。
- 如果有其它 Stream 依赖本接口中指定的 Stream （例如通过 aclrtRecordEvent 、 aclrtStreamWaitEvent 等接口实现两个 Stream 间同步等待），则其它 Stream 执 行可能会卡住，此时您需要显式调用本接口清除其它 Stream 上的任务。
- 如果调用本接口清除指定 Stream 上的任务时，再调用同步等待接口（例如 aclrtSynchronizeStream 、 aclrtSynchronizeEvent 等），同步等待接口会退出 并返回 ACL\_ERROR\_RT\_STREAM\_ABORT 的报错。
