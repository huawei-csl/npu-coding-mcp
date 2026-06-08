# 函数： malloc\_with\_cfg

> **Section**: 2.12.32


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

在 Device 上分配 size 大小的线性内存，并通过 dev\_ptr 返回已分配内存的指针。

与 acl.rt.malloc 接口相比，本接口在申请内存时，还可以指定内存相关的配置信息。

使用本接口申请的内存，需要通过 acl.rt.free 接口释放内存。

- C 函数原型 aclError aclrtMallocWithCfg(void **devPtr, size\_t size, aclrtMemMallocPolicy policy, aclrtMallocConfig

*cfg)

- python 函数
- dev\_ptr, ret = acl.rt.malloc\_with\_cfg(size, policy, cfg)

## 参数说明

## 返回值说明

| 返回值    | 说明                            |
|--------|-------------------------------|
| devPtr | int ，指向 Device 上已分配内存的指针地址。   |
| ret    | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
