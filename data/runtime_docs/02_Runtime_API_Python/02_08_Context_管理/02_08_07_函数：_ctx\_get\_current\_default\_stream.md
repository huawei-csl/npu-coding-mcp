# 函数： ctx\_get\_current\_default\_stream

> **Section**: 2.8.7


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

获取 Context 上的默认 Sream 。

- C 函数原型

aclError aclrtCtxGetCurrentDefaultStream(aclrtStream *stream)

- python 函数

stream, ret = acl.rt.ctx\_get\_current\_default\_stream()

无

| 返回值    | 说明                   |
|--------|----------------------|
| stream | int ，获取到的默认 Stream 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
