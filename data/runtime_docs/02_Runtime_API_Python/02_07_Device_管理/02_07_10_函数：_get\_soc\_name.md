# 函数： get\_soc\_name

> **Section**: 2.7.10


## 产品支持情况

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

查询 Device 状态是正常可用、还是异常不可用。

- C 函数原型

aclError aclrtQueryDeviceStatus(int32\_t deviceId, aclrtDeviceStatus *deviceStatus)

- python 函数
- device\_status, ret = acl.rt.query\_device\_status(device\_id)

| 参数名       | 说明                                                                                                              |
|-----------|-----------------------------------------------------------------------------------------------------------------|
| device_id | int ， Device 设备号。 用户调用 acl.rt.get_device_count 接口获取可用的 Device 数量后，该 Device ID 的取值范围为 [0, ( 可用的 Device 数量 -1)] 。 |

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 返回值   | 说明                                         |
|-------|--------------------------------------------|
| name  | str ，返回芯片版本字符串。如果通过该接口获取芯片版本失败，则返 回 None 。 |
