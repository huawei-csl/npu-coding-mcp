# 函数： ctx\_get\_sys\_param\_opt

> **Section**: 2.8.5


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取当前 Context 中的系统参数值。

- C 函数原型

aclError aclrtCtxGetSysParamOpt(aclSysParamOpt opt, int64\_t *value)

- python 函数

value, ret = acl.rt.ctx\_get\_sys\_param\_opt(opt)

| 参数名   | 说明                                    |
|-------|---------------------------------------|
| opt   | int ，系统参数，参考 2.19.50 aclSysParamOpt 。 |
| value | int ，系统参数值。                           |

## 返回值说明

## 约束说明

系统参数无默认值，如果不调用 acl.rt.ctx\_set\_sys\_param\_opt 接口设置系统参数的 值，直接调用本接口获取系统参数的值，接口会返回失败。
