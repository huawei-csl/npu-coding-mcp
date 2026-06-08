# aclrtDestroyStreamConfigHandle

> **Section**: 1.28.113.2


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | x      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | x      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | x      |
| Atlas 200I/500 A2 推理产品           | x      |
| Atlas 推理系列产品                     | x      |
| Atlas 训练系列产品                     | x      |

销毁通过 aclrtCreateStreamConfigHandle 接口创建的 aclrtStreamConfigHandle 类 型的数据。

aclError aclrtDestroyStreamConfigHandle(aclrtStreamConfigHandle *handle)

| 参数名    | 输入 / 输 出   | 说明                                  |
|--------|------------|-------------------------------------|
| handle | 输入         | 待销毁的 aclrtStreamConfigHandle 类型的指针。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
