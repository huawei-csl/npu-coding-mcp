# aclprofStart

> **Section**: 1.21.1.4


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

下发 Profiling 请求，使能对应数据的采集。

用户可根据需要，在模型执行过程中按需调用 aclprofStart 接口， Profiling 采集到的数 据为调用该接口之后的数据。

aclError aclprofStart(const aclprofConfig *profilerConfig)

## 功能说明

## 函数原型

| 参数名           | 输入 / 输 出   | 说明                                                                                                  |
|---------------|------------|-----------------------------------------------------------------------------------------------------|
| configType    | 输入         | 作为 configType 参数值。每个枚举表示不同采集配置， 若要使用该接口下不同的选项采集多种性能数据，则需 要多次调用该接口，详细请参见 1.28.17 aclprofConfigType 。 |
| config        | 输入         | 指定配置项参数值。                                                                                           |
| configLengt h | 输入         | config 的长度，单位为 Byte ，最大长度不超过 256 字节。                                                                |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 参数说明

## 返回值说明

## 约束说明

与 aclprofStop 接口配对使用，先调用 aclprofStart 接口再调用 aclprofStop 接口。
