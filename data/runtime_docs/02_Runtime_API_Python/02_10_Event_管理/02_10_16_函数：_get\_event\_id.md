# 函数： get\_event\_id

> **Section**: 2.10.16


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

获取指定 Event 的 ID 。

- C 函数原型

aclError aclrtGetEventId(aclrtEvent event, uint32\_t *eventId)

- python 函数

event\_id, ret = acl.rt.get\_event\_id(event)

| 参数名   | 说明                  |
|-------|---------------------|
| event | int ，指定要查询的 Event 。 |

| 返回值      | 说明                        |
|----------|---------------------------|
| event_id | int ， Event ID 。          |
| ret      | int ，返回 0 表示成功，返回其他值表示失败。 |
