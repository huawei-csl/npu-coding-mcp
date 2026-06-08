# 函数： event\_get\_timestamp

> **Section**: 2.10.15


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

获取 Event 的执行结束时间点（表示从 AI 处理器系统启动以来的时间）。

本接口需与其它关键接口配合使用，接口调用顺序：

- 调用 acl.rt.create\_event / acl.rt.create\_event\_with\_flag 接口创建 Event 。
- 调用 acl.rt.record\_event 接口在 Stream 中记录 Event 。
- 调用 acl.rt.synchronize\_stream 接口阻塞应用程序运行， 直到指定 Stream 中的所 有任务都完成。
- 调用 acl.rt.event\_get\_timestamp 接口获取 Event 的执行时间。
- C 函数原型

aclError aclrtEventGetTimestamp(aclrtEvent event, uint64\_t *timestamp)

- python 函数

timestamp, ret = acl.rt.event\_get\_timestamp(event)

| 参数名   | 说明               |
|-------|------------------|
| event | int ，查询的 Event 。 |

| 返回值       | 说明                          |
|-----------|-----------------------------|
| timestamp | int ， Event 执行结束的时间点，单位为微秒。 |

| 返回值   | 说明                                           |
|-------|----------------------------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败，请参见 17.1-aclError 。 |
