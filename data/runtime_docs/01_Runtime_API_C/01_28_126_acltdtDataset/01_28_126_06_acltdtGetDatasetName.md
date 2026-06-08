# acltdtGetDatasetName

> **Section**: 1.28.126.6


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

获取标识 acltdtDataset （对等一个 Vector&lt;tensor&gt; ）的描述符。

const char *acltdtGetDatasetName(const acltdtDataset *dataset)

| 参数名     | 输入 / 输 出   | 说明                                                                       |
|---------|------------|--------------------------------------------------------------------------|
| dataset | 输入         | acltdtDataset 类型的指针。 需提前调用 acltdtCreateDataset 接口创建 acltdtDataset 类型的数据。 |

## 返回值说明

标识 acltdtDataset （对等一个 Vector&lt;tensor&gt; ）的描述符的指针。
