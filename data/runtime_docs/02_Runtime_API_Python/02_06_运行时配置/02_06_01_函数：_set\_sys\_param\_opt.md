# 函数： set\_sys\_param\_opt

> **Section**: 2.6.1


## 产品支持情况

## 功能说明

count, ret = acl.finalize\_reference()

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

设置当前进程中的运行时参数值。调用本接口设置运行时参数值后，若需获取参数 值，需调用 acl.rt.get\_sys\_param\_opt 接口。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

本接口与 acl.rt.ctx\_set\_sys\_param\_opt 接口的差别是，本接口作用域是进程， acl.rt.ctx\_set\_sys\_param\_opt 接口作用域是 Context 。

- C 函数原型

aclError aclrtSetSysParamOpt(aclrtSysParamOpt opt, int64\_t value)

- python 函数

ret = acl.rt.set\_sys\_param\_opt(opt, value)

| 参数名   | 说明                               |
|-------|----------------------------------|
| opt   | int ，运行时系统参数，参考 aclSysParamOpt 。 |
| value | int ，运行时参数值。                     |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |

多次调用本接口，以最后一次设置的值为准。
