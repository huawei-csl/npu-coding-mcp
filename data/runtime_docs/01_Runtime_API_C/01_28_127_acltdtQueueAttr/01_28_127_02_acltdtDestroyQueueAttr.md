# acltdtDestroyQueueAttr

> **Section**: 1.28.127.2


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

销毁通过 acltdtCreateQueueAttr 接口创建的 acltdtQueueAttr 类型的数据。

aclError acltdtDestroyQueueAttr(const acltdtQueueAttr *attr)

| 参数名   | 输入 / 输 出   | 说明                          |
|-------|------------|-----------------------------|
| attr  | 输入         | 待销毁的 acltdtQueueAttr 类型的指针。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
