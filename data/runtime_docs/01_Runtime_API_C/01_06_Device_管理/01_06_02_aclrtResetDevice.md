# aclrtResetDevice

> **Section**: 1.6.2


## 产品支持情况

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

复位当前运算的 Device ，释放 Device 上的资源。释放的资源包括默认 Context 、默认 Stream 以及默认 Context 下创建的所有 Stream 。若默认 Context 或默认 Stream 下的任务 还未完成，系统会等待任务完成后再释放。

aclrtResetDevice 接口内部涉及引用计数的实现，建议 aclrtResetDevice 接口与 aclrtSetDevice 接口配对使用， aclrtSetDevice 接口每被调用一次，则引用计数加一， aclrtResetDevice 接口每被调用一次，则该引用计数减一，当引用计数减到 0 时，才会 真正释放 Device 上的资源。

如果多次调用 aclrtSetDevice 接口而不调用 aclrtResetDevice 接口释放本线程使用的 Device 资源，进程退出时也会释放本进程使用的 Device 资源。

aclError aclrtResetDevice(int32\_t deviceId)

| 参数名      | 输入 / 输 出   | 说明          |
|----------|------------|-------------|
| deviceId | 输入         | Device ID 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

若要复位的 Device 上存在显式创建的 Context 、 Stream 、 Event ，在复位前，建议遵循 如下接口调用顺序，否则可能会导致业务异常。

接口调用顺序：调用 aclrtDestroyEvent 接口释放 Event/ 调用 aclrtDestroyStream 接口 释放显式创建的 Stream--&gt; 调用 aclrtDestroyContext 释放显式创建的 Context--&gt; 调用 aclrtResetDevice 接口
