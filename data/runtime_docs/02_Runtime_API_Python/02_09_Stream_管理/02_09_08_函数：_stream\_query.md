# 函数： stream\_query

> **Section**: 2.9.8


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

查询指定 Stream 上的所有任务的执行状态。

- C 函数原型

aclError aclrtStreamQuery(aclrtStream stream, aclrtStreamStatus *status)

- python 函数

status, ret = acl.rt.stream\_query(stream)

| 参数名    | 说明                     |
|--------|------------------------|
| stream | int ，待操作 Stream 的指针地址。 |

| 返回值    | 说明                                              |
|--------|-------------------------------------------------|
| status | Stream 上的任务状态，具体请参见 2.19.48 aclrtStreamStatus 。 |
| ret    | int ，错误码，返回 0 表示成功，返回其它值表示失败。                   |

本接口支持在以下场景使用：

- 昇 腾虚拟化实例（ Ascend Virtual Instance ）场景下支持使用该接口查询任务的执 行状态。
