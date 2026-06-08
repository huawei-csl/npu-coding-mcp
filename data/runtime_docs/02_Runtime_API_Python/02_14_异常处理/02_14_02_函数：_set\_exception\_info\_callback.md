# 函数： set\_exception\_info\_callback

> **Section**: 2.14.2


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

设置异常回调函数。

- C 函数原型

aclError aclrtSetExceptionInfoCallback(aclrtExceptionInfoCallback callback)

- python 函数

ret = acl.rt.set\_exception\_info\_callback(fn)

| 参数名      | 说明                                                                                                                                        |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------|
| callback | function ，表示 Python 侧的回调函数，格式如下： def exception_callback(exception_info) """ :exception_info: 表示异常信息 aclrtExceptionInfo 的指针地址 :return: """ |

## 返回值说明

## 约束说明

## 接口调用流程

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 回调函数涉及共享资源（例如锁），因此在使用回调函数需慎重，在回调函数内 调用资源申请 &amp; 释放、 Stream 同步、 Device 同步、任务下发、任务终止等接口， 可能会导致错误或死锁。
- 您需要在执行异步任务之前，设置异常回调函数，当 Device 上的任务执行异常 时，系统会向用户设置的异常回调函数中传入一个包含任务 ID 、 Stream ID 、线程 ID 、 Device ID 以及错误码的 aclrtExceptionInfo 的指针地址，并执行回调函数，用 户可以再分别调用 acl.rt.get\_task\_id\_from\_exception\_info 、

acl.rt.get\_thread\_id\_from\_exception\_info 、

acl.rt.get\_stream\_id\_from\_exception\_info 、

acl.rt.get\_device\_id\_from\_exception\_info 、

Stream ID 、线程 ID 、 Device ID 以及错误码，便于定位问题。

acl.rt.get\_error\_code\_from\_exception\_info 接口获取产生异常的任务 ID 、

使用场景举例：例如，在调用 acl.op.execute\_v2 接口前，调用 acl.rt.set\_exception\_info\_callback 接口设置异常回调函数，当算子在 Device 执行 异常时，系统会向用户设置的异常回调函数中传入一个包含任务 ID 、 Stream ID 、 线程 ID 、 Device ID 以及错误码的 aclrtExceptionInfo 的指针地址，并执行回调函 数。

- 如果多次设置异常回调函数，以最后一次设置为准。
- 如果想清空回调函数，可再次调用 acl.rt.set\_exception\_info\_callback 接口进行重 置（传入 None 或不传入参数）。

使用场景举例：执行整网模型推理时（不支持动态 Shape 场景），如果产生 AI Core 报 错，可以调用本接口获取报错算子的描述信息，再做进一步错误排查。

## 推荐的接口调用顺序如下：

1. 定义并实现异常回调函数 fn(aclrtExceptionInfoCallback 类型 ) ，回调函数原型请 参见 acl.rt.set\_exception\_info\_callback 。

## 实现回调函数的关键步骤如下：

- a. 在异常回调函数 fn 内调用 acl.rt.get\_device\_id\_from\_exception\_info 、 acl.rt.get\_stream\_id\_from\_exception\_info 、 acl.rt.get\_task\_id\_from\_exception\_info 接口分别获取 Device ID 、 Stream ID 、 Task ID 。
- b. 在异常回调函数 fn 内调用 acl.mdl.create\_and\_get\_op\_desc 接口获取算子的描 述信息。
- c. 在异常回调函数 fn 内调用 acl.get\_tensor\_desc\_by\_index 接口获取指定算子输 入 / 输出的 Tensor 描述。
- d. 在异常回调函数 fn 内参考如下接口获取 Tensor 描述中的数据，进行进一步分 析。

## 示例代码

例如，调用 acl.get\_tensor\_desc\_address 接口获取 Tensor 数据的内存地址（用 户可从该内存地址中获取 Tensor 数据）、调用 acl.get\_tensor\_desc\_type 接口 获取 Tensor 描述中的数据类型、调用 acl.get\_tensor\_desc\_format 接口获取 Tensor 描述中的 Format 、调用 acl.get\_tensor\_desc\_num\_dims 接口获取 Tensor 描述中的 Shape 维度个数、调用 acl.get\_tensor\_desc\_dim\_v2 接口获取 Shape 中指定维度的大小。

2. 调用 acl.rt.set\_exception\_info\_callback 接口设置异常回调函数。
3. 执行模型推理。

如果存在 AI Core 报错，则触发回调函数 fn ，获取算子的信息，进行进一步分析。

调用接口后，需增加异常处理的分支，示例代码中不一一列举。以下是关键步骤的代 码示例，不可以直接拷贝运行，仅供参考。

示例中，运行时资源申请与释放请参见运行时资源申请与释放，模型加载的接口调用 流程请参见接口调用流程，模型推理的接口调用流程、准备模型推理的输入 / 输出数据 的接口调用流程请参见准备模型执行的输入 / 输出数据结构。

```
import numpy as np # ...... # 1. 申请运行时资源。 # ...... # 2. 模型加载，加载成功后，返回标识模型的 model_id 。 # ...... # 3. 创建 aclmdlDataset 类型的数据，用于描述模型的输入数据 input 、输出数据 output 。 # ...... # 4. 实现异常回调函数。 def exception_callback(info): stream_id = acl.rt.get_stream_id_from_exception_info (info) device_id = acl.rt.get_device_id_from_exception_info (info) task_id = acl.rt.get_task_id_from_exception_info (info) # 用户可以将获取的算子信息写入到文件，或者另起线程侦听异常回调，当发生异常回调时触发线程处理函 数，在线程处理函数中将算子信息打屏。 op_name, input_desc, num_inputs, output_desc, num_outputs, ret = \ acl.mdl.create_and_get_op_desc (device_id, stream_id, task_id, 256) # 可以调用 acl Tensor 的相关接口，获取算子的相关信息，用户可以根据自己需要调用。 for i in range(num_inputs): desc = acl.get_tensor_desc_by_index (input_desc, i) address = acl.get_tensor_desc_address (desc) num_dims = acl.get_tensor_desc_num_dims (desc) dim_0, ret = acl.get_tensor_desc_dim_v2 (desc, 0) for i in range(num_outputs): desc = acl.get_tensor_desc_by_index (output_desc, i) address = acl.get_tensor_desc_address (desc) num_dims = acl.get_tensor_desc_num_dims (desc) dim_0, ret = acl.get_tensor_desc_dim_v2 (desc, 0) acl.destroy_tensor_desc (input_desc) acl.destroy_tensor_desc (output_desc) # 5. 设置异常回调。 ret = acl.rt.set_exception_info_callback (exception_callback) # 6. 执行模型。 ret = acl.mdl.execute (model_id, input, output) # 7. 处理模型推理结果。
```

import acl

```
# ...... # 8. 释放描述模型输入 / 输出信息、内存等资源，卸载模型。 # ...... # 9. 释放运行时资源。 # ......
```
