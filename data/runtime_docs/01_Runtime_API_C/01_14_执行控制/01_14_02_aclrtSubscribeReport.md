# aclrtSubscribeReport

> **Section**: 1.14.2


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

注册处理 Stream 上回调函数的线程。

## 本接口需与以下其它接口配合使用，以便实现异步场景下的 callback 功能：

1. 定义并实现回调函数，函数原型为： typedef void (*aclrtCallback)(void *userData) ；
2. 新建线程，在线程函数内，调用 aclrtProcessReport 接口设置超时时间（需循环 调用），等待回调任务执行；
3. 调用 aclrtSubscribeReport 接口建立第 2 步中的线程和 Stream 的绑定关系，该 Stream 下发的回调函数将在绑定的线程中执行；
4. 在指定 Stream 上执行异步任务（例如异步推理任务）；
5. 调用 aclrtLaunchCallback 接口在 Stream 的任务队列中下发回调任务，触发第 2 步 中注册的线程处理回调函数，每调用一次 aclrtLaunchCallback 接口，就会触发一 次回调函数的执行；
6. 异步任务全部执行完成后，取消线程注册（ aclrtUnSubscribeReport 接口）。

aclError aclrtSubscribeReport(uint64\_t threadId, aclrtStream stream)

| 参数名      | 输入 / 输出   | 说明                               |
|----------|-----------|----------------------------------|
| threadId | 输入        | 指定线程的 ID 。                       |
| stream   | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

支持多次调用 aclrtSubscribeReport 接口给多个 Stream （仅支持同一 Device 内的多个 Stream ）注册同一个处理回调函数的线程；为确保 Stream 内的任务按调用顺序执行， 不支持调用 aclrtSubscribeReport 接口给同一个 Stream 注册多个处理回调函数的线程； 同一个进程内，在不同的 Device 上注册回调函数的线程时，不能指定同一个线程 ID 。

单进程内调用本接口注册的线程数量超过一定限制，则接口返回失败。考虑操作系统 的线程切换性能开销，建议调用 aclrtSubscribeReport 接口注册的线程数量控制在 32 个 以下（包括 32 ）。各产品型号支持的线程数量最大值不同，如下表所示。

## 参考资源

| 型号                                                                                                                                  |   线程数量最大值 |
|-------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Atlas 350 加速卡 Atlas A3 训练系列产品 / Atlas A3 推理系列产品 Atlas A2 训练系列产品 / Atlas A2 推理系列产品 Atlas 200I/500 A2 推理产 品 Atlas 推理系列产品 Atlas 训练系列产品 |      1024 |

接口调用流程及示例代码，参见异步模型推理。
