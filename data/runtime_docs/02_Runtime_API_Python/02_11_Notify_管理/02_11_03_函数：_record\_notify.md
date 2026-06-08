# 函数： record\_notify

> **Section**: 2.11.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

在指定 Stream 上记录一个 Notify 。 acl.rt.record\_notify 接口与 acl.rt.wait\_and\_reset\_notify 接口配合使用时，主要用于多 Stream 之间同步等待的场

景。

- C 函数原型

aclError aclrtRecordNotify(aclrtNotify notify, aclrtStream stream)

- python 函数

ret = acl.rt.record\_notify(notify, stream)

| 参数名    | 说明                                                                                      |
|--------|-----------------------------------------------------------------------------------------|
| notify | int ，待记录的 Notify 指针地址。                                                                  |
| stream | int ，指定 Stream 指针地址。例如， Stream2 等 Stream1 的场景，此处 配置为 Stream1 。 如果使用默认 Stream ，此处设置为 0 。 |

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
