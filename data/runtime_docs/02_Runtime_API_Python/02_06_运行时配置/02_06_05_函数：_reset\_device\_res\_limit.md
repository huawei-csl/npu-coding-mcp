# 函数： reset\_device\_res\_limit

> **Section**: 2.6.5


## 产品支持情况

- C 函数原型

aclError aclrtSetDeviceResLimit(int32\_t deviceId, aclrtDevResLimitType type, uint32\_t value)

- python 函数

ret = acl.rt.set\_device\_res\_limit(device\_id, type, value)

| 参数名       | 说明                                            |
|-----------|-----------------------------------------------|
| device_id | int ， Device ID 。                             |
| type      | int, 枚举值 , 具体请参见新增数据结构 aclrtDevResLimitType 。 |
| value     | int ，资源限制的大小。                                 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | x      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
