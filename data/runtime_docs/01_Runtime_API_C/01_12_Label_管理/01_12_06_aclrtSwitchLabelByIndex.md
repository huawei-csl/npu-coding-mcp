# aclrtSwitchLabelByIndex

> **Section**: 1.12.6


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

根据标签索引跳转到相应的标签位置，执行该标签所在 Stream 上的任务，同时当前 Stream 上的任务停止执行。异步接口。

aclError aclrtSwitchLabelByIndex(void *ptr, uint32\_t maxValue, aclrtLabelList labelList, aclrtStream stream)

## 参数说明

## 返回值说明

| 参数名       | 输入 / 输 出   | 说明                                                                                                       |
|-----------|------------|----------------------------------------------------------------------------------------------------------|
| ptr       | 输入         | 标签索引。 存放目标标签索引值的 Device 内存地址，索引值的数据类型 uint32 ，长度 4 字节，索引值从 0 开始。 当目标标签索引大于 labelList 数组的最大索引值时，跳转到 最大标签。 |
| maxValu e | 输入         | 标签列表中的标签个数。                                                                                              |
| labelList | 输入         | 标签列表。类型定义请参见 aclrtLabelList 。 通过 aclrtCreateLabelList 接口创建的标签列表作为此处的 输入。                                 |
| stream    | 输入         | 执行跳转任务的 Stream 。类型定义请参见 aclrtStream 。                                                                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
