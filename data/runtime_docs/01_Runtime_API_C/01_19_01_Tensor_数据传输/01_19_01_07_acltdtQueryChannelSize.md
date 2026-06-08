# acltdtQueryChannelSize

> **Section**: 1.19.1.7


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

查询队列通道内的消息数量。

aclError acltdtQueryChannelSize(const acltdtChannelHandle *handle, size\_t *size)

## 参数说明

## 返回值说明

| 参数名    | 输入 / 输 出   | 说明                                                                           |
|--------|------------|------------------------------------------------------------------------------|
| handle | 输入         | 指定通道。 需提前调用 acltdtCreateChannelWithCapacity 接口创 建 acltdtChannelHandle 类型的数据。 |
| size   | 输出         | 消息数量的指针。                                                                     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
