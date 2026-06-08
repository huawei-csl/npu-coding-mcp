# 函数： binary\_unload

> **Section**: 2.15.20


## 产品支持情况

## 功能说明

- C 函数原型

aclError aclrtBinaryLoad(const aclrtBinary binary, aclrtBinHandle *binHandle)

- python 函数

bin\_handle, ret= acl.rt.binary\_load(binary)

| 参数名    | 说明                                                                     |
|--------|------------------------------------------------------------------------|
| binary | int ，算子二进制信息。此处需先调用 acl.rt.create_binary 接口，获 取 acl.rt.binary 类型数据的指针。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

删除 binHandle 指向的算子二进制数据，同时也删除通过 acl.rt.binary\_load 接口拷贝 到 Device 上的算子二进制数据。仅支持 Ascend C 自定义算子。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

调用本接口删除算子二进制数据时，需跟 acl.rt.binary\_load 接口在同一个 Context 下，这样才能一并删除通过 acl.rt.binary\_load 接口拷贝到 Device 上的算子二进制数 据，否则可能会导致 Device 上的算子二进制数据删除异常。
