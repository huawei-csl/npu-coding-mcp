# aclrtGetDeviceResLimit

> **Section**: 1.5.3


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

获取当前进程的 Device 资源限制。

若没有调用 aclrtSetDeviceResLimit 接口设置当前进程的 Device 资源限制，则调用本 接口获取到的是 AI 处理器硬件默认的资源限制。

aclError aclrtGetDeviceResLimit(int32\_t deviceId, aclrtDevResLimitType type, uint32\_t* value)

## 参数说明

## 返回值说明

| 参数名      | 输入 / 输出   | 说明                                                                                                     |
|----------|-----------|--------------------------------------------------------------------------------------------------------|
| deviceId | 输入        | Device ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数 量后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数 量 -1)] |
| type     | 输入        | 资源类型，请参见 aclrtDevResLimitType 。                                                                        |
| value    | 输出        | 资源限制的大小。                                                                                               |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
