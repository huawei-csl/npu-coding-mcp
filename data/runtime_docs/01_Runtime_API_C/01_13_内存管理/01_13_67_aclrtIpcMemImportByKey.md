# aclrtIpcMemImportByKey

> **Section**: 1.13.67


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

在本进程中导入 key 的信息，并返回本进程可以使用的 Device 内存地址指针。

本接口需与其它接口配合使用，以便实现内存共享的目的，配合使用流程请参见 aclrtIpcMemGetExportKey 接口处的说明。

aclError aclrtIpcMemImportByKey(void **devPtr, const char *key, uint64\_t flags)

| 参数名    | 输入 / 输 出   | 说明                                                            |
|--------|------------|---------------------------------------------------------------|
| devPtr | 输出         | Device 内存地址指针。                                                |
| key    | 输入         | 共享内存 key 必须先调用 aclrtIpcMemGetExportKey 接口获取共享内存 key ，再作为入参传入。 |

## 返回值说明

## 接口调用示例

| 参数名   | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| flags | 输入         | 是否开启两个 Device 之间的数据交互。 取值为如下宏： ● ACL_RT_IPC_MEM_IMPORT_FLAG_DEFAULT ：默认值， 关闭两个 Device 之间的数据交互。 配置为该值时，需单独调用 aclrtDeviceEnablePeerAccess 接口开启两个 Device 之间 的数据交互。 ● ACL_RT_IPC_MEM_IMPORT_FLAG_ENABLE_PEER_ACC ESS ：开启两个 Device 之间的数据交互。 配置为该值时，则无需调用 aclrtDeviceEnablePeerAccess 接口。 宏的定义如下： #define ACL_RT_IPC_MEM_IMPORT_FLAG_DEFAULT 0x0UL #define ACL_RT_IPC_MEM_IMPORT_FLAG_ENABLE_PEER_ACCESS 0x1UL |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见进程间通信。
