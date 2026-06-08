# 函数：fl oat16\_to\_float

> **Section**: 2.18.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 参数名       | 说明                            |
|-----------|-------------------------------|
| data_type | int ，指定要获取大小的 aclDataType 数据。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

将 aclFloat16 类型的数据转换为fl oat （指fl oat32 ）类型的数据。

- C 函数原型

float aclFloat16ToFloat(aclFloat16 value)

- python 函数

output = acl.float16\_to\_float(value)

| 参数名   | 说明                             |
|-------|--------------------------------|
| value | int ，待转换的数据， aclFloat16 类型的数据。 |

## 返回值说明

| 返回值    | 说明            |
|--------|---------------|
| output | float ，浮点数类型。 |
