# 函数： kernel\_args\_get\_handle\_mem\_size

> **Section**: 2.15.10


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
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取参数列表句柄占用的内存大小。

- C 函数原型

aclError aclrtKernelArgsGetHandleMemSize(aclrtFuncHandle funcHandle, size\_t *memSize)

- python 函数

mem\_size, ret = acl.rt.kernel\_args\_get\_handle\_mem\_size(func\_handle)

| 参数名         | 说明                                                               |
|-------------|------------------------------------------------------------------|
| func_handle | int ，核函数句柄。 调用 acl.rt.binary_get_function 获取核函数句柄，再将其作为入参 传入本接口。 |

| 返回值      | 说明                            |
|----------|-------------------------------|
| mem_size | int ，参数列表句柄占用的内存大小，单位为 Byte 。 |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
