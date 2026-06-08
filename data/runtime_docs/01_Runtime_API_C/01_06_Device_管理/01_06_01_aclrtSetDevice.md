# aclrtSetDevice

> **Section**: 1.6.1


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

指定当前线程中用于运算的 Device 。在不同线程中支持调用 aclrtSetDevice 接口指定同 一个 Device 用于运算。

调用本接口会隐式创建默认 Context ，该默认 Context 中包含一个默认 Stream 。在同一 个进程的多个线程中，如果调用 aclrtSetDevice 接口并指定相同的 Device 用于计算，那 么这些线程将共享同一个默认 Context 。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

## 接口调用示例

但 Atlas 推理系列产品的 EP 标准形态除外，其隐式创建的默认 Context 中包含两个 Stream ：一个默认 Stream 和一个执行内部同步的 Stream 。

aclError aclrtSetDevice(int32\_t deviceId)

| 参数名      | 输入 / 输 出   | 说明                                                                                                    |
|----------|------------|-------------------------------------------------------------------------------------------------------|
| deviceId | 输入         | Device ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 调用 aclrtSetDevice 接口指定运算的 Device 后，若不使用 Device 上的资源时，可调 用 aclrtResetDevice 或 aclrtResetDeviceForce 接口及时释放本进程使用的 Device 资源（若不调用 Reset 接口，进程退出时也会释放本进程使用的 Device 资源）：
- -若调用 aclrtResetDevice 接口释放 Device 资源： aclrtResetDevice 接口内部涉及引用计数的实现，建议 aclrtResetDevice 接口 与 aclrtSetDevice 接口配对使用， aclrtSetDevice 接口每被调用一次，则引用 计数加一， aclrtResetDevice
- 接口每被调用一次，则该引用计数减一，当引用 计数减到 0 时，才会真正释放 Device 上的资源。
- -若调用 aclrtResetDeviceForce 接口释放 Device 资源： aclrtResetDeviceForce 接口可与 aclrtSetDevice 接口配对使用，也可不与 aclrtSetDevice 接口配对使用，若不配对使用，一个进程中，针对同一个 Device ，调用一次或多次 aclrtSetDevice 接口后，仅需调用一次 aclrtResetDeviceForce 接口可释放 Device 上的资源。
- 多 Device 场景下，可在进程中通过 aclrtSetDevice 接口切换到其它 Device 。

接口调用示例，参见初始化。
