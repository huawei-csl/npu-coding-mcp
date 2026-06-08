# aclrtPersistentTaskClean

> **Section**: 1.8.20


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

清理 ACL\_STREAM\_PERSISTENT 类型的 Stream 上的任务，适用于在不删除该类型 Stream 的情况下重新下发任务的场景。

ACL\_STREAM\_PERSISTENT 类型的 Stream 需调用 aclrtCreateStreamWithConfig 接口 创建。

aclError aclrtPersistentTaskClean(aclrtStream stream)

## 参数说明

## 返回值说明

| 参数名    | 输入 / 输 出   | 说明                               |
|--------|------------|----------------------------------|
| stream | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
