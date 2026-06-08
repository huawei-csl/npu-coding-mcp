# 函数： set\_op\_wait\_timeout

> **Section**: 2.10.14


## 产品支持情况

| 参数名    | 说明                                                          |
|--------|-------------------------------------------------------------|
| stream | int ，指定需要等待 Event 完成的 Stream 的指针地址。如果使用默认 Stream ，此处设置为 0 。 |
| event  | int ，需等待的 Event 的指针地址。                                      |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 该接口是异步接口，调用接口成功仅表示任务下发成功，不表示任务执行成功。 调用该接口后，需调用同步等待接口（例如， acl.rt.synchronize\_stream ）确保 任务已执行完成。
- acl.rt.record\_event 接口与 acl.rt.stream\_wait\_event 接口配合使用时，主要用于 多 Stream 之间同步的场景，在调用 acl.rt.record\_event 接口时，系统内部会申请 Event 资源，在调用 acl.rt.stream\_wait\_event 接口之后，请及时调用 acl.rt.reset\_event 接口释放 Event 资源。

接口调用顺序： acl.rt.create\_event--&gt;acl.rt.record\_event--&gt;acl.rt.stream\_wait\_event--&gt;acl.rt.reset\_event

- 一个进程内，调用 acl.init 接口初始化后，调用 acl.rt.set\_op\_wait\_timeout 接口 设置超时时间，本进程内后续调用 acl.rt.stream\_wait\_event 接口下发的任务支 持在所设置的超时时间内等待，若等待的时间超过所设置的超时时间，则会返回 报错。

由于 acl.rt.stream\_wait\_event 接口是异步接口，调用接口成功仅表示任务下发成 功，不表示任务执行成功，因此若等待的时间超过所设置的超时时间，则在调用 acl.rt.synchronize\_stream 接口后，会返回报错。

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | √      |

本接口用于设置等待 Event 完成的超时时间。

- C 函数原型

aclError aclrtSetOpWaitTimeout(uint32\_t timeout)

- python 函数

ret = acl.rt.set\_op\_wait\_timeout(timeout)

| 参数名     | 说明                                  |
|---------|-------------------------------------|
| timeout | int ，设置超时时间，单位为秒。将该参数设置为 0 时，表示不超时。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 不调用本接口，则默认不超时，一个进程内多次调用本接口，则以最后一次设置 的时间为准。
- 一个进程内，调用 acl.init 接口初始化后，调用本接口设置超时时间，本进程内后 续调用 acl.rt.stream\_wait\_event 接口下发的任务支持在所设置的超时时间内等 待。

由于 acl.rt.stream\_wait\_event 接口是异步接口，调用接口成功仅表示任务下发 成功，不表示任务执行成功，因此若等待的时间超过所设置的超时时间，则在调 用 acl.rt.synchronize\_stream 接口后，会返回报错。
