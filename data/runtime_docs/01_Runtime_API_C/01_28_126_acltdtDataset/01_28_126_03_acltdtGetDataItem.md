# acltdtGetDataItem

> **Section**: 1.28.126.3


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | x      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | x      |
| Atlas 训练系列产品 | √      |

获取 acltdtDataset 中的第 n 个 acltdtDataItem 。

acltdtDataItem *acltdtGetDataItem(const acltdtDataset *dataset, size\_t index)

| 参数名     | 输入 / 输 出   | 说明                                                                                                                  |
|---------|------------|---------------------------------------------------------------------------------------------------------------------|
| dataset | 输入         | acltdtDataset 类型的指针。 需提前调用 acltdtCreateDataset 接口创建 acltdtDataset 类型的数据，再调用 acltdtAddDataItem 接口添加 acltdtDataItem 。 |
| index   | 输入         | 表明获取的是第几个 acltdtDataItem 。                                                                                          |

- 获取成功，返回 acltdtDataItem 的地址。
- 获取失败返回空地址。
