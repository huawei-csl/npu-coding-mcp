# aclrtResetDeviceForce

> **Section**: 1.6.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

复位当前运算的 Device ，释放 Device 上的资源。释放的资源包括默认 Context 、默认 Stream 以及默认 Context 下创建的所有 Stream 。若默认 Context 或默认 Stream 下的任务 还未完成，系统会等待任务完成后再释放。

aclrtResetDeviceForce 接口可与 aclrtSetDevice 接口配对使用，也可不与 aclrtSetDevice 接口配对使用，若不配对使用，一个进程中，针对同一个 Device ，调用一次或多次 aclrtSetDevice 接口后，仅需调用一次 aclrtResetDeviceForce 接口可释放 Device 上的资 源。

# 与 aclrtSetDevice 接口配对使用： aclrtSetDevice(1) -&gt; aclrtResetDeviceForce(1) -&gt; aclrtSetDevice(1) -&gt; aclrtResetDeviceForce(1) # 与 aclrtSetDevice 接口不配对使用： aclrtSetDevice(1) -&gt; aclrtSetDevice(1) -&gt; aclrtResetDeviceForce(1)

aclError aclrtResetDeviceForce(int32\_t deviceId)

| 参数名      | 输入 / 输 出   | 说明          |
|----------|------------|-------------|
| deviceId | 输入         | Device ID 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 多线程场景下，针对同一个 Device ，如果每个线程中都调用 aclrtSetDevice 接 口、 aclrtResetDeviceForce 接口，如下所示，线程 2 中的 aclrtResetDeviceForce 接

## 接口调用示例

## 功能说明

## 函数原型

## 口会返回报错，因为线程 1 中 aclrtResetDeviceForce 接口已经释放了 Device 1 的资

源：

时间线

线程 1 ：

aclrtSetDevice(1)           aclrtResetDeviceForce(1)

线程 2 ：

aclrtSetDevice(1)                                   aclrtResetDeviceForce(1)

-----------------------------------------------------------------------------&gt;

多线程场景下，正确方式是应在线程执行的最后，调用一次 aclrtResetDeviceForce 释放 Device 资源，如下所示：

时间线

-----------------------------------------------------------------------------&gt;

线程 1 ：

aclrtSetDevice(1)

线程 2 ：

aclrtSetDevice(1)                                   aclrtResetDeviceForce(1)

- aclrtResetDevice 接口与 aclrtResetDeviceForce 接口可以混用，但混用时，若两 个 Reset 接口的调用次数、调用顺序不对，接口会返回报错。

```
# 混用时的正确方式： # 两个 Reset 接口都分别与 Set 接口配对使用，且 aclrtResetDeviceForce 接口在 aclrtResetDevice 接口之后 aclrtSetDevice(1) -> aclrtResetDevice(1) -> aclrtSetDevice(1) -> aclrtResetDeviceForce(1) aclrtSetDevice(1) -> aclrtSetDevice(1) -> aclrtResetDevice(1) -> aclrtResetDeviceForce(1) # 混用时的错误方式： # aclrtResetDevice 接口内部涉及引用计数的实现，当 aclrtResetDevice 接口每被调用一次，则该引用计数减 1 ，当引用计数减到 0 时，会真正释放 Device 上的资源，此时再调用 aclrtResetDevice 或 aclrtResetDeviceForce 接口都会报错 aclrtSetDevice(1) -> aclrtSetDevice(1) -> aclrtResetDevice(1)-->aclrtResetDevice(1)->aclrtResetDeviceForce(1) aclrtSetDevice(1) -> aclrtSetDevice(1) -> aclrtResetDevice(1)-->aclrtResetDeviceForce(1)->aclrtResetDeviceForce(1) # aclrtResetDeviceForce 接口在 aclrtResetDevice 接口之后，否则接口返回报错 aclrtSetDevice(1) -> aclrtSetDevice(1) -> aclrtResetDeviceForce(1)-->aclrtResetDevice(1)
```

接口调用示例，参见初始化。
