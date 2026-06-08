# 函数： device\_disable\_peer\_access

> **Section**: 2.7.15


## 产品支持情况

## 功能说明

## 函数原型

| 参数名          | 说明                                                                                                                                        |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| peer_dev_i d | int ， Device ID ，该 ID 不能与当前 Device 的 ID 相同。 用户调 acl.rt.get_device_count 接口获取可用的 Device 数量后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] 。 |
| flag         | 保留参数，当前必须设置为 0 。                                                                                                                          |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | x      |

关闭当前 Device 与指定 Device 之间的内存复制功能。关闭内存复制功能是 Device 级 的。

- C 函数原型 aclError aclrtDeviceDisablePeerAccess(int32\_t peerDeviceId)
- python 函数
- ret = acl.rt.device\_disable\_peer\_access(peer\_dev\_id)

## 参数说明

## 返回值说明

## 约束说明

需调用两次 acl.rt.device\_disable\_peer\_access 接口使能两个 Device 之间的数据交互功 能（例如，调用一次 acl.rt.device\_enable\_peer\_access 接口使能 Device 0 到 Device 1 的数据交互，再调用一次 acl.rt.device\_disable\_peer\_access 接口使能 Device 1 到 Device 0 的数据交互）。
