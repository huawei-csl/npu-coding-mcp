# aclrtAllocatorSetObjToDesc

> **Section**: 1.28.27.3


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

使用用户提供的 Allocator 场景下，向 Allocator 描述信息中设置 Allocator 对象。

## 函数原型

## 参数说明

## 返回值说明

aclError aclrtAllocatorSetObjToDesc(aclrtAllocatorDesc allocatorDesc,  aclrtAllocator allocator)

| 参数名            | 输入 / 输 出   | 说明                                                                   |
|----------------|------------|----------------------------------------------------------------------|
| allocatorDes c | 输入         | Allocator 描述符指针。 需提前调用 aclrtAllocatorCreateDesc 接口设置 Allocator 描述信息。 |
| allocator      | 输入         | 用户提供的 Allocator 对象指针。类型定义请参见 aclrtAllocator 。                        |

返回 0 表示成功，返回其他值表示失败。
