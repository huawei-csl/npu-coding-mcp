# 函数： synchronize\_stream\_with\_timeout

> **Section**: 2.9.10


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

阻塞应用程序运行，直到指定 Stream 中的所有任务都完成，该接口是在 acl.rt.synchronize\_stream 接口基础上进行了增强，支持用户设置超时时间，当应用 程序异常时可根据所设置的超时时间自行退出。

- C 函数原型

aclError aclrtSynchronizeStreamWithTimeout(aclrtStream stream, int32\_t timeout)

- python 函数

ret = acl.rt.synchronize\_stream\_with\_timeout(stream, timeout)

| 参数名     | 说明                                                                                           |
|---------|----------------------------------------------------------------------------------------------|
| stream  | int ，指定需要完成所有任务的 Stream 的指针地址。                                                               |
| timeout | int ，接口的超时时间。取值说明如下： ● -1 ：表示永久等待，和接口 acl.rt.synchronize_stream 功能一样。 ● >0 ：配置具体的超时时间，单位是毫秒。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
