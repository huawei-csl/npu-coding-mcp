# aclrtDestroyBinary

> **Section**: 1.16.29


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

销毁通过 aclrtCreateBinary 接口创建的 aclrtBinary 类型的数据。此处的算子为使用 Ascend C 语言开发的自定义算子。

注意，此处仅销毁 aclrtBinary 的数据，调用 aclrtCreateBinary 接口时传入的 data 内存 需由用户自行、及时释放，否则可能会导致内存异常。

aclError aclrtDestroyBinary(aclrtBinary binary)

| 参数名    | 输入 / 输 出   | 说明                      |
|--------|------------|-------------------------|
| binary | 输入         | 待销毁的 aclrtBinary 类型的指针。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
