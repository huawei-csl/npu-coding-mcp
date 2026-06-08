# 函数： free\_physical

> **Section**: 2.12.21


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

释放通过 acl.rt.malloc\_physical 接口申请的物理内存。

- C 函数原型

aclError aclrtFreePhysical(aclrtDrvMemHandle handle)

- python 函数

ret = acl.rt.free\_physical(handle)

| 参数名    | 说明                       |
|--------|--------------------------|
| handle | int ，待释放的物理地址信息 handle 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

Ascend RC 形态不支持调用本接口。
