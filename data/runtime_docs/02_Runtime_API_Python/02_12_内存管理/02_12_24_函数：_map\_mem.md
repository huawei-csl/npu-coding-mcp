# 函数： map\_mem

> **Section**: 2.12.24


## 产品支持情况

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |

## 功能说明

## 函数原型

## 参数说明

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 推理系列产品           | √      |
| Atlas 200I/500 A2 推理产品 | √      |

将虚拟内存映射到物理内存。

本接口需与以下其它接口配合使用，以便申请地址连续的虚拟内存、最大化利用物理 内存的目的：

1. 申请虚拟内存（ acl.rt.reserve\_mem\_address 接口）。
2. 申请物理内存（ acl.rt.malloc\_physical 接口）。
3. 将虚拟内存映射到物理内存（ acl.rt.map\_mem 接口）。
4. 执行任务（调用具体的任务接口）。
5. 取消虚拟内存与物理内存的映射（ acl.rt.unmap\_mem 接口）。
6. 释放物理内存（ acl.rt.free\_physical 接口）。
7. 释放虚拟内存（ acl.rt.release\_mem\_address 接口）。

## ● C 函数原型

aclError aclrtMapMem(void *virPtr, size\_t size, size\_t offset, aclrtDrvMemHandle handle, uint64\_t flags)

## ● python 函数

ret = acl.rt.map\_mem(vir\_ptr, size, offset, handle, flags)

| 参数名     | 说明                                                                                                                                                                                                                                                      |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vir_ptr | int ，待映射的虚拟地址。该地址不一定为起始地址，用户也可以根据 起始地址自行偏移后，再映射。                                                                                                                                                                                                        |
| size    | int ，待映射的内存大小，单位 Byte 。 此处的 size 必须与 acl.rt.malloc_physical 接口的 size 参数值相同， size 必须与 acl.rt.mem_get_allocation_granularity 接口获取的 ACL_RT_MEM_ALLOC_GRANULARITY_MINIMUM 对齐。                                                                               |
| offset  | int ，物理内存偏移值，当前只能设置为 0 。                                                                                                                                                                                                                                |
| handle  | int ，物理内存指针地址。 通过 acl.rt.reserve_mem_address 接口预留出来的一整段虚拟地址， 由用户自行管理、划分时，不能同时与两个 Device 上申请的物理地址 绑定。 通过 acl.rt.reserve_mem_address 接口预留出来的一整段虚拟地址， 由用户自行管理、划分时，不能同时与 acl.rt.malloc_physical 、 acl.rt.mem_import_from_shareable_handle 接口输出的 handle 绑 定。 |

## 返回值说明

## 约束说明

| 参数名   | 说明                   |
|-------|----------------------|
| flags | int ，预留，当前仅支持设置为 0 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

Ascend RC 形态不支持调用本接口。
