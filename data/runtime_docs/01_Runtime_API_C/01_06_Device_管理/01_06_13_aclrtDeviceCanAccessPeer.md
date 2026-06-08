# aclrtDeviceCanAccessPeer

> **Section**: 1.6.13


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

查询 Device 之间是否支持数据交互。

aclError aclrtDeviceCanAccessPeer(int32\_t *canAccessPeer, int32\_t deviceId, int32\_t peerDeviceId)

| 参数名            | 输入 / 输 出   | 说明                                                                                                                                |
|----------------|------------|-----------------------------------------------------------------------------------------------------------------------------------|
| canAcces sPeer | 输出         | 是否支持数据交互， 1 表示支持， 0 表示不支持。                                                                                                        |
| deviceId       | 输入         | 指定 Device 的 ID ，不能与 peerDeviceId 参数值相同。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |
| peerDevi ceId  | 输入         | 指定 Device 的 ID ，不能与 deviceId 参数值相同。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)]     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 仅支持物理机和容器场景；
- 仅支持同一个 PCIe Switch 内 Device 之间的数据交互。 AI Server 场景下，虽然是跨 PCIe Switch ，但也支持 Device 之间的数据交互。
- 仅支持同一个物理机或容器内的 Device 之间的数据交互操作。
- 仅支持同一个进程内、线程间的 Device 之间的数据交互，不支持不同进程间 Device 之间的数据交互。
- Host 的相关端口要已使能（例如 Host BIOS 等），同一个 PCIe Switch 内 Device 之 间的拷贝才能端到端可用。

## 接口调用示例

接口调用示例，参见跨 Device 的数据交互。
