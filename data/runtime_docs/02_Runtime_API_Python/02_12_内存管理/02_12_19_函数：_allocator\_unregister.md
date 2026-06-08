# 函数： allocator\_unregister

> **Section**: 2.12.19


## 产品支持情况

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | x      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

## 资源参考

取消注册用户提供的 Allocator 以及 Allocator 对应的回调函数，用于取消使用用户提供 的 Allocator 。

- C 函数原型

aclError aclrtAllocatorUnregister(aclrtStream stream)

- python 函数

ret = acl.rt.allocator\_unregister(stream)

| 参数名    | 说明                            |
|--------|-------------------------------|
| stream | int ，该 Allocator 对应的 stream 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- Atlas 200I/500 A2 推理产品，不支持该接口。
- 用户销毁 Allocator 前，调用本接口取消注册。
- 待取消注册的 Stream 不存在，或多次调用本接口取消注册，本接口内部不做任何 操作，返回成功。

接口调用示例，参见动态 Shape 输入（设置 Shape 范围）。
