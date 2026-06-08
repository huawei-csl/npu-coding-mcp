# 函数： peek\_at\_last\_error

> **Section**: 2.14.9


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

获取当前线程的 Runtime （运行时管理模块）错误码，仅获取但不清空错误码。

- C 函数原型

aclError aclrtPeekAtLastError(aclrtLastErrLevel level)

- python 函数

ret = acl.rt.peek\_at\_last\_error(level)

| 参数名   | 说明                                                     |
|-------|--------------------------------------------------------|
| level | int ，指定获取错误码的级别，当前仅支持线程级别。参考 2.19.29 aclrtLastErrLevel |

| 返回值   | 说明                         |
|-------|----------------------------|
| ret   | int ，返回 0 表示成功，返回非 0 表示失败。 |
