# aclmdlRICaptureTaskUpdateBegin

> **Section**: 1.17.7


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

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

标记待更新任务的开始。

本接口与 aclmdlRICaptureTaskUpdateEnd 接口成对使用，位于这两个接口之间的任 务需更新。

aclmdlRICaptureTaskUpdateBegin 、 aclmdlRICaptureTaskUpdateEnd 接口之间的 任务数量、任务类型必须与 aclmdlRICaptureTaskGrpBegin 、 aclmdlRICaptureTaskGrpEnd 接口之间任务数量、任务类型保持一致。

若任务更新时返回 ACL\_ERROR\_RT\_FEATURE\_NOT\_SUPPORT ，这表示底层驱动不支 持该特性，需升级驱动包。您可以单击 Link ，在'固件与驱动'页面下载对应版本的 驱动安装包，并参照其文档进行安装和升级。

- 针对 Atlas A2 训练系列产品 /Atlas A2 推理系列产品、 Atlas A3 训练系列产品 / Atlas A3 推理系列产品，需将驱动包升级到 25.0.RC1 或更高版本。
- 针对 Atlas 推理系列产品，需将驱动包升级到 26.0.RC1 或更高版本。

aclError aclmdlRICaptureTaskUpdateBegin(aclrtStream stream, aclrtTaskGrp handle)

| 参数名    | 输入 / 输出   | 说明                                                                                                                                                       |
|--------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| stream | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。 此处的 Stream 必须是不在捕获状态的 Stream 。                                                                                          |
| handle | 输入        | 标识任务组的句柄。类型定义请参见 aclrtTaskGrp 。 提前调用 aclmdlRICaptureTaskGrpBegin 、 aclmdlRICaptureTaskGrpEnd 接口标记任务组，并通过 aclmdlRICaptureTaskGrpEnd 接口获取任务组句柄，再作 为入参传入此处。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 约束说明

## 接口调用示例

对于 Atlas A2 训练系列产品 /Atlas A2 推理系列产品、 Atlas A3 训练系列产品 /Atlas A3 推理系列产品，如果 CANN 配套的 Ascend HDK 的版本为 25.5.X 之前（不包含该版 本），那么单个 Device 可支持同时更新的最大任务数是 1024*1024 个，超出该规格， 任务会在执行阶段报错。

接口调用示例，参见任务更新。
