# acltdtGetDimNumFromItem

> **Section**: 1.28.125.7


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | x      |
| Atlas 推理系列产品                     | x      |
| Atlas 训练系列产品                     | √      |

得到正常 tensor 数据的数据 Shape 中的维度个数。

size\_t acltdtGetDimNumFromItem(const acltdtDataItem *dataItem)

## 参数说明

## 返回值说明

| 参数名      | 输入 / 输 出   | 说明                                                                          |
|----------|------------|-----------------------------------------------------------------------------|
| dataItem | 输入         | acltdtDataItem 类型的指针。 需提前调用 acltdtCreateDataItem 接口创建 acltdtDataItem 类型的数据。 |

获取到的维度个数。
