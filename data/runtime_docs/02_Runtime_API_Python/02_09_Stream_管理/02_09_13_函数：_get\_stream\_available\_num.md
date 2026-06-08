# 函数： get\_stream\_available\_num

> **Section**: 2.9.13


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

获取当前 Device 上剩余可用的 Stream 数量。

- C 函数原型 aclError aclrtGetStreamAvailableNum(uint32\_t *streamCount)
- python 函数

stream\_count, ret = acl.rt.get\_stream\_available\_num()

无

| 返回值           | 说明                        |
|---------------|---------------------------|
| stream_c ount | int ，剩余可用的 Stream 数量。     |
| ret           | int ，返回 0 表示成功，返回其他值表示失败。 |
