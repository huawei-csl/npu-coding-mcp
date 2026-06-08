# aclrtCreateLabel

> **Section**: 1.12.1


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

创建标签。每个进程最多创建 65535 个标签。

调用本接口创建标签后，再依次配合 aclrtCreateLabelList 接口（创建标签列表）、 aclrtSetLabel 接口（在 Stream 上设置标签）、 aclrtSwitchLabelByIndex 接口（跳转 到指定 Stream ）使用，实现 Stream 之间的跳转。

aclError aclrtCreateLabel(aclrtLabel *label)

| 参数名   | 输入 / 输 出   | 说明                         |
|-------|------------|----------------------------|
| label | 输出         | 标签的指针。类型定义请参见 aclrtLabel 。 |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
