# 函数： reduce\_async

> **Section**: 2.13.7


## 产品支持情况

## 功能说明

## 函数原型

- C 函数原型

aclError aclrtGetThreadLastTaskId(uint32\_t *taskId)

- python 函数

task\_id, ret = acl.rt.get\_thread\_last\_task\_id()

无

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

执行 Reduce 操作，包括 SUM 、 MIN 、 MAX 等。

本接口是异步接口，调用接口成功仅表示任务下发成功，不表示任务执行成功。调用 该接口后，需调用同步等待接口（例如， synchronize\_stream ）确保任务已执行完 成，否则可能会导致训练或推理等业务异常、 Device 断链掉卡等未知情况。

- C 函数原型

## 参数说明

## 返回值说明

## 约束说明

aclError aclrtReduceAsync(void *dst, const void *src, uint64\_t count, aclrtReduceKind kind, aclDataType type, aclrtStream stream, void *reserve)

## ● python 函数

ret = acl.rt.reduce\_async(dst, src, count, kind, type, stream, reserve)

| 参数名     | 说明                                                                                                                                                                                                                                                                                                                                           |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dst     | int ，目的内存地址指针。                                                                                                                                                                                                                                                                                                                               |
| src     | int ，源内存地址指针。                                                                                                                                                                                                                                                                                                                                |
| count   | int ，源内存大小，单位为 Byte 。                                                                                                                                                                                                                                                                                                                        |
| kind    | int ，操作类型。具体请参见新增数据结构 aclrtReduceKind 。                                                                                                                                                                                                                                                                                                      |
| type    | int ，数据类型。 Atlas A3 训练系列产品 /Atlas A3 推理系列产品支持如下类型： int8 、 int16 、 int32 、 fp16 、 fp32 、 bf16 。 Atlas A2 训练系列产品 /Atlas A2 推理系列产品支持如下类型： int8 、 int16 、 int32 、 fp16 、 fp32 、 bf16 。 Atlas 200I/500 A2 推理产品支持如下类型： int8 、 int16 、 int32 、 fp16 、 fp32 。 Atlas 推理系列产品支持如下类型： fp32 、 fp16 、 int16 。 Atlas 训练系列产品仅支持 fp32 类型。 具体请参见 aclDataType 。 |
| stream  | int ，指定 Stream 。如果使用默认 Stream ，此处设置为 0 。                                                                                                                                                                                                                                                                                                     |
| reserve | int ，预留参数。当前固定传 NULL 。                                                                                                                                                                                                                                                                                                                       |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

dts 、 src 必须跟 stream 所在的 Device 是同一个设备。
