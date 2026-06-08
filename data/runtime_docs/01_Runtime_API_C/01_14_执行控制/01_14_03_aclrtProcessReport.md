# aclrtProcessReport

> **Section**: 1.14.3


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

调用本接口设置超时时间，等待 aclrtLaunchCallback 接口下发的回调任务执行。

本接口需与以下其它接口配合使用，以便实现异步场景下的 callback 功能：

1. 定义并实现回调函数，函数原型为： typedef void (*aclrtCallback)(void *userData) ；
2. 新建线程，在线程函数内，调用 aclrtProcessReport 接口设置超时时间（需循环 调用），等待回调任务执行；
3. 调用 aclrtSubscribeReport 接口建立第 2 步中的线程和 Stream 的绑定关系，该 Stream 下发的回调函数将在绑定的线程中执行；
4. 在指定 Stream 上执行异步任务（例如异步推理任务）；

## 函数原型

## 参数说明

## 返回值说明

## 参考资源

接口调用流程及示例代码，参见异步模型推理。
