# aclDataTypeSize

> **Section**: 1.27.2


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取 aclDataType 数据的大小，单位 Byte 。

size\_t aclDataTypeSize(aclDataType dataType)

| 参数名      | 输入 / 输 出   | 说明                                            |
|----------|------------|-----------------------------------------------|
| dataType | 输入         | 指定要获取大小的 aclDataType 数据。类型定义请参见 aclDataType 。 |

返回 aclDataType 数据的大小，单位 Byte 。
