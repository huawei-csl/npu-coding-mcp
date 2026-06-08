# 函数： get\_device\_count

> **Section**: 2.7.7


## 产品支持情况

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |

设置本次计算需要使用的 Task Schedule 。

- C 函数原型

aclError aclrtSetTsDevice(aclrtTsId tsId)

- python 函数

ret = acl.rt.set\_ts\_device(ts\_id)

| 参数名   | 说明                                                                                                                                                                                                                                              |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ts_Id | int ，指定本次计算需要使用的 Task Schedule 。如果 昇 腾 AI 软件栈中仅 有 AICORE Task Schedule ，则设置该参数无效，默认使用 AICORE Task Schedule 。 ● 0 ： ACL_TS_ID_AICORE ，使用 AICORE Task Schedule 。 ● 1 ： ACL_TS_ID_AIVECTOR ，使用 AIVECTOR Task Schedule 。 ● 2 ： ACL_TS_ID_RESERVED 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| count | int ，获取 Device 数量。            |
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
