# aclrtSnapShotProcessBackup

> **Section**: 1.23.2


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

## 功能说明

## 函数原型

锁定当前进程，以阻止后续的运行时接口调用，包括 Device 设置 / 释放、内存的申请 / 释 放 / 拷贝、 Context/Stream/Event/Notify 等资源的创建与销毁、以及部分任务下发接 口。

在调用此接口之前，必须确保当前进程处于 RUNNING 状态，当前进程默认是 RUNNING 状态；调用该接口后，当前进程将变为 LOCKED 状态。

aclError aclrtSnapShotProcessLock()

无

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

备份快照进程中的 Device 资源，并将 Device 资源保存在 Host 侧，以便后续恢复。针对 当前进程，支持多次备份，以最后一次生效。

在调用此接口之前，必须确保当前进程处于 LOCKED 状态；调用该接口后，当前进程将 变为 BACKED\_UP 状态。

aclError aclrtSnapShotProcessBackup()

## 参数说明

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
