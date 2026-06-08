# aclrtKernelArgsAppend

> **Section**: 1.16.19


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |
| Atlas 推理系列产品           | √      |
| Atlas 训练系列产品           | √      |

调用本接口将用户设置的参数值追加拷贝到 argsHandle 指向的参数数据区域。若参数 列表中有多个参数，则需按顺序追加参数。

如果要更新参数值，可调用 aclrtKernelArgsParaUpdate 接口进行更新。

aclError aclrtKernelArgsAppend(aclrtArgsHandle argsHandle, void *param, size\_t paramSize, aclrtParamHandle *paramHandle)

| 参数名          | 输入 / 输 出   | 说明                               |
|--------------|------------|----------------------------------|
| argsHandle   | 输入         | 参数列表句柄。类型定义请参见 aclrtArgsHandle 。 |
| param        | 输入         | 待追加参数值的内存地址。 此处为 Host 内存地址。      |
| paramSize    | 输入         | 内存大小，单位 Byte 。                   |
| paramHandl e | 输出         | 参数句柄。类型定义请参见 aclrtParamHandle 。  |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
