# aclrtSetMemcpyDesc

> **Section**: 1.13.25


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

设置内存复制描述符，此接口调用完成后，会将源地址，目的地址、内存复制长度记 录到内存复制描述符中。

本接口需与其它关键接口配合使用，以便实现内存复制，详细描述请参见 aclrtMemcpyAsyncWithDesc 。

## 函数原型

## 参数说明

## 返回值说明

aclError aclrtSetMemcpyDesc(void *desc, aclrtMemcpyKind kind, void *srcAddr, void *dstAddr, size\_t count, void *config)

| 参数名     | 输入 / 输 出   | 说明                                                                                                                   |
|---------|------------|----------------------------------------------------------------------------------------------------------------------|
| desc    | 输出         | 内存复制描述符地址指针。 需先调用 aclrtGetMemcpyDescSize 接口获取内存描述 符所需的内存大小，再申请 Device 内存后（例如 aclrtMalloc 接口），将 Device 内存地址作为入参传入此 处。 |
| kind    | 输入         | 内存复制的类型。类型定义请参见 aclrtMemcpyKind 。 当前仅支持 ACL_MEMCPY_INNER_DEVICE_TO_DEVICE ，表示 Device 内的内存复制。                         |
| srcAddr | 输入         | 源内存地址指针。 由用户申请内存并管理内存。                                                                                               |
| dstAddr | 输入         | 目的内存地址指针。 由用户申请内存并管理内存。                                                                                              |
| count   | 输入         | 内存复制的长度，单位 Byte 。                                                                                                    |
| config  | 输入         | 预留参数，当前固定传 NULL 。                                                                                                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
