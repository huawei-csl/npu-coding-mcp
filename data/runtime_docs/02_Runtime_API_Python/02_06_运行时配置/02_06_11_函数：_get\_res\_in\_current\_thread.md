# 函数： get\_res\_in\_current\_thread

> **Section**: 2.6.11


## 产品支持情况

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |

在当前线程中取消使用指定 Stream 上的 Device 资源限制。

- C 函数原型

aclError aclrtUnuseStreamResInCurrentThread(aclrtStream stream)

- python 函数

ret = acl.rt.unuse\_stream\_res\_in\_current\_thread(stream)

| 参数名    | 说明                                    |
|--------|---------------------------------------|
| stream | int ，指定 stream ，若传入 0 ，则表示默认 Stream 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| value | int ，当前线程资源限制的大小。         |
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
