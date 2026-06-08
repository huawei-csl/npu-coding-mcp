# 函数： wait\_and\_reset\_notify

> **Section**: 2.11.4


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

阻塞指定 Stream 的运行，直到指定的 Notify 完成，再复位 Notify 。

- C 函数原型 aclError aclrtWaitAndResetNotify(aclrtNotify notify, aclrtStream stream, uint32\_t timeout)
- python 函数

ret = acl.rt.wait\_and\_reset\_notify(notify, stream, timeout)

| 参数名    | 说明                                                                                      |
|--------|-----------------------------------------------------------------------------------------|
| notify | int ，需等待的 Notify 指针地址。                                                                  |
| stream | int ，指定 Stream 指针地址。例如， Stream2 等 Stream1 的场景，此处 配置为 Stream2 。 如果使用默认 Stream ，此处设置为 0 。 |

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
