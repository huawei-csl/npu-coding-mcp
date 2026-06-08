# 函数： stream\_get\_id

> **Section**: 2.9.12


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
| Atlas 200I/500 A2 推理产品            | √      |

获取指定 Stream 的 ID 。

- C 函数原型

aclError aclrtStreamGetId(aclrtStream stream, int32\_t *streamId)

- python 函数
- stream\_id, ret = acl.rt.stream\_get\_id(stream)

| 参数名    | 说明                                            |
|--------|-----------------------------------------------|
| stream | int ，指定要查询的 Stream 指针地址，若传入 0 ，则操作默认 Stream 。 |

## 返回值说明

| 返回值       | 说明                                           |
|-----------|----------------------------------------------|
| stream_id | int ， stream ID 。                            |
| ret       | int ，返回 0 表示成功，返回其他值表示失败，请参见 17.1-aclError 。 |
