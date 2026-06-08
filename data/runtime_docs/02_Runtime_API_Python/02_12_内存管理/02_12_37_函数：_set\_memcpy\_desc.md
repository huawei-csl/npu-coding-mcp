# 函数： set\_memcpy\_desc

> **Section**: 2.12.37


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | x      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | √      |

设置内存复制描述符，此接口调用完成后，会将源地址，目的地址、内存复制长度记 录到内存复制描述符中。

本接口需与其它关键接口配合使用，以便实现内存复制，详细描述请参见 acl.rt.memcpy\_async\_with\_desc 。

## ● C 函数原型

aclError aclrtSetMemcpyDesc(void *desc, aclrtMemcpyKind kind, void *srcAddr, void *dstAddr, size\_t count, void *config)

## ● python 函数

desc, ret = acl.rt.set\_memcpy\_desc(desc, kind, src\_addr, dst\_addr, count, config)

| 参数名      | 说明                                                                                                                              |
|----------|---------------------------------------------------------------------------------------------------------------------------------|
| desc     | int ，内存复制描述符地址指针。 需先调用 acl.rt.get_memcpy_desc_size 接口获取内存描述符所需的 内存大小，再申请 Device 内存后（例如 acl.rt.malloc 接口），将 Device 内存地址作为入参传入此处。 |
| kind     | int ，内存复制的类型。当前仅支持 ACL_MEMCPY_INNER_DEVICE_TO_DEVICE ，表示 Device 内的内存 复制。                                                        |
| src_addr | int ，源内存地址指针。由用户申请内存并管理内存。                                                                                                      |
| dst_addr | int ，目的内存地址指针。由用户申请内存并管理内存。                                                                                                     |
| count    | int ，内存复制的长度，单位 Byte 。                                                                                                          |

## 返回值说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| desc  | int ，内存复制描述符地址指针。             |
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
