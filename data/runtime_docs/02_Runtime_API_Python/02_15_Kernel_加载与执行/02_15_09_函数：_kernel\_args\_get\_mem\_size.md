# 函数： kernel\_args\_get\_mem\_size

> **Section**: 2.15.9


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

获取 Kernel Launch 时参数列表所需内存的实际大小。

## ● C 函数原型

aclError aclrtKernelArgsGetMemSize(aclrtFuncHandle funcHandle, size\_t userArgsSize, size\_t *actualArgsSize)

- python 函数

actual\_args\_size, ret = acl.rt.kernel\_args\_get\_mem\_size(func\_handle, user\_args\_size)

| 参数名             | 说明                                                                                               |
|-----------------|--------------------------------------------------------------------------------------------------|
| func_handle     | int ，核函数句柄。 调用 acl.rt.binary_get_function 获取核函数句柄，再将其作为入参 传入本接口。                                 |
| user_args_siz e | int ，在内存中存放参数列表数据所需的大小，单位为 Byte 。 每个参数数据的内存大小都需要 8 字节对齐，这里的 user_args_size 是这些对齐后的参数数据内存大小相加的总和。 |

| 返回值               | 说明                                            |
|-------------------|-----------------------------------------------|
| actual_args_ size | int ， Kernel Launch 时参数列表所需内存的实际大小，单位为 Byte 。 |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
