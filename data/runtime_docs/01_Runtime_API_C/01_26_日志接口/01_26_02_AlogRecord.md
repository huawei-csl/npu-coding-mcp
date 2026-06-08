# AlogRecord

> **Section**: 1.26.2


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 须知

该接口将在后续版本中废弃，不建议用户使用，以防止引发兼容性问题。

用于记录各模块产生的日志。

void AlogRecord(uint32\_t moduleId, uint32\_t logType, int32\_t level, const char *fmt, ...)

| 参数       | 输入 / 输出   | 说明                            |
|----------|-----------|-------------------------------|
| moduleId | 输入        | 模块 ID ，枚举值请参见 1.26.4 数据 类型定义。 |

## 函数功能

## 函数原型

## 参数说明

## 返回值

## 调用示例

AlogRecord(SLOG, DLOG\_TYPE\_RUN, DLOG\_INFO, "test run log");
