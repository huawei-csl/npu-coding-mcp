# 函数： get\_stream\_overflow\_switch

> **Section**: 2.9.6


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | x      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | x      |

针对指定 Stream ，获取其当前溢出检测开关是否打开。

- C 函数原型

aclError aclrtGetStreamOverflowSwitch(aclrtStream stream, uint32\_t flag)

- python 函数

flag, ret = acl.rt.get\_stream\_overflow\_switch(stream)

## 参数说明

## 返回值说明

| 返回值   | 说明                                  |
|-------|-------------------------------------|
| flag  | int ，溢出检测开关，取值范围如下。 ● 0 ：关闭 ● 1 ：打开 |
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。       |
