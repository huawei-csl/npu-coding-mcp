# aclrtValueWait

> **Section**: 1.13.63


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

等待指定内存中的数据满足一定条件后解除阻塞。异步接口。

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

aclError aclrtValueWait(void* devAddr, uint64\_t value, uint32\_t flag, aclrtStream stream)

| 参数名     | 输入 / 输出   | 说明                                                                                                                                                                                                                                                                                                                                               |
|---------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| devAddr | 输入        | Device 侧内存地址。 devAddr 的有效内存位宽为 64bit 。                                                                                                                                                                                                                                                                                                           |
| value   | 输入        | 需与内存中的数据作比较的值。                                                                                                                                                                                                                                                                                                                                   |
| flag    | 输入        | 比较的方式，等满足条件后解除阻塞。取值如下： #define ACL_STREAM_WAIT_VALUE_GEQ 0x00000000U // 等到 (int64_t) (*devAddr - value) >= 0 #define ACL_STREAM_WAIT_VALUE_EQ 0x00000001U // 等到 *devAddr == value #define ACL_STREAM_WAIT_VALUE_AND 0x00000002U // 等到 (*devAddr & value) != 0 #define ACL_STREAM_WAIT_VALUE_NOR 0x00000003U // 等到 ~ (*devAddr &#124; value) != 0 |
| stream  | 输入        | 执行等待任务的 stream 。类型定义请参见 aclrtStream 。 此处支持传 NULL ，表示使用默认 Stream 。                                                                                                                                                                                                                                                                                |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见内存语义同步。
