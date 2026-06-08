# 函数： allocator\_set\_obj\_to\_desc

> **Section**: 2.19.9.3


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

使用用户提供的 Allocator 场景下，向 Allocator 描述信息中设置 Allocator 对象。

- C 函数原型 aclError aclrtAllocatorSetObjToDesc(aclrtAllocatorDesc allocatorDesc,  aclrtAllocator allocator)
- python 函数

ret = acl.rt.allocator\_set\_obj\_to\_desc(allocatorDesc, allocator)

| 参数名           | 说明                                                                              |
|---------------|---------------------------------------------------------------------------------|
| allocatorDesc | int ， Allocator 描述符指针地址。需提前调用 acl.rt.allocator_create_desc 接口设置 Allocator 描述信息。 |
| allocator     | int ，用户提供的 Allocator 对象指针地址。                                                    |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
