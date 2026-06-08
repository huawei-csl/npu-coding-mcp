# 函数： subscribe\_report

> **Section**: 2.13.1


## 产品支持情况

存 key ，需所有调用 acl.rt.ipc\_mem\_import\_by\_key 接口的进程中都调用 acl.rt.ipc\_mem\_close 接口后，调用 acl.rt.ipc\_mem\_get\_export\_key 接口的进程中才 可以调用 acl.rt.ipc\_mem\_close 接口，否则可能导致异常。 本接口需与其它接口配合 使用，以便实现内存共享的目的，配合使用流程请参 acl.rt.ipc\_mem\_get\_export\_key 接口处的说明。

- C 函数原型 aclError aclrtIpcMemClose(const char *key)
- python 函数

ret = acl.rt.ipc\_mem\_close(key)

| 参数名   | 说明                                                             |
|-------|----------------------------------------------------------------|
| key   | str ，共享内存 key ，通过 acl.rt.ipc_mem_get_export_key 接口获取 的内存 key 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

异步任务场景下，指定处理 Stream 上回调函数的线程。

本接口需与以下其它接口配合使用，以便实现异步场景下的 Callback 功能：

1. 新建线程，在线程函数内，调用 acl.rt.process\_report 接口设置超时时间（需循环 调用），等待 acl.rt.launch\_callback 接口下发的函数回调任务。
2. 调用 acl.rt.subscribe\_report 接口建立第 1 步中的线程和 Stream 的绑定关系，该 Stream 下发的函数回调任务将在绑定的线程中执行。
3. 在指定 Stream 上执行异步任务（例如异步推理任务）。
4. 定义并实现回调函数，调用 acl.rt.launch\_callback 接口在 Stream 的任务队列中下 发函数回调任务，触发 acl.rt.subscribe\_report 订阅的线程处理回调函数，每调用 一次 acl.rt.launch\_callback 接口，就会下发一个回调函数任务。
5. 异步任务全部执行完成后，调用 acl.rt.unsubscribe\_report 接口取消线程订阅， 解除线程和 Stream 的绑定关系。
- C 函数原型 aclError aclrtSubscribeReport(uint64\_t threadId, aclrtStream stream)

## ● python 函数

ret = acl.rt.subscribe\_report(thread\_id, stream)

| 参数名       | 说明                         |
|-----------|----------------------------|
| thread_id | int ，指定线程 id 。             |
| stream    | int ，指定需要处理的 Stream 的指针地址。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 支持多次调用 acl.rt.subscribe\_report 接口给多个 Stream （仅支持同一 Device 内的 多个 Stream ）订阅同一个处理回调函数的线程。
- 为确保 Stream 内的任务按调用顺序执行，不支持调用 acl.rt.subscribe\_report 接口 给同一个 Stream 订阅多个处理回调函数的线程。
- 在 Atlas 训练系列产品上，单进程内调用 acl.rt.subscribe\_report 接口订阅的线程数 量如果超过 1024 个，则接口返回失败。
- 在 Atlas A2 训练系列产品 /Atlas A2 推理系列产品上，单进程内调用 acl.rt.subscribe\_report 接口订阅的线程数量如果超过 1024 个，则接口返回失败。

## 资源参考

- 在 Atlas A3 训练系列产品 /Atlas A3 推理系列产品上，单进程内调用 aclrtSubscribeReport 接口订阅的线程数量如果超过 1024 个，则接口返回失败。
- 在 Atlas 推理系列产品上，单进程内调用 acl.rt.subscribe\_report 接口订阅的线程数 量如果超过 1024 个，则接口返回失败。
- 在 Atlas 200I/500 A2 推理产品上，单进程内调用 acl.rt.subscribe\_report 接口订阅 的线程数量如果超过 1024 个，则接口返回失败。
- 考虑操作系统的线程切换性能开销，建议调用 acl.rt.subscribe\_report 接口订阅的 线程数量控制在 32 个以下（包括 32 ）。
- 同一个进程内，在不同的 Device 上订阅回调函数的线程时，不能指定同一个线程 ID 。
- 接口调用流程，参见接口调用流程。
- 接口调用示例，参见示例代码。
