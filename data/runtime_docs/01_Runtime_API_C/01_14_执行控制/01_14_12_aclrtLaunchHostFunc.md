# aclrtLaunchHostFunc

> **Section**: 1.14.12


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

在 Stream 的任务队列中下发一个 Host 回调任务，系统内部在执行到该回调任务时，会 在 Stream 上注册的线程（该线程在本接口内部创建并注册）中执行回调函数，并且回 调任务默认阻塞本 Stream 上后续任务的执行。异步接口。

本接口可用于实现异步场景下的 callback 功能，与另一套实现异步场景下的 callback 功 能接口（ aclrtLaunchCallback 、 aclrtSubscribeReport 、 aclrtProcessReport 、 aclrtUnSubscribeReport ）的差别在于：使用 aclrtLaunchCallback 等接口时， Stream 上注册的线程需由用户自行创建并通过 aclrtSubscribeReport 接口注册，另外也可以 指定回调任务是否阻塞本 Stream 上后续任务的执行。

对于同一个 Stream ，两套实现异步场景下的 callback 功能的接口不能混用，否则可能 出现异常。

aclError aclrtLaunchHostFunc(aclrtStream stream, aclrtHostFunc fn, void *args)

| 参数名    | 输入 / 输 出   | 说明                                      |
|--------|------------|-----------------------------------------|
| stream | 输入         | 指定执行回调任务的 Stream 。类型定义请参见 aclrtStream 。 |

## 返回值说明

## 约束说明

## 接口调用示例

| 参数名   | 输入 / 输 出   | 说明                                                                |
|-------|------------|-------------------------------------------------------------------|
| fn    | 输入         | 指定要增加的回调函数。 回调函数的函数原型为： typedef void (*aclrtHostFunc)(void *args) |
| args  | 输入         | 待传递给回调函数的用户数据。                                                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

回调函数涉及共享资源（例如锁），因此在使用回调函数需慎重，不应该调用资源申 请、资源释放、 Stream 同步、 Device 同步、任务下发、任务终止等接口，否则可能导 致错误或死锁。

接口调用示例，参见 Host 回调任务。
