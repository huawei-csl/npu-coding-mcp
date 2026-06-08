# 函数： use\_stream\_res\_in\_current\_thread

> **Section**: 2.6.9


## 产品支持情况

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 推理系列产品           | √      |
| Atlas 200I/500 A2 推理产品 | √      |

调用 acl.rt.set\_stream\_res\_limit 接口设置指定 Stream 的 Device 资源限制后，可调用本 接口重置指定 Stream 的 Device 资源限制，恢复默认配置，此时可通过 acl.rt.get\_stream\_res\_limit 接口查询默认的资源限制。

- C 函数原型

aclError aclrtResetStreamResLimit(aclrtStream stream)

- python 函数

ret = acl.rt.reset\_stream\_res\_limit(stream)

| 参数名    | 说明                                    |
|--------|---------------------------------------|
| stream | int ，指定 Stream, 若传入 0 ，则表示默认 Stream 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
