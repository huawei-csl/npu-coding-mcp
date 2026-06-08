# aclrtKernelArgsInitByUserMem

> **Section**: 1.16.16


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

根据核函数句柄初始化参数列表，并获取标识参数列表的句柄。

与 aclrtKernelArgsInit 接口的区别在于，调用本接口表示由用户管理内存。

aclError aclrtKernelArgsInitByUserMem(aclrtFuncHandle funcHandle, aclrtArgsHandle argsHandle, void *userHostMem, size\_t actualArgsSize)

| 参数名             | 输入 / 输 出   | 说明                                                                                                                 |
|-----------------|------------|--------------------------------------------------------------------------------------------------------------------|
| funcHandle      | 输入         | 核函数句柄。类型定义请参见 aclrtFuncHandle 。 调用 aclrtBinaryGetFunctionByEntry 或 aclrtBinaryGetFunction 获取核函数句柄，再将其作为 入参传入本接口。   |
| argsHandle      | 输出         | 参数列表句柄。类型定义请参见 aclrtArgsHandle 。 需提前调用 aclrtKernelArgsGetHandleMemSize 接口 获取内存大小，申请 Host 内存，再将 Host 内存地址作为 入参传入此处。 |
| userHostMe m    | 输入         | Host 内存地址。 需提前调用 aclrtKernelArgsGetMemSize 接口获取内存 大小，申请 Host 内存，再将 Host 内存地址作为入参传入 此处。                             |
| actualArgsSi ze | 输入         | 内存大小。 需提前调用 aclrtKernelArgsGetMemSize 接口获取内存 大小，再将其作为入参传入此处。                                                       |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
