# 函数： reset\_device

> **Section**: 2.7.2


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

复位当前运算的 Device ，释放 Device 上的资源。释放的资源包括默认 Context 、默认 Stream 以及默认 Context 下创建的所有 Stream 。若默认 Context 或默认 Stream 下的任务 还未完成，系统会等待任务完成后再释放。

- C 函数原型

aclError aclrtResetDevice(int32\_t deviceId)

- python 函数
- ret = acl.rt.reset\_device(device\_id)

| 参数名       | 说明                |
|-----------|-------------------|
| device_id | int ， Device 设备号。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

若要复位的 Device 上存在显式创建的 Context 、 Stream 、 Event ，在复位前，建议遵循 如下接口调用顺序，否则可能会导致业务异常。

## 资源参考

接口调用顺序：调用 acl.rt.destroy\_event 接口释放 Event/ 调用 acl.rt.destroy\_stream 接口释放显式创建的 Stream--&gt; 调用 acl.rt.destroy\_context 释放显式创建的 Context--&gt; 调用 acl.rt.reset\_device 接口。

接口调用流程与示例，请参见运行时资源申请与释放、同步等待。
