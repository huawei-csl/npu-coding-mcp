# 函数： host\_register

> **Section**: 2.12.39


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
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | x      |

将 Host 内存映射注册为 Devcie 可访问的地址，供 Device 侧网卡访问。映射后的 Device 地址不能用于内存复制操作。

本接口与 acl.rt.host\_unregister 接口成对使用。

- C 函数原型

aclError aclrtHostRegister(void *ptr, uint64\_t size, aclrtHostRegisterType type, void **devPtr)

- python 函数

dev\_ptr, ret = acl.rt.host\_register(ptr, size, type)

| 参数名   | 说明                                                                                                                                                                                           |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ptr   | int ， Host 内存地址。 Host 内存地址需 4K 页对齐。当 os 内核版本为 5.10 或更低时，使用非锁页内存会导致异常，因此必须调用 acl.rt.malloc_host 接口来申请 Host 内存；当 os 内核版本为 5.10 以上 时，支持使用非锁页的 Host 内存，因此也支持不调用 acl.rt.malloc_host 接口申请 Host 内存。 |

## 返回值说明

| 返回值     | 说明                                 |
|---------|------------------------------------|
| dev_ptr | int ， Host 内存映射成的 Device 可访问的内存地址。 |
| ret     | int ，错误码，返回 0 表示成功，返回其它值表示失败。      |
