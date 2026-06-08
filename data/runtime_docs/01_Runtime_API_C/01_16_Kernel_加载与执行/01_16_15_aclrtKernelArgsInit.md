# aclrtKernelArgsInit

> **Section**: 1.16.15


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

根据核函数句柄初始化参数列表，并获取标识参数列表的句柄。

与 aclrtKernelArgsInitByUserMem 接口的区别在于，调用本接口表示由系统管理内 存。

aclError aclrtKernelArgsInit(aclrtFuncHandle funcHandle, aclrtArgsHandle *argsHandle)

| 参数名        | 输入 / 输 出   | 说明                                                                                                               |
|------------|------------|------------------------------------------------------------------------------------------------------------------|
| funcHandle | 输入         | 核函数句柄。类型定义请参见 aclrtFuncHandle 。 调用 aclrtBinaryGetFunctionByEntry 或 aclrtBinaryGetFunction 获取核函数句柄，再将其作为 入参传入本接口。 |
| argsHandle | 输出         | 参数列表句柄。类型定义请参见 aclrtArgsHandle 。                                                                                 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
