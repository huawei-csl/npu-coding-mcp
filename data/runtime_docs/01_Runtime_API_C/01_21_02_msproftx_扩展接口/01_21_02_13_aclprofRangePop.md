# aclprofRangePop

> **Section**: 1.21.2.13


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

在 Torch 场景下， msproftx 上报 Tensor 信息。

调用此接口后， Profiling 上报缓存的 Tensor 信息。

aclError aclprofRangePop()

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 功能说明

## 函数原型

## 返回值说明

aclError aclprofRangePushEx(aclprofEventAttributes *attr)

| 参数名   | 输入 / 输 出   | 说明                                                     |
|-------|------------|--------------------------------------------------------|
| attr  | 输入         | 需要上报的 Tensor 信息，结构体详见 1.28.18 aclprofEventAttributes 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 约束说明

与 1.21.2.12 aclprofRangePushEx 接口配对使用，先调用 aclprofRangePushEx 接口再 调用 aclprofRangePop 接口。
