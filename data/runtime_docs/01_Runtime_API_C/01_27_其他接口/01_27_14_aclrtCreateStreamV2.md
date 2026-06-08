# aclrtCreateStreamV2

> **Section**: 1.27.14


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

创建 Stream ，支持创建 Stream 时增加 Stream 配置。

本接口需要配合其它接口一起使用，创建 Stream ，接口调用顺序如下：

1. 调用 aclrtCreateStreamConfigHandle 接口创建 Stream 配置对象。
2. 多次调用 aclrtSetStreamConfigOpt 接口设置配置对象中每个属性的值。
3. 调用 aclrtCreateStreamV2 接口创建 Stream 。
4. Stream 使用完成后，调用 aclrtDestroyStreamConfigHandle 接口销毁 Stream 配 置对象，调用 aclrtDestroyStream 接口销毁 Stream 。

## 函数原型

## 参数说明

## 返回值说明

aclError aclrtCreateStreamV2(aclrtStream *stream, const aclrtStreamConfigHandle *handle)

| 参数名    | 输入 / 输 出   | 说明                                                                                         |
|--------|------------|--------------------------------------------------------------------------------------------|
| stream | 输出         | Stream 的指针。类型定义请参见 aclrtStream 。                                                           |
| handle | 输入         | Stream 配置对象的指针。类型定义请参见 aclrtStreamConfigHandle 。 与 aclrtSetStreamConfigOpt 中的 handle 保持一致。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
