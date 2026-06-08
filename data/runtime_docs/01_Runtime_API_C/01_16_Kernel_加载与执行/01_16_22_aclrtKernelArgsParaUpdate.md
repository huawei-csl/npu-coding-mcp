# aclrtKernelArgsParaUpdate

> **Section**: 1.16.22


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

通过 aclrtKernelArgsAppend 接口追加的参数，可调用本接口更新参数值。

## 函数原型

## 参数说明

## 返回值说明

aclError aclrtKernelArgsParaUpdate(aclrtArgsHandle argsHandle, aclrtParamHandle paramHandle, void *param, size\_t paramSize)

| 参数名          | 输入 / 输 出   | 说明                               |
|--------------|------------|----------------------------------|
| argsHandle   | 输入         | 参数列表句柄。类型定义请参见 aclrtArgsHandle 。 |
| paramHandl e | 输入         | 参数句柄。类型定义请参见 aclrtParamHandle 。  |
| param        | 输入         | 待更新参数值的内存地址。 此处为 Host 内存地址。      |
| paramSize    | 输入         | 内存大小，单位 Byte 。                   |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
