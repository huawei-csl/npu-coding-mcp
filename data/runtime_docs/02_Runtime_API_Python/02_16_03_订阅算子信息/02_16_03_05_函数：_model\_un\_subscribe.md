# 函数： model\_un\_subscribe

> **Section**: 2.16.3.5


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

网络场景下，取消订阅算子的基本信息，包括算子名称、算子类型、算子执行耗时 等。

- C 函数原型

aclError aclprofModelUnSubscribe(uint32\_t modelId)

- python 函数

ret = acl.prof.model\_un\_subscribe(model\_id)

| 参数名      | 说明                  |
|----------|---------------------|
| model_id | int ，已订阅的网络模型的 ID 。 |

| 返回值   | 说明                                  |
|-------|-------------------------------------|
| ret   | int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。 |

## 约束说明

需要与 acl.prof.model\_subscribe 接口配对使用。
