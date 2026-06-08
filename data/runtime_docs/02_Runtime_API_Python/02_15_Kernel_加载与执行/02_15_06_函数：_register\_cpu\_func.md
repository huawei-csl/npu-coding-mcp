# 函数： register\_cpu\_func

> **Section**: 2.15.6


## 产品支持情况

根据核函数句柄获取核函数名称。

- C 函数原型 aclError aclrtGetFunctionName(aclrtFuncHandle funcHandle, uint32\_t maxLen, char *name)
- python 函数

func\_name, ret = acl.rt.get\_function\_name(func\_handle, max\_len)

| 参数名         | 说明                                                    |
|-------------|-------------------------------------------------------|
| func_handle | int ，核函数句柄。                                           |
| max_len     | int ，用户申请用于存储核函数名称的最大内存大小，单位 Byte 。取 值范围： [0, 1024) 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 返回值         | 说明                        |
|-------------|---------------------------|
| func_handle | int ，核函数句柄。               |
| ret         | int ，返回 0 表示成功，返回其他值表示失败。 |
