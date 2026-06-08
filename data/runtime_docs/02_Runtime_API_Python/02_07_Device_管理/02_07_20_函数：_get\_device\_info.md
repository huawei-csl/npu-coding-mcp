# 函数： get\_device\_info

> **Section**: 2.7.20


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

获取指定 Device 的信息。

- C 函数原型

aclError aclrtGetDeviceInfo(uint32\_t deviceId, aclrtDevAttr attr, int64\_t *value)

- python 函数

value, ret = acl.rt.get\_device\_info(device\_Id, attr)

| 参数名       | 说明                                  |
|-----------|-------------------------------------|
| device_id | int ， Device ID 。                   |
| attr      | int, 枚举值，具体请参见新增数据结构 aclrtDevAttr 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
| value | int ， device 属性值。             |
