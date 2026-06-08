# 函数： query\_event\_status

> **Section**: 2.10.8


## 产品支持情况

- C 函数原型

aclError aclrtQueryEvent(aclrtEvent event, aclrtEventStatus *status)

- python 函数

status, ret = acl.rt.query\_event(event)

| 参数名   | 说明                        |
|-------|---------------------------|
| event | int ，指定待查询的 Event 对象指针地址。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

如果用户在不同线程上分别调用 acl.rt.record\_event 和 acl.rt.query\_event\_status ，可 能由于多线程导致这两个 API 的执行时间乱序，进而导致查询到的 Event 对象的完成状 态不符合预期。
