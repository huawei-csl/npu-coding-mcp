# aclrtUnmapMem

> **Section**: 1.13.34


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

取消虚拟内存与物理内存之间的映射关系。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

## 接口调用示例

## 本接口需与以下其它接口配合使用，以便申请地址连续的虚拟内存、最大化利用物理 内存：

1. 申请虚拟内存（ aclrtReserveMemAddress 接口）；
2. 申请物理内存（ aclrtMallocPhysical 接口）；
3. 将虚拟内存映射到物理内存（ aclrtMapMem 接口）；
4. 执行任务（调用具体的任务接口）；
5. 取消虚拟内存与物理内存的映射（ aclrtUnmapMem 接口）；
6. 释放物理内存（ aclrtFreePhysical 接口）；
7. 释放虚拟内存（ aclrtReleaseMemAddress 接口）。

aclError aclrtUnmapMem(void *virPtr)

| 参数名    | 输入 / 输出   | 说明              |
|--------|-----------|-----------------|
| virPtr | 输入        | 待取消映射的虚拟内存地址指针。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

对于 Atlas 200I/500 A2 推理产品， Ascend RC 形态下，不支持调用本接口。

接口调用示例，参见虚拟内存管理。
