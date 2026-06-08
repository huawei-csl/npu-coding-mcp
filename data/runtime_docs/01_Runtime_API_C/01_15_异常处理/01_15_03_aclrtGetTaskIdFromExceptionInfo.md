# aclrtGetTaskIdFromExceptionInfo

> **Section**: 1.15.3


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

获取异常信息中的任务 ID 。该接口与 aclrtSetExceptionInfoCallback 接口配合使用。

uint32\_t aclrtGetTaskIdFromExceptionInfo(const aclrtExceptionInfo *info)

| 参数名   | 输入 / 输 出   | 说明                                                                                                                              |
|-------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| info  | 输入         | 异常信息的指针。 在执行任务之前调用 aclrtSetExceptionInfoCallback 接 口，系统会将产生异常的任务 ID 、 Stream ID 、线程 ID 、 Device ID 存放在 aclrtExceptionInfo 结构体中。 |

返回异常信息中的任务 ID ，返回值为 0xFFFFFFFF （以十六进制为例）时表示 Device 异 常。
