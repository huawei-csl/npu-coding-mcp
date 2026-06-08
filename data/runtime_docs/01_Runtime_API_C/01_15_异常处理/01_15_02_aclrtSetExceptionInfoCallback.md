# aclrtSetExceptionInfoCallback

> **Section**: 1.15.2


## 产品支持情况

## 功能说明

## 函数原型

获取进程级别、还是线程级别的错误描述信息由 aclInit 接口中的 err\_msg\_mode 配置控 制，默认线程级别。

建议在每次调用 acl 接口失败时都调用 aclGetRecentErrMsg 接口，以便获取调用 acl 接口 异常时的错误描述信息，用于定位问题，否则可能导致错误信息堆积、丢失。同一个 进程或线程中多次调用 aclGetRecentErrMsg 接口后，只有最后一次调用 aclGetRecentErrMsg 接口返回的错误描述字符串的指针有效，之前 aclGetRecentErrMsg 接口返回的错误描述字符串指针不能使用，否则可能导致内存非 法访问。

const char *aclGetRecentErrMsg()

无

返回错误描述字符串的指针。如果通过本接口获取到多条错误描述信息，最上面的错 误描述信息为最新的。

获取错误描述信息失败时，返回 nullptr 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

设置异常回调函数。若多次设置异常回调函数，以最后一次设置为准。

aclError aclrtSetExceptionInfoCallback(aclrtExceptionInfoCallback callback)

## 参数说明

## 返回值说明

## 约束说明

## 接口调用流程

| 参数名      | 输入 / 输 出   | 说明                                                                                                     |
|----------|------------|--------------------------------------------------------------------------------------------------------|
| callback | 输入         | 指定要注册的回调函数。 回调函数的函数原型为： typedef void (*aclrtExceptionInfoCallback)(aclrtExceptionInfo *exceptionInfo); |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 回调函数涉及共享资源（例如锁），因此在使用回调函数需慎重，在回调函数内 调用资源申请 &amp; 释放、 Stream 同步、 Device 同步、任务下发、任务终止等接口， 可能会导致错误或死锁。
- 您需要在执行异步任务之前，设置异常回调函数，当 Device 上的任务执行异常 时，系统会向用户设置的异常回调函数中传入一个包含任务 ID 、 Stream ID 、线程 ID 、 Device ID 以及错误码的 aclrtExceptionInfo 结构体指针，并执行回调函数，用 户可以再分别调用 aclrtGetTaskIdFromExceptionInfo 、

aclrtGetThreadIdFromExceptionInfo 、

aclrtGetStreamIdFromExceptionInfo 、

aclrtGetDeviceIdFromExceptionInfo 、 aclrtGetErrorCodeFromExceptionInfo

接口获取产生异常的任务 ID 、 Stream ID 、线程 ID 、 Device ID 以及错误码，便于

定位问题。

使用场景举例：例如，在调用 aclopExecuteV2 接口前，调用

aclrtSetExceptionInfoCallback 接口设置异常回调函数，当算子在 Device 执行异常 时，系统会向用户设置的异常回调函数中传入一个包含任务 ID 、 Stream ID 、线程 ID 、 Device ID 以及错误码的 aclrtExceptionInfo 结构体指针，并执行回调函数。

- 如果想清空回调函数，可调用 aclrtSetExceptionInfoCallback 接口，将入参设置为 空指针。

使用场景举例：执行整网模型推理时（不支持动态 Shape 场景），如果产生 AI Core 报 错，可以按照本章的内容获取报错算子的描述信息，再做进一步错误排查。

## 推荐的接口调用顺序如下：

1. 定义并实现异常回调函数 fn(aclrtExceptionInfoCallback 类型 ) 。 实现回调函数的关键逻辑如下：
- a. 在异常回调函数 fn 内调用 aclrtGetDeviceIdFromExceptionInfo 、 aclrtGetStreamIdFromExceptionInfo 、 aclrtGetTaskIdFromExceptionInfo 接 口分别获取 Device ID 、 Stream ID 、 Task ID 。
- b. 在异常回调函数 fn 内调用 aclmdlCreateAndGetOpDesc 接口获取算子的描述 信息。
- c. 在异常回调函数 fn 内调用 aclGetTensorDescByIndex 接口获取指定算子输入 / 输出的 tensor 描述。

## 示例代码

- d. 在异常回调函数 fn 内调用如下接口获取 tensor 描述中的数据，进行进一步分 析。

例如，调用 aclGetTensorDescAddress 接口获取 tensor 数据的内存地址（用户 可从该内存地址中获取 tensor 数据）、调用 aclGetTensorDescType 接口获取 tensor 描述中的数据类型、调用 aclGetTensorDescFormat 接口获取 tensor 描 述中的 Format 、调用 aclGetTensorDescNumDims 接口获取 tensor 描述中的 Shape 维度个数、调用 aclGetTensorDescDimV2 接口获取 Shape 中指定维度的 大小。

2. 调用 aclrtSetExceptionInfoCallback 接口设置异常回调函数。
3. 执行模型推理。

如果存在 AI Core 报错，则触发回调函数 fn ，获取算子的信息，进行进一步分析。

以下是 AI Core 异常信息获取功能的关键步骤代码示例，不能直接拷贝编译运行，仅供 参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一 一列举。

```
...... // 1. 模型加载，加载成功后，返回标识模型的 modelId // 2. 创建 aclmdlDataset 类型的数据，用于描述模型的输入数据 input 、输出数据 output // 3. 实现异常回调函数 void callback(aclrtExceptionInfo *exceptionInfo) { deviceId = aclrtGetDeviceIdFromExceptionInfo (exceptionInfo); streamId = aclrtGetStreamIdFromExceptionInfo (exceptionInfo); taskId = aclrtGetTaskIdFromExceptionInfo (exceptionInfo); char opName[256]; aclTensorDesc *inputDesc = nullptr; aclTensorDesc *outputDesc = nullptr; size_t inputCnt = 0; size_t outputCnt = 0; // 用户可以将获取的算子信息写入到文件，或者另起线程，当发生异常回调时触发线程处理函数，在线程处理 函数中将算子信息在屏幕上显示 aclmdlCreateAndGetOpDesc (deviceId, streamId, taskId, opName, 256,  &inputDesc, &inputCnt, &outputDesc, &outputCnt); // 可以调用 tensor 的相关接口，获取算子的相关信息，用户可以根据自己需要调用 for (size_t i = 0; i < inputCnt; ++i) { const aclTensorDesc *desc = aclGetTensorDescByIndex (inputDesc, i); aclGetTensorDescAddress (desc); aclGetTensorDescFormat (desc); } for (size_t i = 0; i < outputCnt; ++i) { const aclTensorDesc *desc = aclGetTensorDescByIndex (outputDesc, i); aclGetTensorDescAddress (desc); aclGetTensorDescFormat (desc); } aclDestroyTensorDesc (inputDesc); aclDestroyTensorDesc (outputDesc); } // 4. 设置异常回调 aclrtSetExceptionInfoCallback (callback); // 5. 执行模型 aclmdlExecute (modelId, input, output); // 6. 处理模型推理结果 ......
```

// 7. 释放描述模型输入 / 输出信息、内存等资源，卸载模型

......
