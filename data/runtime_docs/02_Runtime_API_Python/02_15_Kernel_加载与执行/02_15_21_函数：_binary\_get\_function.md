# 函数： binary\_get\_function

> **Section**: 2.15.21


## 产品支持情况

## 功能说明

- C 函数原型

aclError aclrtBinaryUnLoad(aclrtBinHandle binHandle)

- python 函数

ret = acl.rt.binary\_unload(bin\_handle)

| 参数名        | 说明                                                           |
|------------|--------------------------------------------------------------|
| bin_handle | int ，指向算子二进制的 handle 。该 handle 在调用 acl.rt.binary_load 接口时生成。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

根据 kernel\_name ，查找到对应的 kernel 对象，使用 func\_handle 表达。

## 函数原型

## 参数说明

## 返回值说明

| 返回值         | 说明                                      |
|-------------|-----------------------------------------|
| func_handle | int ，标识指定 kernel 的 func_handle 表达的指针地址。 |
| ret         | int ，错误码，返回 0 表示成功，返回其它值表示失败。           |
