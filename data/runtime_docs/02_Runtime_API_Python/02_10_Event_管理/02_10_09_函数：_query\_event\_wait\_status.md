# 函数： query\_event\_wait\_status

> **Section**: 2.10.9


## 产品支持情况

查询该 Event 捕获的所有任务的执行状态。具体见 acl.rt.record\_event 接口参考 Event 捕获的细节。

- C 函数原型 aclError aclrtQueryEventStatus(aclrtEvent event, aclrtEventRecordedStatus *status)
- python 函数
- status, ret = acl.rt.query\_event\_status(event)

| 参数名   | 说明                         |
|-------|----------------------------|
| event | int ，指定待查询的 Event 对象的指针地址。 |

| 返回值    | 说明                                                                                                                                                                                              |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| status | int ，表示的是 Event 状态的指针地址。 ● ACL_EVENT_RECORDED_STATUS_NOT_READY = 0 ， Event 未被 记录到 Stream 中，或记录到 Stream 中的 Event 未被执行或执行失 败。 ● ACL_EVENT_RECORDED_STATUS_COMPLETE = 1 ，记录到 Stream 中的 Event 执行成功。 |
| ret    | int ，错误码，返回 0 表示成功，返回其它值表示失败。                                                                                                                                                                   |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

调用 acl.stream\_wait\_event 接口后查询该 Event 对应的等待任务是否都执行完成。

- C 函数原型 aclError aclrtQueryEventWaitStatus(aclrtEvent event, aclrtEventWaitStatus *status)
- python 函数

status, ret = acl.rt.query\_event\_wait\_status(event)

| 参数名   | 说明                         |
|-------|----------------------------|
| event | int ，指定待查询的 Event 对象的指针地址。 |

| 返回值    | 说明                                                                                                                                                                                                                              |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| status | int ， Event 状态的指针地址，具体请参见 2.19.25 aclrtEventWaitStatus 。 ● ACL_EVENT_RECORDED_STATUS_NOT_READY = 0 ， Event 未被 记录到 Stream 中，或记录到 Stream 中的 Event 未被执行或执行失 败。 ● ACL_EVENT_RECORDED_STATUS_COMPLETE = 1 ，记录到 Stream 中的 Event 执行成功。 |
| ret    | int ，错误码，返回 0 表示成功，返回其它值表示失败。                                                                                                                                                                                                   |

通过 acl.rt.create\_event\_ex\_with\_flag 接口创建的 Event ，不支持调用本接口。
