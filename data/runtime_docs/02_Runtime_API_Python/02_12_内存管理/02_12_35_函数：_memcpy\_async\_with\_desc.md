# 函数： memcpy\_async\_with\_desc

> **Section**: 2.12.35


## 产品支持情况

申请 Host 内存（该内存是锁页内存），由系统保证内存首地址 64 字节对齐。与 acl.rt.malloc\_host 接口相比，本接口在申请内存时，还可以指定内存相关的配置信 息。

针对 Ascend RC 形态、 Control CPU 开放形态， Host 与 Device 是合一的，所以申请 Host 内存也等同于申请 Device 内存。此外，申请内存时，按普通页申请。如果需要 64 字节 对齐的首地址，用户需自行处理对齐问题。

- C 函数原型

aclError aclrtMallocHostWithCfg(void **ptr, uint64\_t size, aclrtMallocConfig *cfg)

- python 函数

host\_ptr, ret= acl.rt.malloc\_host\_with\_cfg(size, cfg)

| 参数名   | 说明                                                            |
|-------|---------------------------------------------------------------|
| size  | int ，申请内存的大小，单位 Byte 。 size 不能为 0 。                           |
| cfg   | dict ，内存配置信息。不指定配置时，此处可传空字典，具体请参见 2.19.35 aclrtMallocConfig 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | x      |
| Atlas 推理系列产品                      | x      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |

使用内存复制描述符（二级指针方式）进行内存复制。

本接口是异步接口，调用接口成功仅表示任务下发成功，不表示任务执行成功。调用 该接口后，需调用同步等待接口（例如， acl.rt.synchronize\_stream ）确保任务已执 行完成，否则可能会导致训练或推理等业务异常、 Device 断链掉卡等未知情况。

## 本接口需与以下其它关键接口配合使用，以便实现内存复制：

- 调用 acl.rt.get\_memcpy\_desc\_size 接口获取内存描述符所需的内存大小。
- 申请 Device 内存，用于存放内存描述符。
- 申请源内存、目的内存，分别用于存放复制前后的数据。
- 调用 acl.rt.set\_memcpy\_desc 接口将源内存地址、目的内存地址等信息设置到内 存描述符中。
- 调用 acl.rt.memcpy\_async\_with\_desc 接口实现内存复制。
- C 函数原型 aclError aclrtMemcpyAsyncWithDesc(void *desc, aclrtMemcpyKind kind, aclrtStream stream)
- python 函数

ret= acl.rt.memcpy\_async\_with\_desc(desc, kind, stream)

| 参数名    | 说明                                                                                                |
|--------|---------------------------------------------------------------------------------------------------|
| desc   | int ，内存复制描述符地址指针， Device 侧内存地址。此处需先调用 acl.rt.set_memcpy_desc 接口设置内存复制描述符，再将内存复制 描述符地址指针作为入参传入本接口。 |
| kind   | int ，内存复制的类型。当前仅支持 ACL_MEMCPY_INNER_DEVICE_TO_DEVICE ，表示 Device 内的内存 复制。                          |
| stream | int ，指定 stream 。                                                                                  |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
