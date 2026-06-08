# 函数： device\_can\_access\_peer

> **Section**: 2.7.13


## 产品支持情况

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | x      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | x      |

查询当前 Device 的浮点计算结果输出模式。

- C 函数原型 aclError aclrtGetDeviceSatMode(aclrtFloatOverflowMode *mode)
- python 函数

无

mode, ret = acl.rt.get\_device\_sat\_mode()

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | x      |

查询 Device 之间是否支持内存复制。

- C 函数原型

aclError aclrtDeviceCanAccessPeer(int32\_t *canAccessPeer, int32\_t deviceId, int32\_t peerDeviceId)

- python 函数

can\_access\_peer, ret = acl.rt.device\_can\_access\_peer(dev\_id, peer\_dev\_id)

| 参数名          | 说明                                                                                                                                          |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| dev_id       | int ，指定 Device 的 ID ，不能与 peer_dev_id 参数值相同。 用户调用 acl.rt.get_device_count 接口获取可用的 Device 数量后，这 个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] 。 |
| peer_dev_i d | int ，指定 Device 的 ID ，不能与 dev_id 参数值相同。 用户调用 acl.rt.get_device_count 接口获取可用的 Device 数量后，这 个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] 。      |

| 返回值              | 说明                                                                                    |
|------------------|---------------------------------------------------------------------------------------|
| can_access _peer | int ，通过 dev_id 参数指定的 Device 和通过 peer_dev_id 参数指定的 Device 之间是否支持内存复制， 1 表示支持， 0 表示不支持。 |
| ret              | int ，错误码，返回 0 表示成功，返回其它值表示失败。                                                         |

- 仅支持物理机和容器场景。
- 仅支持同一个 PCIe Switch 内 Device 之间的内存复制。 AI Server 场景下，虽然是跨 PCIe Switch ，但也支持 Device 之间的内存复制。

- 仅支持同一个物理机或容器内的 Device 之间的内存复制操作。
- 仅支持同一个进程内、线程间的 Device 之间的内存复制，不支持不同进程间 Device 之间的内存复制。
- Host 的相关端口要已使能（例如 Host BIOS 等），同一个 PCIe Switch 内 Device 之 间的拷贝才能端到端可用。
