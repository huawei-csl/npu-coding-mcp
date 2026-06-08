# aclrtGetSysParamOpt

> **Section**: 1.5.2


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取当前进程中的运行时参数值。

## 函数原型

## 参数说明

## 返回值说明

如果不调用 aclrtSetSysParamOpt 接口设置运行时参数的值，直接调用本接口可获取 各参数的默认值 0 ，表示不开启确定性计算或内存访问越界检测；调用 aclrtSetSysParamOpt 接口设置运行时参数值后，若需获取参数值，需调用 aclrtGetSysParamOpt 接口。

aclError aclrtGetSysParamOpt(aclSysParamOpt opt, int64\_t *value)

| 参数名   | 输入 / 输 出   | 说明                         |
|-------|------------|----------------------------|
| opt   | 输入         | 运行时参数，请参见 aclSysParamOpt 。 |
| value | 输出         | 运行时参数值。                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
