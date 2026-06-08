# aclrtIpcMemClose

> **Section**: 1.13.69


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 训练系列产品 | √      |

关闭 IPC 共享内存，调用 aclrtIpcMemImportByKey 接口的进程中、调用 aclrtIpcMemGetExportKey 接口的进程中都需要调用此接口。

对于同一个共享内存 key ，需所有调用 aclrtIpcMemImportByKey 接口的进程中都调用 aclrtIpcMemClose 接口后，调用 aclrtIpcMemGetExportKey 接口的进程中才可以调用 aclrtIpcMemClose 接口，否则可能导致异常。

本接口需与其它接口配合使用，以便实现内存共享的目的，配合使用流程请参见 aclrtIpcMemGetExportKey 接口处的说明。

aclError aclrtIpcMemClose(const char *key)

| 参数名   | 输入 / 输 出   | 说明                                         |
|-------|------------|--------------------------------------------|
| key   | 输入         | 通过 aclrtIpcMemGetExportKey 接口获取的共享内存 key 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见进程间通信。
