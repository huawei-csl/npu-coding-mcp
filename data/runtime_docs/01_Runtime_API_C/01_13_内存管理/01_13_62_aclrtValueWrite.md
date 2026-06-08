# aclrtValueWrite

> **Section**: 1.13.62


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

向指定内存中写数据。异步接口。

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

aclError aclrtValueWrite(void* devAddr, uint64\_t value, uint32\_t flag, aclrtStream stream)

| 参数名     | 输入 / 输出   | 说明                                                                                         |
|---------|-----------|--------------------------------------------------------------------------------------------|
| devAddr | 输入        | Device 侧内存地址。 此处需用户提前申请 Device 内存（例如调用 aclrtMalloc 接 口）， devAddr 要求 8 字节对齐，有效内存位宽为 64bit 。 |
| value   | 输入        | 需向内存中写入的数据。                                                                                |
| flag    | 输入        | 预留参数，当前固定设置为 0 。                                                                           |
| stream  | 输入        | 执行写数据任务的 stream 。类型定义请参见 aclrtStream 。 此处支持传 NULL ，表示使用默认 Stream 。                         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见内存语义同步。
