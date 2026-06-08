# aclrtCtxGetSysParamOpt

> **Section**: 1.7.6


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取当前 Context 中的系统参数值。

系统参数无默认值，如果不调用 aclrtCtxSetSysParamOpt 接口设置系统参数的值，直 接调用本接口获取系统参数的值，接口会返回失败。

aclError aclrtCtxGetSysParamOpt(aclSysParamOpt opt, int64\_t *value)

| 参数名   | 输入 / 输 出   | 说明                            |
|-------|------------|-------------------------------|
| opt   | 输入         | 系统参数。类型定义请参见 aclSysParamOpt 。 |
| value | 输出         | 存放系统参数值的内存的指针。                |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
