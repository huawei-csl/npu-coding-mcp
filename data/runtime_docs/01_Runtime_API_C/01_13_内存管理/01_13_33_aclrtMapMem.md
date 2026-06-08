# aclrtMapMem

> **Section**: 1.13.33


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

将虚拟内存映射到物理内存。

本接口需与以下其它接口配合使用，以便申请地址连续的虚拟内存、最大化利用物理 内存：

1. 申请虚拟内存（ aclrtReserveMemAddress 接口）；
2. 申请物理内存（ aclrtMallocPhysical 接口）；
3. 将虚拟内存映射到物理内存（ aclrtMapMem 接口）；
4. 执行任务（调用具体的任务接口）；
5. 取消虚拟内存与物理内存的映射（ aclrtUnmapMem 接口）；
6. 释放物理内存（ aclrtFreePhysical 接口）；
7. 释放虚拟内存（ aclrtReleaseMemAddress 接口）。

aclError aclrtMapMem(void *virPtr, size\_t size, size\_t offset, aclrtDrvMemHandle handle, uint64\_t flags)

| 参数名    | 输入 / 输 出   | 说明                                                                                                                                                              |
|--------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| virPtr | 输入         | 待映射的虚拟内存地址指针。 这个地址不一定是起始地址，用户也可以根据起始地址自行 偏移后，再映射。                                                                                                               |
| size   | 输入         | 待映射的内存大小，单位 Byte 。 此处的 size 必须与 aclrtMallocPhysical 接口的 size 参数值相 同， size 必须与 aclrtMemGetAllocationGranularity 接口 获取的 ACL_RT_MEM_ALLOC_GRANULARITY_MINIMUM 对 齐。 |

## 返回值说明

## 约束说明

## 接口调用示例

| 参数名    | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                |
|--------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| offset | 输入         | 物理内存偏移值，当前只能设置为 0 。                                                                                                                                                                                                                                               |
| handle | 输入         | 物理内存信息 handle 。类型定义请参见 aclrtDrvMemHandle 。 通过 aclrtReserveMemAddress 接口预留出来的一整段虚拟 地址，由用户自行管理、划分时，不能同时与两个 Device 上 申请的物理地址绑定。 通过 aclrtReserveMemAddress 接口预留出来的一整段虚拟 地址，由用户自行管理、划分时，不能同时与 aclrtMallocPhysical 、 aclrtMemImportFromShareableHandle 接口输出的 handle 绑定。 |
| flags  | 输入         | 预留，当前只能设置为 0 。                                                                                                                                                                                                                                                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

对于 Atlas 200I/500 A2 推理产品， Ascend RC 形态下，不支持调用本接口。

接口调用示例，参见虚拟内存管理。
