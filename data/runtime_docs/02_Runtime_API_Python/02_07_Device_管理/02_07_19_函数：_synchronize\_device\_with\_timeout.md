# 函数： synchronize\_device\_with\_timeout

> **Section**: 2.7.19


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

阻塞应用程序运行，直到正在运算中的 Device 完成运算。该接口是在 synchronize\_device 接口基础上进行了增强，支持用户设置超时时间，当应用程序异 常时可根据所设置的超时时间自行退出，超时退出时本接口返回 ACL\_ERROR\_RT\_STREAM\_SYNC\_TIMEOUT 。

多 Device 场景下，调用该接口等待的是当前 Context 对应的 Device 。

- C 函数原型 aclError aclrtSynchronizeDeviceWithTimeout(int32\_t timeout)
- python 函数

ret = acl.rt.synchronize\_device\_with\_timeout(timeout)

| 参数名     | 说明                                                                                     |
|---------|----------------------------------------------------------------------------------------|
| timeout | int ，接口的超时时间。 取值说明如下： ● -1 ：表示永久等待，和接口 synchronize_device 功能一样； ● >0 ：配置具体的超时时间，单位是毫秒。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
