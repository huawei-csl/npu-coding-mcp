# aclrtGetHardwareSyncAddr

> **Section**: 1.16.13


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

获取 Cube Core 、 Vector Core 之间的同步地址。

aclError aclrtGetHardwareSyncAddr(void **addr)

| 参数名   | 输入 / 输 出   | 说明    |
|-------|------------|-------|
| addr  | 输出         | 同步地址。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
