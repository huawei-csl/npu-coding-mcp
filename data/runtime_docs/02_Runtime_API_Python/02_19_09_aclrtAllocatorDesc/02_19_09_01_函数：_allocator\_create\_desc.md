# 函数： allocator\_create\_desc

> **Section**: 2.19.9.1


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

创建 aclrtAllocatorDesc 类型的数据，表示 Allocator 描述信息，主要用于注册回调函 数。

- C 函数原型

aclrtAllocatorDesc aclrtAllocatorCreateDesc()

- python 函数

desc = acl.rt.allocator\_create\_desc()

无

| 返回值   | 说明                                                           |
|-------|--------------------------------------------------------------|
| desc  | int 。 ● 返回 aclrtAllocatorDesc 类型的指针地址，表示成功。 ● 返回 NULL ，表示失败。 |
