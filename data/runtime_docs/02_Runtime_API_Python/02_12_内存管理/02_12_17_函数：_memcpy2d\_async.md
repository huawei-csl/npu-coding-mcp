# 函数： memcpy2d\_async

> **Section**: 2.12.17


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

实现异步内存复制，主要用于矩阵数据的复制。异步接口。

Atlas 推理系列加速模块产品不支持该接口。

- C 函数原型

aclError aclrtMemcpy2dAsync(void *dst, size\_t dpitch, const void *src, size\_t spitch, size\_t width, size\_t height, aclrtMemcpyKind kind, aclrtStream stream)

- python 函数
- ret = acl.rt.memcpy2d\_async(dst, dpitch, src, spitch, width, height, kind, stream)

## 参数说明

## 返回值说明

## 约束说明

| 参数名    | 说明                                                                                                                                                                                                                                                                  |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dst    | int ，目的内存地址的指针地址。                                                                                                                                                                                                                                                   |
| dpitch | int ，目的内存中相邻两列向量的地址距离。                                                                                                                                                                                                                                              |
| src    | int ，源内存地址的指针地址。                                                                                                                                                                                                                                                    |
| spitch | int ，源内存中相邻两列向量的地址距离。                                                                                                                                                                                                                                               |
| width  | int ，待复制的矩阵宽度。 width 最大设置为 5000000 ，且必须小于或等于 dpitch 和 spitch 。                                                                                                                                                                                                      |
| height | int ，待复制的矩阵高度。 ' height '最大可设置为 5 * 1024 * 1024 = 5242880 ，否则接口返回 失败。                                                                                                                                                                                               |
| kind   | int ，内存复制的类型。 ACL_MEMCPY_HOST_TO_HOST = 0 // Host 内的内存复制 ACL_MEMCPY_HOST_TO_DEVICE = 1 // Host 到 Device 的内存复制 ACL_MEMCPY_DEVICE_TO_HOST = 2 // Device 到 Host 的内存复制 ACL_MEMCPY_DEVICE_TO_DEVICE = 3 // Device 内的内存复制 ACL_MEMCPY_DEFAULT = 4 // 由系统根据源、目的内存地址自行判断拷贝方向 |
| stream | int ，指定 Stream 的指针地址。                                                                                                                                                                                                                                               |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 该接口是异步接口，调用接口成功仅表示任务下发成功，不表示任务执行成功。 调用该接口后，需调用同步等待接口（例如， acl.rt.synchronize\_stream ）确保 内存复制的任务已执行完成。
- 本接口仅支持 ACL\_MEMCPY\_HOST\_TO\_DEVICE 、 ACL\_MEMCPY\_DEVICE\_TO\_HOST 或 ACL\_MEMCPY\_DEVICE\_TO\_DEVICE 内存复 制类型，且不同型号支持的类型不同。对于不支持的内存复制类型，接口返回

ACL\_ERROR\_INVALID\_PARAM 。

- -ACL\_MEMCPY\_HOST\_TO\_DEVICE 、 ACL\_MEMCPY\_DEVICE\_TO\_HOST 类 型，以下型号支持：

Atlas 350 加速卡

Atlas A3 训练系列产品 /Atlas A3 推理系列产品

Atlas A2 训练系列产品 /Atlas A2 推理系列产品

Atlas 200I/500 A2 推理产品

Atlas 推理系列产品

Atlas 训练系列产品

- -ACL\_MEMCPY\_DEVICE\_TO\_DEVICE 类型，以下型号支持：

Atlas 350 加速卡

Atlas A3 训练系列产品 /Atlas A3 推理系列产品

Atlas A2 训练系列产品 /Atlas A2 推理系列产品

- 对于 Atlas 推理系列产品， Control CPU 开放形态下，不支持调用本接口。另外， Atlas 推理系列加速模块产品也不支持本接口
- 对于 Atlas 200I/500 A2 推理产品， Ascend RC 形态下，不支持调用本接口。
