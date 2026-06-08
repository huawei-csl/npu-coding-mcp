# aclrtKernelArgsAppendPlaceHolder

> **Section**: 1.16.20


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | √      |
| Atlas 训练系列产品 | √      |

对于 placeholder 参数，调用本接口先占位，返回的是 paramHandle 占位符。

若参数列表中有多个参数，则需按顺序追加参数。等所有参数都追加之后，可调用 aclrtKernelArgsGetPlaceHolderBuffer 接口获取 paramHandle 占位符指向的内存地 址。

aclError aclrtKernelArgsAppendPlaceHolder(aclrtArgsHandle argsHandle, aclrtParamHandle *paramHandle)

| 参数名          | 输入 / 输 出   | 说明                               |
|--------------|------------|----------------------------------|
| argsHandle   | 输入         | 参数列表句柄。类型定义请参见 aclrtArgsHandle 。 |
| paramHandl e | 输出         | 参数句柄。类型定义请参见 aclrtParamHandle 。  |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
