# aclrtSnapShotProcessUnlock

> **Section**: 1.23.4


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

## 功能说明

解锁 Device 上的当前进程，同时解除运行时接口的阻塞调用。

在调用此接口之前，必须确保当前进程处于 LOCKED 或 BACKED\_UP 状态；调用此接口 后，当前进程将变为 RUNNING 状态。

函数原型

aclError aclrtSnapShotProcessUnlock()

参数说明

无

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
