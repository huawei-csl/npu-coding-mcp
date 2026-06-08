# aclrtPeekAtLastError

> **Section**: 1.15.8


## 产品支持情况

## 功能说明

## 函数原型

uint32\_t aclrtGetErrorCodeFromExceptionInfo(const aclrtExceptionInfo *info)

| 参数名   | 输入 / 输 出   | 说明                                                                                                                                  |
|-------|------------|-------------------------------------------------------------------------------------------------------------------------------------|
| info  | 输入         | 异常信息的指针。 在执行任务之前调用 aclrtSetExceptionInfoCallback 接 口，系统会将产生异常的任务 ID 、 Stream ID 、线程 ID 、 Device ID 、错误码存放在 aclrtExceptionInfo 结构体中。 |

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取当前线程的 Runtime （运行时管理模块）错误码，仅获取但不清空错误码。

aclError aclrtPeekAtLastError(aclrtLastErrLevel level)

## 参数说明

## 返回值说明

## 接口调用示例

| 参数名   | 输入 / 输 出   | 说明                                                |
|-------|------------|---------------------------------------------------|
| level | 输入         | 指定获取错误码的级别，当前仅支持线程级别。类型定 义请参见 aclrtLastErrLevel 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见获取 Runtime 错误码。
