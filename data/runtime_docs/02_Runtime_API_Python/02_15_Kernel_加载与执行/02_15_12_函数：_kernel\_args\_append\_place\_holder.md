# 函数： kernel\_args\_append\_place\_holder

> **Section**: 2.15.12


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

对于 placeholder 参数，调用本接口先占位，返回的是 param\_handle 占位符。

若参数列表中有多个参数，则需按顺序追加参数。等所有参数都追加之后，可调用 acl.rt.kernel\_args\_get\_place\_holder\_buffer 接口获取 param\_handle 占位符指向的内 存地址。

- C 函数原型 aclError aclrtKernelArgsAppendPlaceHolder(aclrtArgsHandle argsHandle, aclrtParamHandle *paramHandle)
- python 函数

param\_handle, ret = acl.rt.kernel\_args\_append\_place\_holder(args\_handle)

| 参数名         | 说明           |
|-------------|--------------|
| args_handle | int ，参数列表句柄。 |

## 返回值说明

| 返回值           | 说明                        |
|---------------|---------------------------|
| param_handl e | int ，参数句柄。                |
| ret           | int ，返回 0 表示成功，返回其他值表示失败。 |
