# 函数： get\_device\_capability

> **Section**: 2.18.9


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

查询运行环境中对应 Device 的硬件规格大小。

- C 函数原型

aclError aclGetDeviceCapability(uint32\_t deviceId, aclDeviceInfo deviceInfo, int64\_t *value)

- python 函数
- value, ret = acl.get\_device\_capability(device\_id, device\_info)

| 参数名         | 说明                                                                                                                 |
|-------------|--------------------------------------------------------------------------------------------------------------------|
| device_id   | int ， Device ID 。 用户调用 acl.rt.get_device_count 接口获取可用的 Device 数量后，这 个 Device ID 的取值范围： [0, ( 可用的 Device 数量 - 1)] 。 |
| device_info | int ，指定 Device 上的硬件规格类型，具体请参见 2.19.6 aclDeviceInfo 。                                                               |

| 返回值   | 说明                            |
|-------|-------------------------------|
| value | int ，硬件规格值。                   |
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
