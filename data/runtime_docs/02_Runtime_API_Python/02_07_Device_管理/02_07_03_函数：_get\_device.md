# 函数： get\_device

> **Section**: 2.7.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取当前正在使用的 Device 的 ID 。

- C 函数原型

aclError aclrtGetDevice(int32\_t *deviceId)

- python 函数

device\_id, ret = acl.rt.get\_device()

| 参数名       | 说明             |
|-----------|----------------|
| device_id | Device ID 的指针。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

## 约束说明

如果没有提前指定 Device ，则调用 acl.rt.get\_device 接口时，返回错误。指定 Device 的 方式包括：在 init 接口中开启默认 Device 、调用 acl.rt.set\_device 接口显式指定 Device 、调用 acl.rt.create\_context 接口隐式指定 Device 。
