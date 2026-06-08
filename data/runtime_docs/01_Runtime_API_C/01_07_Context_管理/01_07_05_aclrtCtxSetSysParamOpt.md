# aclrtCtxSetSysParamOpt

> **Section**: 1.7.5


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

设置当前 Context 中的系统参数值，多次调用本接口，以最后一次设置的值为准。调用 本接口设置运行时参数值后，若需获取参数值，需调用 aclrtCtxGetSysParamOpt 接 口。

本接口与 aclrtSetSysParamOpt 接口的差别是，本接口作用域是 Context ， aclrtSetSysParamOpt 的作用域是进程。

aclError aclrtCtxSetSysParamOpt(aclSysParamOpt opt, int64\_t value)

## 参数说明

## 返回值说明

| 参数名   | 输入 / 输 出   | 说明                            |
|-------|------------|-------------------------------|
| opt   | 输入         | 系统参数。类型定义请参见 aclSysParamOpt 。 |
| value | 输入         | 系统参数值。                        |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
