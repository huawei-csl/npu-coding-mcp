# aclrtQueryEvent （废弃）

> **Section**: 1.9.7


须知：此接口后续版本会废弃，请使用 aclrtQueryEventStatus 接口。

## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | √      |
| Atlas 训练系列产品 | √      |

查询与本接口在同一线程中的 aclrtRecordEvent 接口所记录的 Event 是否执行完成。

aclError aclrtQueryEvent(aclrtEvent event, aclrtEventStatus *status)

| 参数名    | 输入 / 输 出   | 说明                                     |
|--------|------------|----------------------------------------|
| event  | 输入         | 指定待查询的 Event 。类型定义请参见 aclrtEvent 。     |
| status | 输出         | Event 状态的指针。类型定义请参见 aclrtEventStatus 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
