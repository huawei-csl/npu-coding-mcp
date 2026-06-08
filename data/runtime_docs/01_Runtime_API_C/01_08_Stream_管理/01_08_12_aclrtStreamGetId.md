# aclrtStreamGetId

> **Section**: 1.8.12


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

获取指定 Stream 的 ID 。

## 函数原型

## 参数说明

## 返回值说明

aclError aclrtStreamGetId(aclrtStream stream, int32\_t *streamId)

| 参数名      | 输入 / 输 出   | 说明                                                                     |
|----------|------------|------------------------------------------------------------------------|
| stream   | 输入         | 指定要查询的 Stream 。类型定义请参见 aclrtStream 。 若此处传入 NULL ，则获取的是默认 Stream 的 ID 。 |
| streamId | 输出         | Stream ID 。                                                            |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
