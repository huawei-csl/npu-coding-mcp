# aclrtCreateContext

> **Section**: 1.7.1


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

在当前线程中显式创建 Context ，并将当前线程与新创建的 Context 相关联。

若不调用 aclrtCreateContext 接口显式创建 Context ，那系统会使用默认 Context ，该默 认 Context 是在调用 aclrtSetDevice 接口时隐式创建的。默认 Context 适合简单、无复 杂交互逻辑的应用，但缺点在于，在多线程编程中，执行结果取决于线程调度的顺 序。显式创建的 Context 适合大型、复杂交互逻辑的应用，且便于提高程序的可读性、 可维护性。

aclError aclrtCreateContext(aclrtContext *context, int32\_t deviceId)

| 参数名     | 输入 / 输 出   | 说明                                 |
|---------|------------|------------------------------------|
| context | 输出         | Context 的指针。类型定义请参见 aclrtContext 。 |

## 返回值说明

## 约束说明

| 参数名      | 输入 / 输 出   | 说明                                                                                                                  |
|----------|------------|---------------------------------------------------------------------------------------------------------------------|
| deviceId | 输入         | 在指定的 Device 下创建 Context 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 在某一进程中指定 Device ，该进程内的多个线程可共用在此 Device 上显式创建的 Context 。
- 若在某一进程内创建多个 Context ， Context 的数量与 Stream 相关， Stream 数量有 限制，请参见显式创建 Stream 的接口。当前线程在同一时刻内只能使用其中一个 Context ，建议通过 aclrtSetCurrentContext 接口明确指定当前线程的 Context ， 增加程序的可维护性。
- 调用本接口创建的 Context 中包含一个默认 Stream 。

但

认

Stream

推理系列产品的

EP

标准形态除外，其

和一个执行内部同步的

Stream

。

- 如果在应用程序中没有调用 aclrtSetDevice 接口，那么在首次调用 aclrtCreateContext 接口时，系统内部会根据该接口传入的 Device ID ，为该 Device 绑定一个默认 Stream （一个 Device 仅绑定一个默认 Stream ），因此在首次调用 aclrtCreateContext 接口时，占用的 Stream 数量 = Device 上绑定的默认 Stream + Context 中包含的 Stream 。
