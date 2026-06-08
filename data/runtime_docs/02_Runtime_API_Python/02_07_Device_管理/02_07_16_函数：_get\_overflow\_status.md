# 函数： get\_overflow\_status

> **Section**: 2.7.16


## 产品支持情况

## 功能说明

| 参数名          | 说明                                                                                                                                        |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| peer_dev_i d | int ， Device ID ，该 ID 不能与当前 Device 的 ID 相同。 用户调 acl.rt.get_device_count 接口获取可用的 Device 数量后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取当前 Device 下所有 Stream 上任务的溢出状态，并将状态值拷贝到用户申请的 Device 内存中。异步接口。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

- C 函数原型

aclError aclrtGetOverflowStatus(void *outputAddr, size\_t outputSize, aclrtStream stream)

## ● python 函数

ret = acl.rt.get\_overflow\_status(outputAddr, outputSize, stream)

| 参数名         | 说明                                                                                                                                |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------|
| outputAdd r | int ，用户申请的 Device 内存，需通过 acl.rt.malloc 接口申请。如果需 要在 Host 侧查看数据，可调用 acl.rt.memcpy 或 acl.rt.memcpy_async 接口，将 Device 侧的数据传输到 Host 侧。 |
| outputSize  | int ，需申请的 Device 内存大小，单位 Byte ，固定大小为 64Byte 。                                                                                     |
| stream      | int ，指定 Stream 的指针地址，用于下发溢出状态查询任务。                                                                                                |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

该接口是异步接口，调用接口成功仅表示任务下发成功，不表示任务执行成功。调用 该接口后，需调用同步等待接口（例如， acl.rt.synchronize\_stream ）确保任务已执 行完成。

Atlas A2 训练系列产品 /Atlas A2 推理系列产品上，调用本接口查询出来的溢出状态是 进程级别的。

Atlas A3 训练系列产品 /Atlas A3 推理系列产品上，调用本接口查询出来的溢出状态是 进程级别的。
