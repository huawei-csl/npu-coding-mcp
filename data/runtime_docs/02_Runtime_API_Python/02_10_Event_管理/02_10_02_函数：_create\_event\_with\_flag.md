# 函数： create\_event\_with\_flag

> **Section**: 2.10.2


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

创建一个带fl ag 的 Event ，不同fl ag 的 Event 用于不同的功能。支持创建 Event 时携带多 个fl ag （按位进行或操作），从而同时使能对应fl ag 的功能。

- C 函数原型 aclError aclrtCreateEventWithFlag(aclrtEvent *event, uint32\_t flag)
- python 函数

event, ret = acl.rt.create\_event\_with\_flag(flag)

## 参数说明

## 返回值说明

## 约束说明

| 参数名   | 说明                                                                                                                                                                                                                                                                                  |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| flag  | int ， Event 的fl ag ，可支持以下选项。 ● ACL_EVENT_TIME_LINE = 0x00000008 ，表示创建的 Event 数量 不受限制且创建出来的 Event 可用于统计两个 Event 之间的耗时。 ● ACL_EVENT_SYNC = 0x00000001 ，表示创建的 Event 数量受限且 创建出来的可用于多 Stream 间的同步等待。 ● ACL_EVENT_CAPTURE_STREAM_PROGRESS = 0x00000002 ， 表示创建的 Event 用于跟踪 Stream 的任务执行进度。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| event | int ，创建的 Event 对象的指针地址。       |
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

使用本接口创建 Event 时，'fl ag '为 bitmap ，支持对单个fl ag 或者多个fl ag 进行操 作，例如： acl.rt.create\_event\_with\_flag( ACL\_EVENT\_TIME\_LINE | ACL\_EVENT\_SYNC ) 。

- 若'fl ag '参数值包含' ACL\_EVENT\_SYNC '，则创建出来的 Event 数量受限，具 体参考如下：

Atlas 200I/500 A2 推理产品，单个 Device 上最多支持 65536 个 Event 。

Atlas 推理系列产品，单个 Device 上最多支持 1023 个 Event 。

Atlas 训练系列产品，单个 Device 上最多支持 65535 个 Event 。

Atlas A2 训练系列产品 /Atlas A2 推理系列产品，单个 Device 上最多支持 65536 个 Event 。

Atlas A3 训练系列产品 /Atlas A3 推理系列产品，单个 Device 上最多支持 65536 个 Event 。

- 若fl ag 参数值不包含' ACL\_EVENT\_SYNC '，则不支持在以下 API 中使用本接口创 建的 Event ： acl.rt.reset\_event 、 acl.rt.stream\_wait\_event 、 acl.rt.query\_event\_wait\_status 。
