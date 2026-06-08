# acltdtGetDimsFromItem

> **Section**: 1.28.125.8


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | x      |
| Atlas 推理系列产品                     | x      |
| Atlas 训练系列产品                     | √      |

得到正常 tensor 数据的数据 Shape 。

aclError acltdtGetDimsFromItem(const acltdtDataItem *dataItem, int64\_t *dims, size\_t dimNum)

| 参数名      | 输入 / 输 出   | 说明                                                                          |
|----------|------------|-----------------------------------------------------------------------------|
| dataItem | 输入         | acltdtDataItem 类型的指针。 需提前调用 acltdtCreateDataItem 接口创建 acltdtDataItem 类型的数据。 |
| dims     | 输入 & 输 出   | 维度信息数组。                                                                     |

## 返回值说明

| 参数名    | 输入 / 输 出   | 说明    |
|--------|------------|-------|
| dimNum | 输入         | 维度个数。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
