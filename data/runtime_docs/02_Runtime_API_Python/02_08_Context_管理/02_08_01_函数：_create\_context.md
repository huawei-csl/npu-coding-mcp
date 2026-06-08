# 函数： create\_context

> **Section**: 2.8.1


## 产品支持情况

## 功能说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

在当前进程或线程中显式创建一个 Context 。

对于 Atlas 200I/500 A2 推理产品，该 Context 中包含 2 个 Stream ， 1 个默认 Stream 和 1 个执行内部同步的 Stream 。

对于 Atlas 训练系列产品，该 Context 中包含 1 个默认 Stream 。

对于 Atlas A2 训练系列产品 /Atlas A2 推理系列产品，该 Context 中包含 1 个默认 Stream 。

对于 Atlas 推理系列产品，在 Ascend EP 下，该 Context 中包含 2 个 Stream ， 1 个默认 Stream 和 1 个执行内部同步的 Stream 。

对于 Atlas A3 训练系列产品 /Atlas A3 推理系列产品，该 Context 中包含 1 个默认 Stream 。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

## 资源参考

## 说明

如果在应用程序中没有调用 acl.rt.set\_device 接口，那么在首次调用 acl.rt.create\_context 接口 时，系统内部会根据该接口传入的 Device ID ，为该 Device 绑定一个默认 Stream （一个 Device 仅 绑定一个默认 Stream ），因此在首次调用 acl.rt.create\_context 接口时，占用的 Stream 数量 = Device 上绑定的默认 Stream + Context 中包含的 Stream 。

- C 函数原型

aclError aclrtCreateContext(aclrtContext *context, int32\_t deviceId)

- python 函数

context, ret = acl.rt.create\_context(device\_id)

| 参数名       | 说明                                |
|-----------|-----------------------------------|
| device_id | int ，指定需要创建 Context 的 Device 设备号。 |

| 返回值     | 说明                            |
|---------|-------------------------------|
| context | int ，表示创建的 Context 的指针地址。     |
| ret     | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

## 支持以下使用场景：

- 若不调用 acl.rt.create\_context 接口显式创建 Context ，那系统会使用默认 Context ，该默认 Context 是在调用 acl.rt.set\_device 接口时隐式创建的。
- -隐式创建 Context ：适合简单、无复杂交互逻辑的应用，但缺点在于，在多线 程编程中，执行结果取决于线程调度的顺序。
- -显式创建 Context ：适合大型、复杂交互逻辑的应用，便于提高程序的可读 性、可维护性。
- 在某一进程中指定 Device ，该进程内的多个线程可共用在此 Device 上显式创建的 Context （调用 acl.rt.create\_context 接口显式创建 Context ）。
- 若在某一进程内创建多个 Context （ Context 的数量与 Stream 相关， Stream 数量有 限制，请参见 acl.rt.create\_stream ），当前线程在同一时刻内只能使用其中一个 Context ，建议通过 acl.rt.set\_context 接口明确指定当前线程的 Context ，增加程 序的可维护性。

接口调用流程与示例，请参见运行时资源申请与释放。
