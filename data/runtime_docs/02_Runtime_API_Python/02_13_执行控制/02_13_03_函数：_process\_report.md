# 函数： process\_report

> **Section**: 2.13.3


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

异步任务场景下，调用本接口设置超时时间，等待 acl.rt.launch\_callback 接口下发的 回调任务执行。

本接口需与以下其它接口配合使用，以便实现异步场景下的 Callback 功能：

1. 新建线程，在线程函数内，调用 acl.rt.process\_report 接口设置超时时间（需循环 调用），等待 acl.rt.launch\_callback 接口下发的函数回调任务。
2. 调用 acl.rt.subscribe\_report 接口建立第 1 步中的线程和 Stream 的绑定关系，该 Stream 下发的函数回调任务将在绑定的线程中执行。
3. 在指定 Stream 上执行异步任务（例如异步推理任务）。
4. 定义并实现回调函数，调用 acl.rt.launch\_callback 接口在 Stream 的任务队列中下 发函数回调任务，触发 acl.rt.subscribe\_report 订阅的线程处理回调函数，每调用 一次 acl.rt.launch\_callback 接口，就会下发一个回调函数任务。
5. 异步任务全部执行完成后，调用 acl.rt.unsubscribe\_report 接口取消线程订阅， 解除线程和 Stream 的绑定关系。
- C 函数原型

aclError aclrtProcessReport(int32\_t timeout)

- python 函数

ret = acl.rt.process\_report(timeout)

## 参数说明

## 返回值说明

## 资源参考

| 参数名     | 说明                                                                           |
|---------|------------------------------------------------------------------------------|
| timeout | timeout ： int ，指定超时时间，单位为 ms 。 取值范围为： ● -1 ：表示无限等待。 ● 大于 0 （不包含 0 ）：表示等待的时间。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 接口调用流程，参见接口调用流程。
- 接口调用示例，参见示例代码。
