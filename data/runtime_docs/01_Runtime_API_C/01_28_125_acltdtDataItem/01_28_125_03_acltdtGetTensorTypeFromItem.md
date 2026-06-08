# acltdtGetTensorTypeFromItem

> **Section**: 1.28.125.3


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
| Atlas 200I/500 A2 推理产品           | x      |
| Atlas 推理系列产品                     | x      |
| Atlas 训练系列产品                     | √      |

收到 dataItem 数据之后，从数据描述里首先 check 这个数据是个正常数据，还是一个 end 数据，还是一个异常数据。

acltdtTensorType acltdtGetTensorTypeFromItem(const acltdtDataItem *dataItem)

| 参数名      | 输入 / 输 出   | 说明                                                                          |
|----------|------------|-----------------------------------------------------------------------------|
| dataItem | 输入         | acltdtDataItem 类型的指针。 需提前调用 acltdtCreateDataItem 接口创建 acltdtDataItem 类型的数据。 |

请参见 acltdtTensorType 。
