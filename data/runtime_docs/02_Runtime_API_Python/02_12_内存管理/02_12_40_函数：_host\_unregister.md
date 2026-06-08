# 函数： host\_unregister

> **Section**: 2.12.40


## 产品支持情况

## 功能说明

## 函数原型

| 参数名   | 说明                                                                         |
|-------|----------------------------------------------------------------------------|
| size  | int ，内存大小，单位 Byte 。                                                        |
| type  | int ，内存注册类型。当前仅支持 ACL_HOST_REGISTER_MAPPED ， 表示将 Host 内存映射注册为 Devcie 可访问的。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | x      |

取消注册 Host 内存。本接口与 acl.rt.host\_register 接口成对使用。

- C 函数原型

aclError aclrtHostUnregister(void *ptr)

- python 函数

ret = acl.rt.host\_unregister(ptr)

## 参数说明

## 返回值说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
