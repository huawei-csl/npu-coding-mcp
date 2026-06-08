# 函数： stream\_abort

> **Section**: 2.9.11


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
| Atlas 训练系列产品                      | x      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | x      |

停止指定 Stream 上的正在执行的任务、丢弃指定 Stream 上已下发但未执行的任务。本 接口执行期间，指定 Stream 上新下发的任务不再生效。

- C 函数原型

aclError aclrtStreamAbort(aclrtStream stream)

- python 函数

ret = acl.rt.stream\_abort(stream)

| 参数名    | 说明                                                                                                                                                      |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| stream | int ，指定待清除任务的 Stream 。 各产品型号对默认 Stream （即该参数传入 0 ）的支持情况不同，如下： Atlas 350 加速卡，不支持 Atlas A3 训练系列产品 /Atlas A3 推理系列产品，支持 Atlas A2 训练系列产品 /Atlas A2 推理系列产品，支持 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

## 约束说明

- 不支持如下方式创建的 Stream ：调用 acl.rt.create\_stream\_with\_config 接口， 将fl ag 设置为 ACL\_STREAM\_DEVICE\_USE\_ONLY （表示该 Stream 仅在 Device 上调 用）。
- 如果有其它 Stream 依赖本接口中指定的 Stream （例如通过 acl.rt.record\_event 、 acl.rt.stream\_wait\_event 等接口实现两个 Stream 间同步等待），则其它 Stream 执行可能会卡住，此时您需要显式调用本接口清除其它 Stream 上的任务。
- 如果调用本接口清除指定 Stream 上的任务时，再调用同步等待接口（例如 acl.rt.synchronize\_stream 、 acl.rt.synchronize\_event 等），同步等待接口会退 出并返回 ACL\_ERROR\_RT\_STREAM\_ABORT 的报错。
