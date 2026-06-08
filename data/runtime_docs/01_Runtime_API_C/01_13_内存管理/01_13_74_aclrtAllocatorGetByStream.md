# aclrtAllocatorGetByStream

> **Section**: 1.13.74


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

根据 Stream 查询用户注册的 Allocator 信息。

aclError aclrtAllocatorGetByStream(aclrtStream stream, aclrtAllocatorDesc *allocatorDesc, aclrtAllocator *allocator, aclrtAllocatorAllocFunc *allocFunc, aclrtAllocatorFreeFunc *freeFunc, aclrtAllocatorAllocAdviseFunc *allocAdviseFunc, aclrtAllocatorGetAddrFromBlockFunc *getAddrFromBlockFunc)

| 参数名                   | 输入 / 输 出   | 说明                                                                                                                                                 |
|-----------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| stream                | 输入         | 注册的类型，按照不同的子模块区分。类型定义请参 见 aclrtStream 。                                                                                                            |
| allocatorDesc         | 输出         | Allocator 描述符指针。类型定义请参见 aclrtAllocatorDesc 。                                                                                                       |
| allocator             | 输出         | 用户提供的 Allocator 对象指针。类型定义请参见 aclrtAllocator 。                                                                                                      |
| allocFunc             | 输出         | 申请内存 block 的回调函数。 回调函数定义如下： typedef void *(*aclrtAllocatorAllocFunc)( aclrtAllocator allocator, size_t size);                                      |
| freeFunc              | 输出         | 释放内存 block 的回调函数。 回调函数定义如下： typedef void (*aclrtAllocatorFreeFunc)( aclrtAllocator allocator, aclrtAllocatorBlock block);                          |
| allocAdviseFunc       | 输出         | 根据建议地址申请内存 block 的回调函数。 回调函数定义如下： typedef void *(*aclrtAllocatorAllocAdviseFunc)( aclrtAllocator allocator, size_t size, aclrtAllocatorAddr addr); |
| getAddrFromBloc kFunc | 输出         | 根据申请来的 block 获取 device 内存地址的回调函 数。 回调函数定义如下： typedef void *(*aclrtAllocatorGetAddrFromBlockFunc) ( aclrtAllocatorBlock block);                     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
