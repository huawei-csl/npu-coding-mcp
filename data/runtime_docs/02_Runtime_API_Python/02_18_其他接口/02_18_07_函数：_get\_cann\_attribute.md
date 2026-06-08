# 函数： get\_cann\_attribute

> **Section**: 2.18.7


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

查询运行环境是否支持指定的 CANN 特性。

- C 函数原型

aclError aclGetCannAttribute(aclCannAttr cannAttr, int32\_t *value)

- python 函数

value, ret = acl.get\_cann\_attribute(cann\_attr)

| 参数名       | 说明                                                  |
|-----------|-----------------------------------------------------|
| cann_attr | int ，特性列表枚举值，一次查询可指定其中一项，具体请参见 2.19.2 aclCannAttr 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| value | int ，是否支持。 ● 1 ：支持 ● 0 ：不支持   |
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
