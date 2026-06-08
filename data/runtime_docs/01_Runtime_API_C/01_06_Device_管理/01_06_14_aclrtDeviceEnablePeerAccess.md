# aclrtDeviceEnablePeerAccess

> **Section**: 1.6.14


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

开启当前 Device 与指定 Device 之间的数据交互。开启数据交互是 Device 级的。

调用本接口开启 Device 之间的数据交互是单向的。例如，当前 Device ID 为 0 ，调用 aclrtDeviceEnablePeerAccess 接口指定 Device ID 为 1 后，仅 Device 0 到 Device 1 方向的 数据交互是可行的。若要启用 Device 1 到 Device 0 方向的数据交互，则需将当前 Device 切换至 Device 1 ，并再次调用 aclrtDeviceEnablePeerAccess 接口指定 Device ID 0 ，此 时 Device 1 到 Device 0 方向的数据交互才能实现。

可提前调用 aclrtDeviceCanAccessPeer 接口查询当前 Device 与指定 Device 之间能否进 行数据交互。开启 Device 间的数据交互功能后，若想关闭该功能，可调用 aclrtDeviceDisablePeerAccess 接口。

aclError aclrtDeviceEnablePeerAccess(int32\_t peerDeviceId, uint32\_t flags)

| 参数名           | 输入 / 输 出   | 说明                                                                                                                                 |
|---------------|------------|------------------------------------------------------------------------------------------------------------------------------------|
| peerDevi ceId | 输入         | 指定 Device ID ，该 ID 不能与当前 Device 的 ID 相同。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |
| flags         | 输入         | 保留参数，当前必须设置为 0 。                                                                                                                   |

## 返回值说明

## 约束说明

## 接口调用示例

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

Atlas 推理系列产品， Control CPU 开放形态下，应用程序运行在 Device 的 Control CPU 上时，该接口不支持 Device 之间的数据交互。

接口调用示例，参见跨 Device 的数据交互。
