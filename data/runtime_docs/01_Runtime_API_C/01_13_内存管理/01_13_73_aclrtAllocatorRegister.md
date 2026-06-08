# aclrtAllocatorRegister

> **Section**: 1.13.73


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

调用该接口注册用户提供的 Allocator 以及 Allocator 对应的回调函数，以便后续使用用 户提供的 Allocator 。

aclError aclrtAllocatorRegister(aclrtStream stream, aclrtAllocatorDesc allocatorDesc)

| 参数名    | 输入 / 输 出   | 说明                                                                              |
|--------|------------|---------------------------------------------------------------------------------|
| stream | 输入         | 该 Allocator 需要注册的 Stream 。类型定义请参见 aclrtStream 。 传入的 stream 参数值不能为 NULL ，否则返回报错。 |

## 返回值说明

## 约束说明

## 参考资源

| 参数名            | 输入 / 输 出   | 说明                                           |
|----------------|------------|----------------------------------------------|
| allocator Desc | 输入         | Allocator 描述符指针。类型定义请参见 aclrtAllocatorDesc 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 当前仅支持在单算子模型执行、动态 shape 模型推理场景下使用本接口。 单算子模型场景下，需在算子执行接口（例如 aclopExecuteV2 ）之前调用本接 口。

动态 shape 模型推理场景，本接口需配合 aclmdlExecuteAsync 接口一起使用，且 需在 aclmdlExecuteAsync 接口之前调用本接口。

- 调用本接口前，需要先调用 aclrtAllocatorCreateDesc 创建 Allocator 描述符，再 分别调用 aclrtAllocatorSetObjToDesc 、 aclrtAllocatorSetAllocFuncToDesc 、 aclrtAllocatorSetGetAddrFromBlockFuncToDesc 、 aclrtAllocatorSetFreeFuncToDesc 设置 Allocator 对象及回调函数。 Allocator 描 述符使用完成后，可调用 aclrtAllocatorDestroyDesc 接口销毁 Allocator 描述符。
- 对于同一条流，多次调用本接口，以最后一次注册为准。
- 对于不同流，如果用户使用同一个 Allocator ，不可以多条流并发执行，在执行下 一条 Stream 前，需要对上一 Stream 做流同步。
- 将 Allocator 中的内存释放给操作系统前，需要先调用 aclrtSynchronizeStream 接 口执行流同步，确保 Stream 中的任务已执行完成。

接口调用示例，参见动态 Shape 输入（设置 Shape 范围）。
