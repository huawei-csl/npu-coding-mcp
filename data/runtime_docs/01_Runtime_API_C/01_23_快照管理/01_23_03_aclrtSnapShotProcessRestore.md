# aclrtSnapShotProcessRestore

> **Section**: 1.23.3


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

无

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

恢复快照进程中的 Device 资源。根据备份好的 Device 资源进行恢复，从最后一次备份 点进行恢复。

在调用该接口之前，必须确保当前进程处于 BACKED\_UP 状态；调用该接口后，当前进 程将变为 LOCKED 状态。

aclError aclrtSnapShotProcessRestore()

无

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

恢复和备份需要在同一个 Device 上（指 Device ID 相同）。恢复时，若 Device 被其他进 程占用，则恢复失败。
