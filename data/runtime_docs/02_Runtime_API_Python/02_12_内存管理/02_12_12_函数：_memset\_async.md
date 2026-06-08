# 函数： memset\_async

> **Section**: 2.12.12


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

初始化内存，将内存中的内容设置为指定的值，异步接口。

待初始化的内存支持在 Host 侧或 Device 侧，系统根据地址判定是 Host 还是 Device 。如 果 Host 内存不是用 acl 接口（例如 acl.rt.malloc\_host ）申请的，将会导致未定义的行 为。

## ● C 函数原型

aclError aclrtMemsetAsync(void *devPtr, size\_t maxCount, int32\_t value, size\_t count, aclrtStream stream)

- python 函数

ret = acl.rt.memset\_async(dev\_ptr, max\_count, value, count, stream)

| 参数名     | 说明            |
|---------|---------------|
| dev_ptr | int ，内存的起始地址。 |

## 返回值说明

## 约束说明

该接口是异步接口，调用接口成功仅表示任务下发成功，不表示任务执行成功。调用 该接口后，必须调用同步等待接口（例如， acl.rt.synchronize\_stream ）确保内存初 始化的任务已执行完成，否则可能会导致训练或推理等业务异常、 Device 断链掉卡等 未知情况。
