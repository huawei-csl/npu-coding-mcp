# 函数： device\_task\_abort

> **Section**: 2.14.8


## 功能说明

## 函数原型

## 参数说明

## 返回值说明

停止指定 Device 上的正在执行的任务，同时丢弃指定 Device 上已下发的任务。该接口 支持用户设置永久等待、或配置具体的超时时间，若配置具体的超时时间，则调用本 接口超出超时时间，则接口返回报错。

- C 函数原型

aclError aclrtDeviceTaskAbort(int32\_tdeviceId,uint32\_ttimeout);

- python 函数
- ret=acl.rt.device\_task\_abort(device\_id,timeout)

| 参数名      | 说明                                                                   |
|----------|----------------------------------------------------------------------|
| deviceId | int ， Device ID 。与 set_device 接口中 Device ID 保持一致。                    |
| timeout  | int ，超时时间。 取值说明如下： ● 0 ：表示永久等待； ● >0 ：配置具体的超时时间，单位是毫秒。最大超时时间 36 分 钟。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

## 须知

本接口为预留接口，暂不支持。
