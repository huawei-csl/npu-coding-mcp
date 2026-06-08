# aclrtSetDeviceResLimit

> **Section**: 1.5.4


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

设置当前进程的 Device 资源限制。

本接口应在调用 aclrtSetDevice 接口之后且在执行算子之前使用。如果对同一 Device 进行多次设置，将以最后一次设置为准。

除了进程级别的 Device 资源限制，当前还支持设置 Stream 级别的 Device 资源限制，可 通过 aclrtSetStreamResLimit 、 aclrtUseStreamResInCurrentThread 接口配合使用 实现。

Device 资源限制的优先级为： Stream 级别的 Device 资源限制 &gt; 进程级别的 Device 资源 限制 &gt; AI 处理器硬件的资源限制

aclError aclrtSetDeviceResLimit(int32\_t deviceId, aclrtDevResLimitType type, uint32\_t value)

## 参数说明

## 返回值说明

## 约束说明

本接口的设置仅对后续下发的任务有效。例如在调用 aclmdlRICaptureBegin 、 aclmdlRICaptureEnd 等接口捕获 Stream 任务到模型中、再执行模型推理的场景下， 则需要在捕获之前调用本接口设置 Device 资源。
