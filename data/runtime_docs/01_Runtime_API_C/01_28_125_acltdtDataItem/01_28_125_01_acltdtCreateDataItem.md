# acltdtCreateDataItem

> **Section**: 1.28.125.1


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

创建 acltdtDataItem 类型的数据，代表一个业务上的 Tensor 。

如需销毁 acltdtDataItem 类型的数据，请参见 acltdtDestroyDataItem 。

acltdtDataItem *acltdtCreateDataItem(acltdtTensorType tdtType, const int64\_t *dims, size\_t dimNum, aclDataType dataType, void *data, size\_t size)

| 参数名     | 输入 / 输 出   | 说明                                   |
|---------|------------|--------------------------------------|
| tdtType | 输入         | tensor 类型。类型定义请参见 acltdtTensorType 。 |
| dims    | 输入         | tensor 的 Shape 。                     |
| dimNum  | 输入         | tensor 的 Shape 中的维度个数。               |

## 返回值说明

| 参数名      | 输入 / 输 出   | 说明                               |
|----------|------------|----------------------------------|
| dataType | 输入         | 正常数据里的数据类型。类型定义请参见 aclDataType 。 |
| data     | 输入         | 数据地址指针。                          |
| size     | 输入         | 数据长度。                            |

- 返回 acltdtDataItem 类型的指针，表示成功。
- 返回 nullptr ，表示失败。
