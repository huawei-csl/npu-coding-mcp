# aclrtMemcpyAsyncWithCondition

> **Section**: 1.13.19


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 实现内存复制。

本接口中的 Host 内存支持锁页内存（例如通过 aclrtMallocHost 接口申请的内存）、非 锁页内存（通过 malloc 接口申请的内存）。当 Host 内存是非锁页内存时，本接口在内 存复制任务完成后才返回；当 Host 内存是锁页内存时，本接口是异步接口，调用接口 成功仅表示任务下发成功，不表示任务执行成功，调用本接口后，需调用同步等待接 口（例如， aclrtSynchronizeStream ）确保内存复制的任务已执行完成。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

aclError aclrtMemcpyAsyncWithCondition(void *dst, size\_t destMax, const void *src, size\_t count, aclrtMemcpyKind kind, aclrtStream stream)

| 参数名     | 输入 / 输 出   | 说明                                        |
|---------|------------|-------------------------------------------|
| dst     | 输入         | 目的内存地址指针。                                 |
| destMax | 输入         | 目的内存地址的最大内存长度，单位 Byte 。                   |
| src     | 输入         | 源内存地址指针。                                  |
| count   | 输入         | 内存复制的长度，单位 Byte 。                         |
| kind    | 输入         | 内存复制的类型。类型定义请参见 aclrtMemcpyKind 。         |
| stream  | 输入         | 指定执行内存复制任务的 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- Ascend EP 形态下，本接口不支持异步 Host 内的内存复制功能，若传入的 kind 为 ACL\_MEMCPY\_HOST\_TO\_HOST 时，接口返回报错 ACL\_ERROR\_RT\_FEATURE\_NOT\_SUPPORT 。
- Ascend RC 形态下，在板端运行应用时，若调用本接口传入的 kind 为 ACL\_MEMCPY\_HOST\_TO\_DEVICE 或 ACL\_MEMCPY\_DEVICE\_TO\_HOST 或 ACL\_MEMCPY\_HOST\_TO\_HOST ，系统内部将默认使用 ACL\_MEMCPY\_DEVICE\_TO\_DEVICE 执行 Device 内的内存复制。
- Control CPU 开放形态下，在 Device 上运行应用时，若调用本接口传入的 kind 为 ACL\_MEMCPY\_HOST\_TO\_DEVICE 或 ACL\_MEMCPY\_DEVICE\_TO\_HOST 或 ACL\_MEMCPY\_HOST\_TO\_HOST ，系统内部将默认使用 ACL\_MEMCPY\_DEVICE\_TO\_DEVICE 执行 Device 内的内存复制。
