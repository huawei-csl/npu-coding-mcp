# 函数：fl oat\_to\_float16

> **Section**: 2.18.4


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

将fl oat （指fl oat32 ）类型的数据转换为 aclFloat16 类型的数据。

- C 函数原型

aclFloat16 aclFloatToFloat16(float value)

- python 函数

output = acl.float\_to\_float16(value)

| 参数名   | 说明             |
|-------|----------------|
| value | float ，待转换的数据。 |

| 返回值    | 说明                            |
|--------|-------------------------------|
| output | int ，错误码，返回 0 表示成功，返回其他值表示失败。 |
