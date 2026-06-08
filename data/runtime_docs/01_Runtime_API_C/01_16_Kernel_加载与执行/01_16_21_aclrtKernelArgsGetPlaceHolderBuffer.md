# aclrtKernelArgsGetPlaceHolderBuffer

> **Section**: 1.16.21


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

根据用户指定的内存大小，获取 paramHandle 占位符指向的内存地址。

aclError aclrtKernelArgsGetPlaceHolderBuffer(aclrtArgsHandle argsHandle, aclrtParamHandle paramHandle, size\_t dataSize, void **bufferAddr)

| 参数名          | 输入 / 输 出   | 说明                                                                                                         |
|--------------|------------|------------------------------------------------------------------------------------------------------------|
| argsHandle   | 输入         | 参数列表句柄。类型定义请参见 aclrtArgsHandle 。                                                                           |
| paramHandl e | 输入         | 参数句柄。类型定义请参见 aclrtParamHandle 。 此处的 paramHandle 需与 aclrtKernelArgsAppendPlaceHolder 接口中的 paramHandle 保持一致。 |
| dataSize     | 输入         | 内存大小。                                                                                                      |
| bufferAddr   | 输出         | paramHandle 占位符指向的内存地址。 后续由用户管理该内存中的数据，但无需管理该内存的 生命周期。                                                     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
