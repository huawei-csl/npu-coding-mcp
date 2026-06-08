# aclmdlRICaptureTaskGrpEnd

> **Section**: 1.17.6


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

标记任务组的结束。

aclmdlRICaptureTaskGrpBegin 接口与本接口成对使用，位于这两个接口之间的任务 构成一组任务，当前仅支持在这两个接口之间下发单算子调用的任务。

aclError aclmdlRICaptureTaskGrpEnd(aclrtStream stream, aclrtTaskGrp *handle)

| 参数名    | 输入 / 输出   | 说明                                                                                              |
|--------|-----------|-------------------------------------------------------------------------------------------------|
| stream | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。 此处的 Stream 需与 aclmdlRICaptureTaskGrpBegin 接口 中指定的 Stream 保持一致。 |
| handle | 输出        | 标识任务组的句柄。类型定义请参见 aclrtTaskGrp 。                                                                 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见任务更新。
