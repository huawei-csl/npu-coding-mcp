# aclrtCreateStreamWithConfig

> **Section**: 1.8.2


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

## 在当前进程或线程中创建 Stream 。

- 针对如下产品型号，相比 aclrtCreateStream 接口，使用本接口可以创建一个快速 下发任务的 Stream ，但会增加内存消耗或 CPU 的性能消耗。

Atlas 350 加速卡

Atlas A3 训练系列产品 /Atlas A3 推理系列产品

Atlas A2 训练系列产品 /Atlas A2 推理系列产品

Atlas 推理系列产品

Atlas 训练系列产品

- 针对如下产品型号，使用本接口与 aclrtCreateStream 接口是等价的。 Atlas 200I/500 A2 推理产品

## 函数原型

## 参数说明

## flag 取值说明

aclError aclrtCreateStreamWithConfig(aclrtStream *stream, uint32\_t priority, uint32\_t flag)

| 参数名      | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                               |
|----------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| stream   | 输出         | Stream 的指针。类型定义请参见 aclrtStream 。                                                                                                                                                                                                                                                 |
| priority | 输入         | 优先级。 Atlas 推理系列产品上，该参数取值范围： [0, 7] ，总共最多 支持 8 个优先级，数字越小代表优先级越高，其中， 0 的优先 级最高， 7 的优先级最低。如果设置的优先级超过取值范 围，则就近修正为边界值。 对以下产品，该参数为预留参数，暂不使用，当前固定设置 为 0 ： ● Atlas 350 加速卡 ● Atlas A3 训练系列产品 /Atlas A3 推理系列产品 ● Atlas A2 训练系列产品 /Atlas A2 推理系列产品 ● Atlas 200I/500 A2 推理产品 ● Atlas 训练系列产品 |
| flag     | 输入         | Stream 指针的fl ag 。 flag 参数值请参见'fl ag 取值说明'。                                                                                                                                                                                                                                       |

flag 既支持配置单个宏，也支持配置多个宏位或（例如 ACL\_STREAM\_FAST\_LAUNCH | ACL\_STREAM\_FAST\_SYNC ）。对于不支持位或的宏，本接口会返回报错。配置其他值 创建出来的 Stream 等同于通过 aclrtCreateStream 接口创建出来的 Stream 。

- ACL\_STREAM\_FAST\_LAUNCH ：使用该fl ag 创建出来的 Stream ，在使用 Stream 时，下发任务的速度更快。

相比 aclrtCreateStream 接口创建出来的 Stream ，在使用 Stream 时才会申请系统 内部资源，导致下发任务的时长增加，使用本接口的

ACL\_STREAM\_FAST\_LAUNCH 模式创建 Stream 时，会在创建 Stream 时预申请系 统内部资源，因此创建 Stream 的时长增加，下发任务的时长缩短，总体来说，创 建一次 Stream ，使用多次的场景下，总时长缩短，但创建 Stream 时预申请内部资 源会增加内存消耗。

#define ACL\_STREAM\_FAST\_LAUNCH      0x00000001U

- ACL\_STREAM\_FAST\_SYNC ：使用该fl ag 创建出来的 Stream ，在调用 aclrtSynchronizeStream
- 接口时，会阻塞当前线程，主动查询任务的执行状态， 一旦任务完成，立即返回。 相比 aclrtCreateStream 接口创建出来的 Stream ，在调用 aclrtSynchronizeStream 接口时，会一直被动等待 Device 上任务执行完成的通 知，等待时间长，使用本接口的 ACL\_STREAM\_FAST\_SYNC 模式创建的 Stream ， 没有被动等待，总时长缩短，但主动查询的操作会增加 CPU 的性能消耗。

## 返回值说明

## 接口调用示例

#define ACL\_STREAM\_FAST\_SYNC        0x00000002U

- ACL\_STREAM\_PERSISTENT ：使用该fl ag 创建出来的 Stream ，在该 Stream 上下 发的任务不会立即执行、任务执行完成后也不会立即销毁，在销毁 Stream 时才会 销毁任务相关的资源。该方式下创建的 Stream 用于与模型绑定，适用于模型构建 场景，模型构建相关接口的说明请参见 1.17.12 aclmdlRIBindStream 。 #define ACL\_STREAM\_PERSISTENT       0x00000004U
- ACL\_STREAM\_HUGE ：相比其他fl ag ，使用该fl ag 创建出来的 Stream 所能容纳的 Task 最大数量更大。

当前版本设置该fl ag 不生效。

#define ACL\_STREAM\_HUGE             0x00000008U

- ACL\_STREAM\_CPU\_SCHEDULE ：使用该fl ag 创建出来的 Stream 用于队列方式模 型推理场景下承载 AI CPU 调度的相关任务。预留功能。 #define ACL\_STREAM\_CPU\_SCHEDULE     0x00000010U
- ACL\_STREAM\_DEVICE\_USE\_ONLY ：表示该 Stream 仅在 Device #define ACL\_STREAM\_DEVICE\_USE\_ONLY  0x00000020U 仅如下型号支持 ACL\_STREAM\_DEVICE\_USE\_ONLY ：

Atlas 350 加速卡

Atlas A3 训练系列产品 /Atlas A3 推理系列产品

Atlas A2 训练系列产品 /Atlas A2 推理系列产品

Atlas 推理系列产品

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见配置 Stream 优先级。
