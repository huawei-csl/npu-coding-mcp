# aclrtMemP2PMap

> **Section**: 1.13.49


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

本接口用于建立同一进程内两个 Device 之间的内存页表映射，以实现跨 Device 的内存 访问，但在进行此操作前，需先调用 aclrtDeviceEnablePeerAccess 接口以开启两个 Device 间的数据交互。

调用本接口建立页表映射后，跨 Device 访问时不会出现内存缺页的问题，首次访问内 存时性能更优。

aclError aclrtMemP2PMap(void *devPtr, size\_t size, int32\_t dstDevId, uint64\_t flags)

| 参数名      | 输入 / 输 出   | 说明                                                              |
|----------|------------|-----------------------------------------------------------------|
| devPtr   | 输入         | Device 内存地址（例如调用 aclrtMalloc 接口申请的 Device 内 存），此处指共享内存提供方的内存地址。 |
| size     | 输入         | 内存大小，单位 Byte 。                                                  |
| dstDevId | 输入         | Device ID ，此处指共享内存使用方的 ID 。                                     |
| flags    | 输入         | 预留参数，当前固定设置为 0 。                                                |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
