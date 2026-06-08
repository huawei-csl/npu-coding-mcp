# 函数： set\_device\_res\_limit

> **Section**: 2.6.4


## 产品支持情况

## 功能说明

获取当前进程的 Device 资源限制。

- C 函数原型

aclError aclrtGetDeviceResLimit(int32\_t deviceId, aclrtDevResLimitType type, uint32\_t* value)

- python 函数

value, ret = acl.rt.get\_device\_res\_limit(device\_id, type)

| 参数名       | 说明                                            |
|-----------|-----------------------------------------------|
| device_id | int ， Device ID 。                             |
| type      | int, 枚举值 , 具体请参见新增数据结构 aclrtDevResLimitType 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

设置当前进程的 Device 资源限制。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

本接口应在调用 set\_device 接口之后且在执行算子之前使用。如果对同一 Device 进行 多次设置，将以最后一次设置为准。
