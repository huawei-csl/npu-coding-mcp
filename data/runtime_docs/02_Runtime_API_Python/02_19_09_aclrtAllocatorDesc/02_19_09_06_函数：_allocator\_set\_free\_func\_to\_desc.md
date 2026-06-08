# 函数： allocator\_set\_free\_func\_to\_desc

> **Section**: 2.19.9.6


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

使用用户提供的 Allocator 场景下，设置 " 释放内存 block" 的回调函数。

## ● C 函数原型

aclError aclrtAllocatorSetFreeFuncToDesc(aclrtAllocatorDesc allocatorDesc, aclrtAllocatorFreeFunc func)

- python 函数

ret = acl.rt.allocator\_set\_free\_func\_to\_desc(allocatorDesc, func)

| 参数名           | 说明                                                                              |
|---------------|---------------------------------------------------------------------------------|
| allocatorDesc | int ， Allocator 描述符指针地址。需提前调用 acl.rt.allocator_create_desc 接口设置 Allocator 描述信息。 |
| func          | ● 释放内存 block 的回调函数。 回调函数定义如下： def allocator_free_func(allocator, block): pass   |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
