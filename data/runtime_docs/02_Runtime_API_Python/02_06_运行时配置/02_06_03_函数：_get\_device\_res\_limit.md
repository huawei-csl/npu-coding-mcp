# 函数： get\_device\_res\_limit

> **Section**: 2.6.3


## 产品支持情况

获取当前进程中的运行时参数值。

如果不调用 acl.rt.set\_sys\_param\_opt 接口设置运行时参数的值，直接调用本接口可获 取各参数的默认值 0 ，表示不开启确定性计算或内存访问越界检测；调用 acl.rt.set\_sys\_param\_opt 接口设置运行时参数值后，若需获取参数值，需调用

acl.rt.get\_sys\_param\_opt 接口。

## ● C 函数原型

aclError aclrtGetSysParamOpt(aclrtSysParamOpt opt, int64\_t *value)

- python 函数

value, ret = acl.rt.get\_sys\_param\_opt(opt)

| 参数名   | 说明                               |
|-------|----------------------------------|
| opt   | int ，运行时系统参数，参考 aclSysParamOpt 。 |

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

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
| value | int ，资源限制的大小。                 |
