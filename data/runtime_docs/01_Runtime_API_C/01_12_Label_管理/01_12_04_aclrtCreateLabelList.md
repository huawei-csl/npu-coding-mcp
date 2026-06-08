# aclrtCreateLabelList

> **Section**: 1.12.4


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | √      |
| Atlas 训练系列产品 | √      |

创建标签列表。

aclError aclrtCreateLabelList(aclrtLabel *labels, size\_t num, aclrtLabelList *labelList)

| 参数名       | 输入 / 输 出   | 说明                                                         |
|-----------|------------|------------------------------------------------------------|
| labels    | 输入         | 标签数组。类型定义请参见 aclrtLabel 。 数组中的标签需通过 aclrtCreateLabel 接口创建。 |
| num       | 输入         | 标签数组长度，取值 (0, 65535] 。                                     |
| labelList | 输出         | 标签列表。类型定义请参见 aclrtLabelList 。                              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
