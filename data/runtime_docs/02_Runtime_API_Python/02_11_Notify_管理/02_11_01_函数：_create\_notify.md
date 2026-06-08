# 函数： create\_notify

> **Section**: 2.11.1


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

创建 Notify 。

- C 函数原型

aclError aclrtCreateNotify(aclrtNotify *notify, uint64\_t flag)

- python 函数

notify, ret = acl.rt.create\_notify(flag)

| 参数名   | 说明                  |
|-------|---------------------|
| flag  | int ，预留参数。当前固定配置为 0 |

| 返回值    | 说明                        |
|--------|---------------------------|
| notify | int ， Notify 的指针地址。       |
| ret    | int ，返回 0 表示成功，返回其他值表示失败。 |

不同型号的硬件支持的 Notify 数量不同，如下表所示：

| 型号                                                                  |   单个 Device 支持的 Notify 最大数 |
|---------------------------------------------------------------------|----------------------------|
| Atlas 350 加速卡                                                       |                      65535 |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 |                       8192 |
| Atlas 200I/500 A2 推理产品                                              |                       2048 |
| Atlas 推理系列产品 Atlas 训练系列产品                                           |                       1024 |
