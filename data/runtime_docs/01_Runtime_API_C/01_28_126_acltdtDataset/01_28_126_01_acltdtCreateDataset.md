# acltdtCreateDataset

> **Section**: 1.28.126.1


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

创建 acltdtDataset 类型的数据，对等一个 Vector&lt;tensor&gt; 。

如需销毁 acltdtDataset 类型的数据，请参见 acltdtDestroyDataset 。

acltdtDataset *acltdtCreateDataset()

无

- 返回 acltdtDataset 类型的指针，表示成功。
- 返回 nullptr ，表示失败。
