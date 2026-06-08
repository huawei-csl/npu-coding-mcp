# 函数： kernel\_args\_append

> **Section**: 2.15.11


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
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

调用本接口将用户设置的参数值追加拷贝到 argsHandle 指向的参数数据区域。若参数 列表中有多个参数，则需按顺序追加参数。

如果要更新参数值，可调用 acl.rt.kernel\_args\_para\_update 接口进行更新。

## ● C 函数原型

aclError aclrtKernelArgsAppend(aclrtArgsHandle argsHandle, void *param, size\_t paramSize, aclrtParamHandle *paramHandle)

- python 函数

param\_handle, ret = acl.rt.kernel\_args\_append(args\_handle, param, param\_size)

| 参数名         | 说明                              |
|-------------|---------------------------------|
| args_handle | int ，参数列表句柄。                    |
| param       | int ，待追加参数值的内存地址。此处为 Host 内存地址。 |
| param_size  | int ，内存大小，单位 Byte 。             |

## 返回值说明

| 返回值           | 说明                        |
|---------------|---------------------------|
| param_handl e | int ，参数句柄。                |
| ret           | int ，返回 0 表示成功，返回其他值表示失败。 |
