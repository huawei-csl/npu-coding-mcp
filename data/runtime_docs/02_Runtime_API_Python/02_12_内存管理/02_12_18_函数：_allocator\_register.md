# 函数： allocator\_register

> **Section**: 2.12.18


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
| Atlas 200I/500 A2 推理产品            | x      |

调用该接口注册用户提供的 Allocator 以及 Allocator 对应的回调函数，用于使用用户提 供的 Allocator 。

- C 函数原型 aclError aclrtAllocatorRegister(aclrtStream stream, aclrtAllocatorDesc allocatorDesc )
- python 函数

ret = acl.rt.allocator\_register(stream, allocatorDesc)

| 参数名            | 说明                                                             |
|----------------|----------------------------------------------------------------|
| stream         | int ，该 Allocator 需要注册的 Stream 。传入的 stream 参数值不能为 NULL ，否则返回报错。 |
| allocatorD esc | int ， Allocator 描述符指针地址。                                       |

## 返回值说明

## 约束说明

## 资源参考

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- Atlas 200I/500 A2 推理产品，不支持该接口。
- 当前仅支持在单算子模型执行、动态 shape 模型推理场景下使用本接口。 acl.op.execute\_v2

单算子模型场景下，需在算子执行接口（例如： 等）之前调用 本接口。

动态 shape 模型推理场景，本接口需配合 aclmdlExecuteAsync 接口一起使用，且 需在 aclmdlExecuteAsync 接口之前调用本接口。

- 调用本接口前，需要先调用 acl.rt.allocator\_create\_desc 创建 Allocator 描述符， 再分别调用 acl.rt.allocator\_set\_obj\_to\_desc 、

acl.rt.allocator\_set\_get\_addr\_from\_block\_func\_to\_desc 、

acl.rt.allocator\_set\_alloc\_func\_to\_desc 、

acl.rt.allocator\_set\_free\_func\_to\_desc 设置 Allocator 对象及回调函数。

Allocator 描述符使用完成后，可调用 acl.rt.allocator\_destroy\_desc 接口销毁 Allocator 描述符。

- 对于同一条流，多次调用本接口，以最后一次注册为准。
- 对于不同流，如果用户使用同一个 Allocator ，不可以多条流并发执行，在执行下 一条 Stream 前，需要对上一 Stream 做流同步。
- 将 Allocator 中的内存释放给操作系统前，需要先调用 acl.rt.synchronize\_stream 接口执行流同步，确保 Stream 中的任务已执行完成。

接口调用示例，参见动态 Shape 输入（设置 Shape 范围）。
