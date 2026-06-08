# 函数： create\_data\_buffer

> **Section**: 2.19.10.1


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

创建 aclDataBuffer 类型的数据，该数据类型用于描述内存地址、大小等内存信息。

如需销毁 aclDataBuffer 类型的数据，请参见 2.19.10.2 函数： destroy\_data\_buffer 。

- C 函数原型 aclDataBuffer *aclCreateDataBuffer(void *data, size\_t size)
- python 函数

output = acl.create\_data\_buffer(data, size)

| 参数名   | 说明                                                                                                                                                                                                           |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data  | int ，表示存储 aclDataBuffer 数据的指针地址。' data '参数支持 传入 0 ，表示创建一个空的数据类型，此时' size '参数值必须设 置为 0 。 该内存需由用户自行管理，调用 acl.rt.malloc 接口 / acl.rt.free 接 口申请 / 释放内存，或调用 acl.rt.malloc_host 接口 / acl.rt.free_host 接口申请 / 释放内存。 |
| size  | int ，内存大小。如果用户需要使用空 Tensor ，则在申请内存时， 内存大小最小为 1Byte ，以保障后续业务正常运行。                                                                                                                                             |

## 返回值说明

| 返回值    | 说明                           |
|--------|------------------------------|
| output | int ，输出 aclDataBuffer 的指针地址。 |
