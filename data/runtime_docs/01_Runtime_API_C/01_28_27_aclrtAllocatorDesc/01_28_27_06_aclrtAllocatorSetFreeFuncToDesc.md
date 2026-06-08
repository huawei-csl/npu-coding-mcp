# aclrtAllocatorSetFreeFuncToDesc

> **Section**: 1.28.27.6


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

使用用户提供的 Allocator 场景下，设置'释放内存 block '的回调函数。

aclError aclrtAllocatorSetFreeFuncToDesc(aclrtAllocatorDesc allocatorDesc, aclrtAllocatorFreeFunc func)

## 参数说明

## 返回值说明

| 参数名            | 输入 / 输 出   | 说明                                                                                                                        |
|----------------|------------|---------------------------------------------------------------------------------------------------------------------------|
| allocatorDes c | 输入         | Allocator 描述符指针。 需提前调用 aclrtAllocatorCreateDesc 接口设置 Allocator 描述信息。                                                      |
| func           | 输入         | 释放内存 block 的回调函数。 回调函数定义如下： typedef void (*aclrtAllocatorFreeFunc)( aclrtAllocator allocator, aclrtAllocatorBlock block); |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
