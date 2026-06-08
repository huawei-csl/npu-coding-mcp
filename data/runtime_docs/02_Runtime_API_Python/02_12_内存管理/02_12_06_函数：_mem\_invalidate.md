# 函数： mem\_invalidate

> **Section**: 2.12.6


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

将 cache 中的数据设置成无效。

该版本不需要用户处理 CPU 与 NPU 之间的 cache 一致性，无需调用该接口。

- C 函数原型

aclError aclrtMemInvalidate(void *devPtr, size\_t size)

- python 函数

ret = acl.rt.mem\_invalidate(dev\_ptr, size)

| 参数名    | 说明                                      |
|--------|-----------------------------------------|
| devPtr | int ，需要指定 DDR 内存对应的 cache 无效。           |
| size   | int ， DDR 内存大小，单位 Byte 。' size '不能为 0 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
