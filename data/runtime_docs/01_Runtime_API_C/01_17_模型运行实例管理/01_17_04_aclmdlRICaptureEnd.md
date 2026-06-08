# aclmdlRICaptureEnd

> **Section**: 1.17.4


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | √      |
| Atlas 训练系列产品 | ☓      |

结束 Stream 的捕获动作，并获取模型运行实例，该模型用于暂存所捕获的任务。

本接口需与其它接口配合使用，以便捕获 Stream 上下发的任务，暂存在内部创建的模 型中，用于后续的任务执行，以此减少 Host 侧的任务下发开销，配合使用流程请参见 1.17.1 aclmdlRICaptureBegin 接口处的说明。

在 1.17.1 aclmdlRICaptureBegin 接口中，如果将 mode 设置为非 ACL\_MODEL\_RI\_CAPTURE\_MODE\_RELAXED 的值，则本接口和 1.17.1 aclmdlRICaptureBegin 接口必须位于同一线程中。

aclError aclmdlRICaptureEnd(aclrtStream stream, aclmdlRI *modelRI)

| 参数名     | 输入 / 输出   | 说明                                       |
|---------|-----------|------------------------------------------|
| stream  | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。         |
| modelRI | 输出        | 模型运行实例，该模型用于暂存所捕获的任务。类型定义 请参见 aclmdlRI 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见单流捕获。
