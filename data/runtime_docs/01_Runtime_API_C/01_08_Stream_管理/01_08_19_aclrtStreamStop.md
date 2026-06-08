# aclrtStreamStop

> **Section**: 1.8.19


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

仅停止指定 Stream 上的正在执行的任务，不清理任务。

aclError aclrtStreamStop(aclrtStream stream)

![Figure](../../images/figure_1383.png)

**[Image: figure_1383.png (210x59, 8.5KB)]**

## 返回值说明

## 约束说明

| 参数名    | 输入 / 输 出   | 说明                                     |
|--------|------------|----------------------------------------|
| stream | 输入         | 指定待停止任务的 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 不支持使用 aclmdlRIBindStream 接口来绑定模型运行实例的 Stream 。
- 不支持默认 Stream （即 stream 参数传入 NULL ）。
- 对于 Atlas A2 训练系列产品 /Atlas A2 推理系列产品、 Atlas A3 训练系列产品 / Atlas A3 推理系列产品，该接口仅支持如下方式创建的 Stream ：调用 aclrtCreateStreamWithConfig 接口，将fl ag 设置为 ACL\_STREAM\_DEVICE\_USE\_ONLY （表示该 Stream 仅在 Device 上调用）。
