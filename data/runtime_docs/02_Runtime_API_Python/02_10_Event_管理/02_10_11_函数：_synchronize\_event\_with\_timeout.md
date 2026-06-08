# 函数： synchronize\_event\_with\_timeout

> **Section**: 2.10.11


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

阻塞当前线程运行直到 Event 捕获的所有任务都执行完成（具体见 acl.rt.record\_event 接口参考 Event 捕获的细节）。

该接口在 acl.rt.synchronize\_event 接口的基础上进行了增强，支持用户设置永久等待 或配置具体的超时时间，若配置具体的超时时间，则当应用程序异常时可根据所设置 的超时时间自行退出。

- C 函数原型 aclError aclrtSynchronizeEventWithTimeout(aclrtEvent event, int32\_t timeout)
- python 函数

ret = acl.rt.synchronize\_event\_with\_timeout(event, timeout)

| 参数名     | 说明                                                                                          |
|---------|---------------------------------------------------------------------------------------------|
| event   | int ，指定需等待的 Event 对象的指针地址。                                                                  |
| timeout | int ，接口的超时时间。 取值说明如下： ● -1 ：表示永久等待与接口 acl.rt.synchronize_event 功能一致。 ● >0 ：配置具体的超时时间，单位是毫秒。 |

## 返回值说明

## 资源参考

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

接口调用示例，参见关于 Event 的同步等待。
