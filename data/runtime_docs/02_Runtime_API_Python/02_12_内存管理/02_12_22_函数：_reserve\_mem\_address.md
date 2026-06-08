# 函数： reserve\_mem\_address

> **Section**: 2.12.22


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

## 预留虚拟内存。

本接口需与以下其它接口配合使用，以便申请地址连续的虚拟内存、最大化利用物理 内存的目的：

1. 申请虚拟内存（ acl.rt.reserve\_mem\_address 接口）。
2. 申请物理内存（ acl.rt.malloc\_physical 接口）。
3. 将虚拟内存映射到物理内存（ acl.rt.map\_mem 接口）。
4. 执行任务（调用具体的任务接口）。
5. 取消虚拟内存与物理内存的映射（ acl.rt.unmap\_mem 接口）。
6. 释放物理内存（ acl.rt.free\_physical 接口）。
7. 释放虚拟内存（ acl.rt.release\_mem\_address 接口）。

## ● C 函数原型

aclError aclrtReserveMemAddress(void **virPtr, size\_t size, size\_t alignment, void *expectPtr, uint64\_t flags)

## ● python 函数

vir\_ptr, ret = acl.rt.reserve\_mem\_address(size, alignment, expect\_ptr, flags)

| 参数名       | 说明                                   |
|-----------|--------------------------------------|
| size      | int ，虚拟地址空间大小，单位 Byte 。 size 不能为 0 。 |
| alignment | int ，虚拟地址对齐值，预留，当前只能设置为 0 。          |
| expectPtr | int ，指定期望返回的虚拟地址空间起始地址，预留，当前只能传 0 。  |

## 返回值说明

## 约束说明

| 参数名   | 说明                               |
|-------|----------------------------------|
| flags | int ，大页 / 普通页标志，预留参数，建议固定配置为 0 。 |

| 返回值    | 说明                            |
|--------|-------------------------------|
| virPtr | int ，指向已分配的虚拟地址空间的地址。         |
| ret    | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- Ascend RC 形态不支持调用本接口。 当前以下型号支持 Ascend RC 形态：
- -Atlas 200I/500 A2 推理产品
- 使用本接口预留的虚拟内存，单进程场景下只支持调用 memcpy\_async 接口实现 两个 Device 之间的数据拷贝。
