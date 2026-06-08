# aclrtSetStreamResLimit

> **Section**: 1.5.7


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

设置指定 Stream 的 Device 资源限制。

本接口应在调用 aclrtSetDevice 接口之后且在执行算子之前使用。如果对同一 Stream 进行多次设置，将以最后一次设置为准。

调用本接口设置指定 Stream 的 Device 资源限制后，需配合调用

aclrtUseStreamResInCurrentThread 接口，设置在当前线程中使用指定 Stream 上的 Device 资源限制。

aclError aclrtSetStreamResLimit(aclrtStream stream, aclrtDevResLimitType type, uint32\_t value)

| 参数名    | 输入 / 输 出   | 说明                                                        |
|--------|------------|-----------------------------------------------------------|
| stream | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 若传入 NULL ，则表示默认 Stream 。 |

## 返回值说明

| 参数名   | 输入 / 输 出   | 说明                              |
|-------|------------|---------------------------------|
| type  | 输入         | 资源类型，请参见 aclrtDevResLimitType 。 |
| value | 输入         | 资源限制的大小。                        |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
