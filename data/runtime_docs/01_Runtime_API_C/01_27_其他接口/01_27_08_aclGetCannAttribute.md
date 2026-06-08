# aclGetCannAttribute

> **Section**: 1.27.8


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

查询运行环境是否支持指定的 CANN 特性。

aclError aclGetCannAttribute(aclCannAttr cannAttr, int32\_t *value)

| 参数名      | 输入 / 输 出   | 说明                                         |
|----------|------------|--------------------------------------------|
| cannAttr | 输入         | 特性列表枚举值，一次查询可指定其中一项。类型定义请参 见 aclCannAttr 。 |
| value    | 输出         | 是否支持： ● 1 ：支持 ● 0 ：不支持                     |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
