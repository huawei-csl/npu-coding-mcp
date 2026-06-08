# 函数： device\_get\_stream\_priority\_range

> **Section**: 2.7.21


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

查询硬件支持的 Stream 最小、最大优先级。

- C 函数原型

aclError aclrtDeviceGetStreamPriorityRange(int32\_t *leastPriority, int32\_t *greatestPriority)

- python 函数

min, max, ret = acl.rt.device\_get\_stream\_priority\_range()

无

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
| max   | int ，最大优先级                    |
| min   | int ，最小优先级                    |
