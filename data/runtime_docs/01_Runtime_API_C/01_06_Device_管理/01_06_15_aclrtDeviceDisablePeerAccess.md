# aclrtDeviceDisablePeerAccess

> **Section**: 1.6.15


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
| Atlas 训练系列产品                     | √      |

关闭当前 Device 与指定 Device 之间的数据交互功能。关闭数据交互功能是 Device 级 的。

调用 aclrtDeviceEnablePeerAccess 接口开启当前 Device 与指定 Device 之间的数据交互 后，可调用 aclrtDeviceDisablePeerAccess 接口关闭数据交互功能。

aclError aclrtDeviceDisablePeerAccess(int32\_t peerDeviceId)

| 参数名           | 输入 / 输 出   | 说明                                                                                                                              |
|---------------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| peerDevi ceId | 输入         | Device ID ，该 ID 不能与当前 Device 的 ID 相同。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |

## 返回值说明

## 接口调用示例

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见跨 Device 的数据交互。
