# aclrtUseStreamResInCurrentThread

> **Section**: 1.5.9


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

在当前线程中使用指定 Stream 上的 Device 资源限制。如果多次调用本接口设置 Stream ，将以最后一次设置为准。

aclError aclrtUseStreamResInCurrentThread(aclrtStream stream)

| 参数名    | 输入 / 输 出   | 说明                                                                                        |
|--------|------------|-------------------------------------------------------------------------------------------|
| stream | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 需先调用 aclrtSetStreamResLimit 接口设置该 Stream 上的 Device 资源限制。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
