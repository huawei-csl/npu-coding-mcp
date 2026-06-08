# 函数： get\_device\_utilization\_rate

> **Section**: 2.7.8


## 产品支持情况

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 训练系列产品           | √      |
| Atlas 推理系列产品           | √      |
| Atlas 200I/500 A2 推理产品 | √      |

获取可用 Device 的数量。

- C 函数原型

aclError aclrtGetDeviceCount(uint32\_t *count)

- python 函数

count, ret = acl.rt.get\_device\_count()

无

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

查询 Device 上 Cube 、 Vector 、 AI CPU 等的利用率。

## ● C 函数原型

aclError aclrtGetDeviceUtilizationRate(int32\_t deviceId, aclrtUtilizationInfo *utilizationInfo)

## ● python 函数

utilization\_info, ret = acl.rt.get\_device\_utilization\_rate(device\_id)

| 参数名       | 说明                                                                                                               |
|-----------|------------------------------------------------------------------------------------------------------------------|
| device_id | int ， Device 设备号。 用户调用 acl.rt.get_device_count 接口获取可用的 Device 数量后， 该 Device ID 的取值范围为 [0, ( 可用的 Device 数量 -1)] 。 |

| 返回值               | 说明                                                                        |
|-------------------|---------------------------------------------------------------------------|
| utilization_ info | dict ， aclrtUtilizationInfo 类型利用率信息字典，具体请参见 17.43- aclrtUtilizationInfo 。 |
| ret               | int ，错误码，返回 0 表示成功，返回其它值表示失败。                                             |

- 昇 腾虚拟化实例场景下，不支持调用本接口查询利用率，接口返回值无实际意 义。
- 开启 Profiling 功能时，不支持调用本接口查询利用率，接口返回值无实际意义。
- 查询 Device 内存利用率为预留功能，当前版本不支持，若调用本接口查询内存利 用率，查询到的利用率为 -1 。
- Atlas 训练系列产品上没有 Vector ，调用本接口查询 Vector 利用率时，查询到的利 用率为 -1 。
