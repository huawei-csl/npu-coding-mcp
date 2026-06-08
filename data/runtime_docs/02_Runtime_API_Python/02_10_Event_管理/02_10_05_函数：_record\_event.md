# 函数： record\_event

> **Section**: 2.10.5


## 产品支持情况

## 功能说明

## ● python 函数

ret = acl.rt.destroy\_event(event)

| 参数名   | 说明                    |
|-------|-----------------------|
| event | int ，待销毁的 Event 指针地址。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

在调用 acl.rt.destroy\_event 接口销毁指定 Event 时，需确保其它接口没有正在使用该 Event 。

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

在 Stream 中记录一个 Event 。本接口被调用时，会捕获当前 Stream 上已下发的任务并 记录到 Event 事件中，因此后续若调用 acl.rt.query\_event\_status 或

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

acl.rt.stream\_wait\_event 接口时，会检查或等待该 Event 事件中所捕获的任务都已经 完成。

对于使用 acl rt.create\_event\_ex\_with\_flag 创建的 Event ：

- 本接口支持对同一个 Event 多次 record 实现 Event 复用，每次 Record 会重新捕获当 前 Stream 上已下发的任务，并覆盖保存到 Event 中。在调用 acl.rt.stream\_wait\_event 接口时，会使用最近一次 Event 中所保存的任务，且不 会被后续的 acl.rt.record\_event 调用影响。
- Event
- 在首次调用本接口前，由于 中没有任务，因此调用 acl.rt.query\_event\_status 接口时会返回 ' ACL\_EVENT\_RECORDED\_STATUS\_COMPLETE '。
- C 函数原型

aclError aclrtRecordEvent(aclrtEvent event, aclrtStream stream)

- python 函数

ret = acl.rt.record\_event(event, stream)

| 参数名    | 说明                                                           |
|--------|--------------------------------------------------------------|
| event  | int ，待记录的 Event 的指针地址。                                       |
| stream | int ，将该 Event 记录在指定的 Stream （指针地址）中，如果使用默认 Stream ，此处设置为 0 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 该接口是异步接口，调用接口成功仅表示任务下发成功，不表示任务执行成功。 调用该接口后，需调用同步等待接口（例如， acl.rt.synchronize\_stream ）确保 任务已执行完成。
- acl.rt.record\_event 接口与 acl.rt.stream\_wait\_event 接口配合使用时，主要用于 多 Stream 之间同步的场景，在调用 acl.rt.record\_event 接口时，系统内部会申请 Event 资源，在调用 acl.rt.stream\_wait\_event 接口之后，请及时调用 acl.rt.reset\_event 接口释放 Event 资源。

接口调用顺序： acl.rt.create\_event--&gt;acl.rt.record\_event--&gt;acl.rt.stream\_wait\_event--&gt;acl.rt.reset\_event

## 资源参考

接口调用示例，参见关于 Event 的同步等待、关于 Stream 间任务的同步等待（通过 Event 实现）。
