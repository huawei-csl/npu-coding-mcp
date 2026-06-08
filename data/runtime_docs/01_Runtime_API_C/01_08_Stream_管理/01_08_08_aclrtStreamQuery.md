# aclrtStreamQuery

> **Section**: 1.8.8


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

查询指定 Stream 上的所有任务的执行状态。

aclError aclrtStreamQuery(aclrtStream stream, aclrtStreamStatus *status)

| 参数名    | 输入 / 输 出   | 说明                                        |
|--------|------------|-------------------------------------------|
| stream | 输入         | Stream 的指针。类型定义请参见 aclrtStream 。          |
| status | 输出         | Stream 上的任务状态。类型定义请参见 aclrtStreamStatus 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
