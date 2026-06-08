# aclrtQueryEventWaitStatus

> **Section**: 1.9.9


## 产品支持情况

## 功能说明

aclError aclrtQueryEventStatus(aclrtEvent event, aclrtEventRecordedStatus *status)

| 参数名    | 输入 / 输 出   | 说明                                                                                                                                                                      |
|--------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event  | 输入         | 指定待查询的 Event 。类型定义请参见 aclrtEvent 。                                                                                                                                      |
| status | 输出         | Event 状态的指针。类型定义请参见 aclrtEventRecordedStatus 。 如果该 Event 捕获的所有任务都已经执行完成则返回 ACL_EVENT_RECORDED_STATUS_COMPLETE ，如果有任 何一个任务未执行完成则返回 ACL_EVENT_RECORDED_STATUS_NOT_READY 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

调用 aclrtStreamWaitEvent 接口后查询该 Event 对应的等待任务是否都执行完成。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

通过 aclrtCreateEventExWithFlag 接口创建的 Event ，不支持调用本接口。
