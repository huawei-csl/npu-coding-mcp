# 函数： mem\_import\_from\_shareable\_handle

> **Section**: 2.12.29


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

在本进程中获取 shareable\_handle 里的信息，并返回本进程中的 handle ，用于在本进 程中建立虚拟地址与物理地址之间的映射关系。本接口还支持生成指定 Device 上的 handle 。

本接口需与其它接口配合使用，以便实现内存共享的目的，配合使用流程请参见 acl.rt.mem\_export\_to\_shareable\_handle 接口处的说明。

- C 函数原型

aclError aclrtMemImportFromShareableHandle(uint64\_t shareableHandle, int32\_t deviceId, aclrtDrvMemHandle *handle)

- python 函数

handle, ret = acl.rt.mem\_import\_from\_shareable\_handle(shareable\_handle, device\_id)

## 参数说明

## 返回值说明

## 约束说明

| 参数名               | 说明                                                                                                                               |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| shareable_ha ndle | int ，待共享的 shareable_handle 。 与 acl.rt.mem_export_to_shareable_handle 接口中导出的 shareable_handle 保持一致。                               |
| deviceId          | int ，用于生成指定 Device ID 上的 handle 。 用户调用 acl.rt.get_device_count 接口获取可用的 Device 数量后， 这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 - 1)] |

| 返回值    | 说明                            |
|--------|-------------------------------|
| handle | int ，本进程的物理内存 handle 。        |
| ret    | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- Atlas 200I/500 A2 推理产品上， Ascend RC 形态不支持调用本接口。
- 在调用本接口前，需确保待共享的物理内存存在，不能提前释放。
- handle 与 shareableHandle 是一一对应的关系，在同一个进程中，不允许一对多、 或多对一。
- 不支持同一个进程中调用 acl.rt.mem\_import\_from\_shareable\_handle 、 acl.rt.mem\_export\_to\_shareable\_handle 这两个接口，只支持跨进程调用。
- 支持在一个 Device 上调用 acl.rt.mem\_export\_to\_shareable\_handle 接口导出 handle ，然后调用本接口生成另一个 Device 上的 handle 。
- 内存使用完成后，要及时调用 acl.rt.free\_physical 销毁 handle ，并且需所有调用 本接口的进程都销毁 shareable\_handle 的情况下， handle 才会真正销毁。
- 支持跨 Device 共享物理内存。

跨 Device 共享物理内存仅支持如下型号，且需配合 acl.rt.device\_enable\_peer\_access 接口使用：

Atlas A3 训练系列产品 /Atlas A3 推理系列产品

Atlas A2 训练系列产品 /Atlas A2 推理系列产品

Atlas 训练系列产品

Atlas 推理系列产品
