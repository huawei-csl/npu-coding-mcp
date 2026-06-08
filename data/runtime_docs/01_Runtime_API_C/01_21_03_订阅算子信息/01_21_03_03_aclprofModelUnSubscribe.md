# aclprofModelUnSubscribe

> **Section**: 1.21.3.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

网络场景下，取消订阅算子的基本信息，包括算子名称、算子类型、算子执行耗时 等。

aclError aclprofModelUnSubscribe(uint32\_t modelId)

| 参数名     | 输入 / 输 出   | 说明           |
|---------|------------|--------------|
| modelId | 输入         | 已订阅的模型的 ID 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

与 aclprofModelSubscribe 接口配对使用。
