# 函数： memcpy\_async\_with\_condition

> **Section**: 2.12.15


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

实现内存复制。

本接口在 aclrtMemcpyAsync 接口基础上扩展了功能，当传入的内存不是通过 pyacl 提 供的接口申请的，本接口在内存复制完成后才会返回；否则本接口是异步接口，调用 接口成功仅表示任务下发成功，不表示任务执行成功，调用本接口后，需调用同步等 待接口（例如， acl.rt.synchronize\_stream ）确保内存复制的任务已执行完成。

- C 函数原型

aclError aclrtMemcpyAsyncWithCondition(void *dst, size\_t destMax, const void *src, size\_t count, aclrtMemcpyKind kind, aclrtStream stream)

- python 函数

ret = acl.rt.memcpy\_async\_with\_condition(dst, dest\_max, src, count, kind, stream)

| 参数名     | 说明                           |
|---------|------------------------------|
| dst     | int ，目的内存地址指针。               |
| destMax | int ，目的内存地址的最大内存长度，单位 Byte 。 |
| src     | int ，源内存地址指针。                |
| count   | int ，内存复制的长度，单位 Byte 。       |

## 返回值说明

## 约束说明

| 参数名    | 说明                                                                                                                                                                                                                                                                              |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| kind   | int ，内存复制的类型。 ● 0 ： ACL_MEMCPY_HOST_TO_HOST ， Host 内的内存复制。 ● 1 ： ACL_MEMCPY_HOST_TO_DEVICE ， Host 到 Device 的内存复 制。 ● 2 ： ACL_MEMCPY_DEVICE_TO_HOST ， Device 到 Host 的内存复 制。 ● 3 ： ACL_MEMCPY_DEVICE_TO_DEVICE ， Device 内的内存复制。 ● 4 ： ACL_MEMCPY_DEFAULT ，由系统根据源、目的内存地址自行 判断拷贝方向。 |
| stream | int ，指定 stream 。                                                                                                                                                                                                                                                                |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

## Atlas 推理系列产品：

- Ascend EP 形态下，本接口不支持异步 Host 内的内存复制功能，若传入的 kind 为 ACL\_MEMCPY\_HOST\_TO\_HOST 时，接口返回报错 ACL\_ERROR\_RT\_FEATURE\_NOT\_SUPPORT 。

## Atlas 200I/500 A2 推理产品：

- Ascend EP 形态下，本接口不支持异步 Host 内的内存复制功能，若传入的 kind 为 ACL\_MEMCPY\_HOST\_TO\_HOST 时，接口返回报错 ACL\_ERROR\_RT\_FEATURE\_NOT\_SUPPORT 。
- Ascend RC 形态下，在板端运行应用时，若调用本接口传入的 kind 为 ACL\_MEMCPY\_HOST\_TO\_DEVICE 、 ACL\_MEMCPY\_DEVICE\_TO\_HOST 或 ACL\_MEMCPY\_HOST\_TO\_HOST ，系统内部会默认使用 ACL\_MEMCPY\_DEVICE\_TO\_DEVICE 执行 Device 内的内存复制。

Atlas 训练系列产品、 Atlas A2 训练系列产品 /Atlas A2 推理系列产品、 Atlas A3 训练 系列产品 /Atlas A3 推理系列产品：

- 本接口不支持异步 Host 内的内存复制功能，若传入的 kind 为 ACL\_MEMCPY\_HOST\_TO\_HOST 时，接口返回报错 ACL\_ERROR\_RT\_FEATURE\_NOT\_SUPPORT 。
