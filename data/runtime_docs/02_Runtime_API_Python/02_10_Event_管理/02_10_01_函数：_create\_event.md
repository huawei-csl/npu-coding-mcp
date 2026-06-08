# 函数： create\_event

> **Section**: 2.10.1


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

创建一个 Event ，创建的 Event 可用于统计两个 Event 之间的耗时、多 Stream 场景下的同 步等待等场景。

- C 函数原型

aclError aclrtCreateEvent(aclrtEvent *event)

- python 函数
- event, ret = acl.rt.create\_event()

无

| 返回值   | 说明                            |
|-------|-------------------------------|
| event | int ，创建的 Event 对象的指针地址。       |
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

采用本 API 创建的 Event 不支持在 acl.rt.reset\_event 接口中使用，否则会导致未定义的 行为。

调用本接口创建 Event 后，后续调用 acl.rt.record\_event 接口时，系统内部才会申请 Event 资源，因此会受 Event 数量的限制， Event 达到上限后，系统内部会等待资源释 放。

## Event 数量限制如下：

Atlas 推理系列产品，单个 Device 上最多支持 1023 个 Event 。

Atlas 200I/500 A2 推理产品，单个 Device 上最多支持 65536 个 Event 。

Atlas 训练系列产品，单个 Device 上最多支持 65535 个 Event 。

Atlas A2 训练系列产品 /Atlas A2 推理系列产品，单个 Device 上最多支持 65536 个 Event 。

Atlas A3 训练系列产品 /Atlas A3 推理系列产品，单个 Device 上最多支持 65536 个 Event 。
