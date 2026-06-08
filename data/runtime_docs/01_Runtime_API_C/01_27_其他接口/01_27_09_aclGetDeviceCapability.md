# aclGetDeviceCapability

> **Section**: 1.27.9


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

查询运行环境中对应 Device 的硬件规格大小。

aclError aclGetDeviceCapability(uint32\_t deviceId, aclDeviceInfo deviceInfo, int64\_t *value)

| 参数名         | 输入 / 输 出   | 说明                                                                                                    |
|-------------|------------|-------------------------------------------------------------------------------------------------------|
| deviceId    | 输入         | Device ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |
| deviceInf o | 输入         | 指定 Device 上的硬件规格类型。类型定义请参见 aclDeviceInfo 。                                                            |
| value       | 输出         | 硬件规格值。                                                                                                |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
