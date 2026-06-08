# aclprofStop

> **Section**: 1.21.1.5


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

停止 Profiling 数据采集。

aclError aclprofStop(const aclprofConfig *profilerConfig)

## 功能说明

## 函数原型

| 参数名             | 输入 / 输 出   | 说明                                                                                                      |
|-----------------|------------|---------------------------------------------------------------------------------------------------------|
| profilerConfi g | 输入         | 指定 Profiling 配置数据。类型定义请参见 aclprofConfig 。 需提前调用 1.28.16.1 aclprofCreateConfig 接口创建 aclprofConfig 类型的数据。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 参数说明

## 返回值说明

## 约束说明

与 aclprofStart 接口配对使用，先调用 aclprofStart 接口再调用 aclprofStop 接口。
