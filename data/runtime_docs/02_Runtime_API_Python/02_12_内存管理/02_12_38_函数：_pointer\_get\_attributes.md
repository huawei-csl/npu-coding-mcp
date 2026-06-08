# 函数： pointer\_get\_attributes

> **Section**: 2.12.38


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 参数名    | 说明                |
|--------|-------------------|
| config | int ，预留参数，当前固定传 0 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | x      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取内存属性信息，包括内存是位于 Host 还是 Device 、页表大小等信息。

- C 函数原型

aclError aclrtPointerGetAttributes(const void *ptr, aclrtPtrAttributes *attributes)

- python 函数

attributes, ret = acl.rt.pointer\_get\_attributes(ptr)

| 参数名   | 说明         |
|-------|------------|
| ptr   | int ，内存地址。 |

## 返回值说明

| 返回值        | 说明                                              |
|------------|-------------------------------------------------|
| attributes | dict ，内存属性信息，具体请参见 2.19.43 aclrtPtrAttributes 。 |
| ret        | int ，错误码，返回 0 表示成功，返回其它值表示失败。                   |
