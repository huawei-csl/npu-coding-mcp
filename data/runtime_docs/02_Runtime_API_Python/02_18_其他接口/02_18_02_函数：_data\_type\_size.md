# 函数： data\_type\_size

> **Section**: 2.18.2


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取 aclDataType 数据的大小，单位 Byte 。

- C 函数原型 size\_t aclDataTypeSize(aclDataType dataType)
- python 函数
- size = acl.data\_type\_size(data\_type)

## 参数说明

## 返回值说明

| 返回值   | 说明                                |
|-------|-----------------------------------|
| size  | int ， aclDataType 数据的大小，单位 Byte 。 |
