# 函数： create\_stamp

> **Section**: 2.16.2.2


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

创建 msproftx 事件标记。后续调用 2.16.2.4 函数： mark 、 2.16.2.3 函数： set\_stamp\_trace\_message 、 2.16.2.6 函数： push 和 2.16.2.8 函数： range\_start 接 口时需要以描述该事件的指针地址作为输入，表示记录该事件发生的时间跨度。

与 2.16.2.10 函数： destroy\_stamp 接口配对使用，需提前调用 2.16.1.6 函数： start 接 口。

- C 函数原型 void *aclprofCreateStamp(void)
- python 函数

stamp = acl.prof.create\_stamp()

## 参数说明

## 约束说明

与 2.16.2.10 函数： destroy\_stamp 接口配对使用，需提前调用 2.16.1.6 函数： start 接 口。
