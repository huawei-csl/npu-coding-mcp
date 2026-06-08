# acltdtCleanChannel

> **Section**: 1.19.1.9


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
| Atlas 训练系列产品                     | √      |

清空通道中的所有数据。

aclError acltdtCleanChannel(acltdtChannelHandle *handle)

## 参数说明

## 返回值说明

| 参数名    | 输入 / 输 出   | 说明                                                                           |
|--------|------------|------------------------------------------------------------------------------|
| handle | 输入         | 指定通道。 需提前调用 acltdtCreateChannelWithCapacity 接口创 建 acltdtChannelHandle 类型的数据。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
