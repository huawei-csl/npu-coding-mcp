# 函数： get\_stream\_res\_limit

> **Section**: 2.6.6


## 产品支持情况

## 功能说明

调用 acl.rt.set\_device\_res\_limit 接口设置 Device 资源限制后，可调用本接口重置当前 进程的 Device 资源限制，恢复默认配置。

- C 函数原型

aclError aclrtResetDeviceResLimit(int32\_t deviceId)

- python 函数 ret = acl.rt.reset\_device\_res\_limit(device\_id)

| 参数名       | 说明                |
|-----------|-------------------|
| device_id | int ， Device ID 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取指定 Stream 的 Device 资源限制。

## 函数原型

## 参数说明

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| value | int ，资源限制的大小。             |
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
