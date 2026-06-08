# 函数： release\_mem\_address

> **Section**: 2.12.23


## 产品支持情况

## 功能说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

释放通过 acl.rt.reserve\_mem\_address 接口申请的虚拟内存。

本接口需与以下其它接口配合使用，以便申请地址连续的虚拟内存、最大化利用物理 内存的目的：

1. 申请虚拟内存（ acl.rt.reserve\_mem\_address 接口）。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

2. 申请物理内存（ acl.rt.malloc\_physical 接口）。
3. 将虚拟内存映射到物理内存（ acl.rt.map\_mem 接口）。
4. 执行任务（调用具体的任务接口）。
5. 取消虚拟内存与物理内存的映射（ acl.rt.unmap\_mem 接口）。
6. 释放物理内存（ acl.rt.free\_physical 接口）。
7. 释放虚拟内存（ acl.rt.release\_mem\_address 接口）。
- C 函数原型

aclError aclrtReleaseMemAddress(void *virPtr)

- python 函数

ret = acl.rt.release\_mem\_address(vir\_ptr)

| 参数名    | 说明                    |
|--------|-----------------------|
| virPtr | int ，指向待释放的虚拟地址空间的地址。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

Ascend RC 形态不支持调用本接口。

若该虚拟内存与物理内存存在映射关系，则释放虚拟内存前，需调用 acl.rt.unmap\_mem 接口取消该虚拟内存与物理内存的映射。
