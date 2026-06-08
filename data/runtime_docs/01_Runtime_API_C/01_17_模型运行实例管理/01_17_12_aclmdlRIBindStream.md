# aclmdlRIBindStream

> **Section**: 1.17.12


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

将模型运行实例与 Stream 绑定。

aclError aclmdlRIBindStream(aclmdlRI modelRI, aclrtStream stream, uint32\_t flag)

| 参数名     | 输入 / 输出   | 说明                                                                             |
|---------|-----------|--------------------------------------------------------------------------------|
| modelRI | 输入        | 模型运行实例。类型定义请参见 aclmdlRI 。 此处的 modelRI 需与 aclmdlRIBuildBegin 接口中的 modelRI 保持一致。 |

## 返回值说明

| 参数名    | 输入 / 输出   | 说明                                                                                                                                                                                                                                                                                                    |
|--------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| stream | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。 此处的 Stream 需通过 aclrtCreateStreamWithConfig 接 口创建 ACL_STREAM_PERSISTENT 类型的 Stream 。 不支持传 NULL ，不支持一个 Stream 绑定多个 modelRI 的 场景。                                                                                                                                       |
| flag   | 输入        | 标记该 Stream 是否从模型执行开始时就运行。 ● ACL_MODEL_STREAM_FLAG_HEAD ：首 Stream ，模 型执行开始时就运行的 Stream 。 ● ACL_MODEL_STREAM_FLAG_DEFAULT ：模型执行过 程中，根据分支算子或循环算子激活的 Stream ，后续 可调用 aclrtActiveStream 接口激活 Stream 宏定义如下： #define ACL_MODEL_STREAM_FLAG_HEAD 0x00000000U #define ACL_MODEL_STREAM_FLAG_DEFAULT 0x7FFFFFFFU |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
