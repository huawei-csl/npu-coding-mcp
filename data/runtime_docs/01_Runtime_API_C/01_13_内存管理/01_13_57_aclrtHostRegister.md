# aclrtHostRegister

> **Section**: 1.13.57


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | √      |

将 Host 内存映射注册为 Device 可访问的内存地址，并获取映射后的 Device 内存地址。 映射后的 Device 内存地址不能用于内存操作，例如内存复制。

如果注册的 ptr 是通过 aclrtMallocHostWithCfg 申请的，并且申请时配置的 attr 类型是 ACL\_RT\_MEM\_ATTR\_VA\_FLAG ， vaFlag 的值为 1 ，则映射后的 Device 地址与 Host 地址 一致，可以进行内存操作。

取消注册 Host 内存需调用 aclrtHostUnregister 接口。

aclError aclrtHostRegister(void *ptr, uint64\_t size, aclrtHostRegisterType type, void **devPtr)

## 参数说明

## 返回值说明

| 参数名    | 输入 / 输 出   | 说明                                                                                                                                                                                                                    |
|--------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ptr    | 输入         | Host 内存地址。 Host 内存地址需 4K 页对齐。 当 os 内核版本为 5.10 或更低时，使用非锁页内存会导致 异常，因此必须调用 aclrtMallocHost 接口来申请 Host 锁 页内存。 当 os 内核版本为 5.10 以上时，支持使用非锁页的 Host 内 存，因此既支持调用 aclrtMallocHost 接口申请 Host 锁页 内存，也支持使用 malloc 接口申请 Host 非锁页内存。 |
| size   | 输入         | 内存大小，单位 Byte 。                                                                                                                                                                                                        |
| type   | 输入         | 内存注册类型。类型定义请参见 aclrtHostRegisterType 。                                                                                                                                                                                |
| devPtr | 输出         | Host 内存映射成的 Device 可访问的内存地址。                                                                                                                                                                                          |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
