# 函数： reset\_stream\_res\_limit

> **Section**: 2.6.8


## 产品支持情况

设置指定 Stream 的 Device 资源限制。

本接口应在调用 acl.rt.set\_device 接口之后且在执行算子之前使用。如果对同一 Stream 进行多次设置，将以最后一次设置为准。

调用本接口设置指定 Stream 的 Device 资源限制后，需配合调用 acl.rt.use\_stream\_res\_in\_current\_thread 接口，设置在当前线程中使用指定 Stream 上的 Device 资源限制。可通过 acl.rt.get\_stream\_res\_limit 接口查询默认的资源限制。

## ● C 函数原型

aclError aclrtSetStreamResLimit(aclrtStream stream, aclrtDevResLimitType type, uint32\_t value)

- python 函数

ret = acl.rt.set\_stream\_res\_limit(stream,  type , value)

| 参数名    | 说明                                                                          |
|--------|-----------------------------------------------------------------------------|
| stream | int ，指定 Stream, 若传入 0 ，则表示默认 Stream 。                                       |
| type   | int ，资源类型，当前支持 Cube Core 、 Vector Core ，具体请参见新增 数据结构 aclrtDevResLimitType 。 |
| value  | int ，资源限制的大小。                                                               |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
