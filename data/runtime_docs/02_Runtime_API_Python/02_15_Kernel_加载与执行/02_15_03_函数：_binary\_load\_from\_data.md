# 函数： binary\_load\_from\_data

> **Section**: 2.15.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

从内存加载并解析 AI CPU 算子二进制数据，输出指向算子二进制的 binHandle 。

调用本接口用于加载 AI CPU 算子信息（ aclrtBinaryLoadOptions 中的 option\_type 包含 ACL\_RT\_BINARY\_LOAD\_OPT\_CPU\_KERNEL\_MODE ）时，还需配合使用 acl.rt.register\_cpu\_func 接口注册 AI CPU 算子信息。

## ● C 函数原型

aclError aclrtBinaryLoadFromData(const void *data, size\_t length, const aclrtBinaryLoadOptions *options, aclrtBinHandle *binHandle)

- python 函数

bin\_handle, ret = acl.rt.binary\_load\_from\_data(mem\_addr, length, options)

| 参数名      | 说明                                  |
|----------|-------------------------------------|
| mem_addr | int ，存放算子二进制数据的 Host 内存地址，不能为空。     |
| length   | int ，算子二进制数据的内存大小，必须大于 0 ，单位 Byte 。 |

## 返回值说明

| 返回值        | 说明                        |
|------------|---------------------------|
| bin_handle | int ，标识算子二进制的句柄。          |
| ret        | int ，返回 0 表示成功，返回其他值表示失败。 |
