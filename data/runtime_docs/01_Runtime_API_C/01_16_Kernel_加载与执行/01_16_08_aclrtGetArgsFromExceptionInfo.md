# aclrtGetArgsFromExceptionInfo

> **Section**: 1.16.8


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

从 aclrtExceptionInfo 异常信息中获取用户下发算子执行任务时的参数。此接口与 aclrtBinarySetExceptionCallback 接口配合使用。

aclError aclrtGetArgsFromExceptionInfo(const aclrtExceptionInfo *info, void **devArgsPtr, uint32\_t *devArgsLen)

## 参数说明

## 返回值说明

| 参数名         | 输入 / 输 出   | 说明              |
|-------------|------------|-----------------|
| info        | 输入         | 异常信息的指针。        |
| devArgsP tr | 输出         | 用户下发算子执行任务时的参数。 |
| devArgsL en | 输出         | 参数个数。           |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
