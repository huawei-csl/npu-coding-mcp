# 函数： device\_enable\_peer\_access

> **Section**: 2.7.14


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | x      |

使能当前 Device 与指定 Device 之间的数据交互。使能内存复制是 Device 级的。

可提前调用 acl.rt.device\_can\_access\_peer 接口查询当前 Device 与指定 Device 之间能 否进行数据交互。需调用两次 acl.rt.device\_enable\_peer\_access 接口使能两个 Device 之间的数据交互功能（例如，调用一次 acl.rt.device\_enable\_peer\_access 接口使能 Device 0 到 Device 1 的数据交互，再调用一次 acl.rt.device\_enable\_peer\_access 接口 使能 Device 1 到 Device 0 的数据交互）。

使能 Device 间的数据交互功能后，若想关闭该功能，可调用 acl.rt.device\_disable\_peer\_access 接口。

- C 函数原型 aclError aclrtDeviceEnablePeerAccess(int32\_t peerDeviceId, uint32\_t flags)
- python 函数

ret = acl.rt.device\_enable\_peer\_access(peer\_dev\_id, flag)

## 参数说明

## 返回值说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
