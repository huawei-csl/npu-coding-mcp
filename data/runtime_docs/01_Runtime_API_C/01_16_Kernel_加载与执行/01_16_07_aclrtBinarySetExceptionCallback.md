# aclrtBinarySetExceptionCallback

> **Section**: 1.16.7


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

调用本接口注册回调函数。若多次设置回调函数，以最后一次设置为准。

在执行算子之前，调用本接口注册回调函数。如果算子执行过程中出现异常，将触发 回调函数的执行，并将异常信息存储在 aclrtExceptionInfo 结构体中。之后，可以通过 调用 aclrtGetArgsFromExceptionInfo 和 aclrtGetFuncHandleFromExceptionInfo 接 口，从异常信息中获取用户下发算子执行任务时的参数以及核函数句柄。目前，仅支 持获取 AI Core 算子执行异常时的信息。

aclError aclrtBinarySetExceptionCallback(aclrtBinHandle binHandle, aclrtOpExceptionCallback callback, void *userData)

![Figure](../../images/figure_3756.png)

**[Image: figure_3756.png (210x60, 8.5KB)]**

## 返回值说明

| 参数名       | 输入 / 输 出   | 说明                                                                                                                   |
|-----------|------------|----------------------------------------------------------------------------------------------------------------------|
| binHandle | 输入         | 算子二进制句柄。 调用 aclrtBinaryLoadFromFile 接口或 aclrtBinaryLoadFromData 接口获取算子二进制句柄， 再将其作为入参传入本接口。                           |
| callback  | 输入         | 指定要注册的回调函数。 回调函数的函数原型为： typedef void (*aclrtOpExceptionCallback)(aclrtExceptionInfo *exceptionInfo, void *userData); |
| userData  | 输入         | 待传递给回调函数的用户数据的指针。                                                                                                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
