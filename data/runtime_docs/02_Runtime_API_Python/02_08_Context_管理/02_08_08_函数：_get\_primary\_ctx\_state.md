# 函数： get\_primary\_ctx\_state

> **Section**: 2.8.8


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

获取默认 Context 的状态。

- C 函数原型

aclError aclrtGetPrimaryCtxState(int32\_t deviceId, uint32\_t *flags, int32\_t *active)

- python 函数

active, flags, ret = acl.rt.get\_primary\_ctx\_state(device\_id)

| 参数名       | 说明                |
|-----------|-------------------|
| device_id | int ， device id 。 |

| 返回值    | 说明                                     |
|--------|----------------------------------------|
| active | int ，存放默认 Context 状态的指针， 0 ：未激活 1 ：激活。 |
| flags  | int ，预留值，当前固定返回 0 。                    |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
