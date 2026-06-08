# 函数： notify\_batch\_reset

> **Section**: 2.11.6


## 产品支持情况

## 功能说明

## 函数原型

| 参数名    | 说明                       |
|--------|--------------------------|
| notify | int ，指定要查询的 Notify 指针地址。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | x      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | x      |

批量复位 Notify 。

- C 函数原型 aclError aclrtNotifyBatchReset(aclrtNotify *notifies, size\_t num)
- python 函数
- ret = acl.rt.notify\_batch\_reset(notifies)

## 参数说明

## 返回值说明

## 约束说明

| 参数名      | 说明                                                                                                            |
|----------|---------------------------------------------------------------------------------------------------------------|
| notifies | list ，存放 Notify 指针地址的列表。 定义： notifies=[notify_1, notify_2, ...] 列表中 Notify 指针地址元素通过 acl.rt.create_notify 接口获取 |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |

昇 腾虚拟化实例场景不支持该操作。
