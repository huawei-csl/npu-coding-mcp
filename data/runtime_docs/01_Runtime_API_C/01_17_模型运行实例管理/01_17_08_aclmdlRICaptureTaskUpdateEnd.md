# aclmdlRICaptureTaskUpdateEnd

> **Section**: 1.17.8


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

标记待更新任务的结束。

aclmdlRICaptureTaskUpdateBegin 接口与本接口成对使用，位于这两个接口之间的 任务需更新。

aclError aclmdlRICaptureTaskUpdateEnd(aclrtStream stream)

| 参数名    | 输入 / 输出   | 说明                                                                                                |
|--------|-----------|---------------------------------------------------------------------------------------------------|
| stream | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。 此处的 Stream 需与 aclmdlRICaptureTaskUpdateBegin 接口中指定的 Stream 保持一致。 |

## 返回值说明

## 约束说明

## 接口调用示例

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

待更新的任务是异步接口，本接口返回成功，并不代表任务更新完成。

单个 Device 可支持同时更新的最大任务数是 1024*1024 个，超出该规格，任务会在执 行阶段报错。

接口调用示例，参见任务更新。
