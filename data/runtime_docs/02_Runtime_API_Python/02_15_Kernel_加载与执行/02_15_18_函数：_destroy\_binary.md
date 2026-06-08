# 函数： destroy\_binary

> **Section**: 2.15.18


## 产品支持情况

## 功能说明

- C 函数原型

aclrtBinary aclrtCreateBinary(const void *data, size\_t dataLen)

- python 函数

binary = acl.rt.create\_binary(data, data\_len)

| 参数名      | 说明                                                                                                                         |
|----------|----------------------------------------------------------------------------------------------------------------------------|
| data     | ● int ，存放算子二进制文件（ *.o 文件）数据的内存地址指针地址。 - 应用运行在 Host 时，此处需申请 Host 上的内存；应用运行在 Device 时，此处需申请 Device 上的内存。内存申请接口请参见 2.12 内存管理。 |
| data_len | int ，内存大小，单位 Byte 。                                                                                                        |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

销毁通过 acl.rt.create\_binary 接口创建的 acl.rt.binary 类型的数据。仅支持 Ascend C 自 定义算子。

## 函数原型

## 参数说明

## 返回值说明

| 返回值   | 说明                         |
|-------|----------------------------|
| ret   | int ，返回 0 表示成功，返回非 0 表示失败。 |
