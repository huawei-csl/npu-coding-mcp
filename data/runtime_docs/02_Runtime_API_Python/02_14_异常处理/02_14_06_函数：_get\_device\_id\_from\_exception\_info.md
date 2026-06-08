# 函数： get\_device\_id\_from\_exception\_info

> **Section**: 2.14.6


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取异常信息中的 Device ID 。

- C 函数原型 uint32\_t aclrtGetDeviceIdFromExceptionInfo(const aclrtExceptionInfo *info)
- python 函数
- device\_id = acl.rt.get\_device\_id\_from\_exception\_info(info)

| 参数名   | 说明                                                                                                                                                             |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| info  | int ，表示异常信息 aclrtExceptionInfo 的指针地址。 在执行任务之前调用 acl.rt.set_exception_info_callback 接口，系 统会将产生异常的任务 ID 、 Stream ID 、线程 ID 、 Device ID 存放在 aclrtExceptionInfo 中。 |

## 返回值说明

| 返回值       | 说明                                                              |
|-----------|-----------------------------------------------------------------|
| device_id | int ，返回异常信息中的 Device 设备号，返回值为' 0xFFFFFFFF ' （以十六进制为例）时表示异常信息为空。 |
