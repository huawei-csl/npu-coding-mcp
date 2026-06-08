# 函数： get\_memcpy\_desc\_size

> **Section**: 2.12.36


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | x      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | √      |

获取当前 Device 的内存复制描述符占用的内存大小。

本接口需与其它关键接口配合使用，以便实现内存复制，详细描述请参见 acl.rt.memcpy\_async\_with\_desc 。

- C 函数原型 aclError aclrtGetMemcpyDescSize(aclrtMemcpyKind kind, size\_t *descSize)
- python 函数
- desc\_size, ret = acl.rt.get\_memcpy\_desc\_size(kind)

| 参数名   | 说明                                                                       |
|-------|--------------------------------------------------------------------------|
| kind  | int ，内存复制的类型。 当前仅支持 ACL_MEMCPY_INNER_DEVICE_TO_DEVICE ，表示 Device 内的内存复制。 |

| 返回值       | 说明                            |
|-----------|-------------------------------|
| desc_size | int ，内存大小，单位 Byte 。           |
| ret       | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
