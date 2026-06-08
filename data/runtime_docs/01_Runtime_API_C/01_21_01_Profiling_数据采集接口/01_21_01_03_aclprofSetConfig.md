# aclprofSetConfig

> **Section**: 1.21.1.3


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

aclprofCreateConfig 接口的扩展接口，用于设置性能数据采集参数。

该接口支持多次调用，用户需要保证数据的一致性和准确性。

aclError aclprofSetConfig(aclprofConfigType configType, const char *config, size\_t configLength)

## 功能说明

## 函数原型

| 参数名                 | 输入 / 输 出   | 说明                                                 |
|---------------------|------------|----------------------------------------------------|
| profilerResul tPath | 输入         | 指定保存性能数据的文件的路径，支持配置为绝对路径 或相对路径。                    |
| length              | 输入         | profilerResultPath 的长度，单位为 Byte ，最大长度不超 过 4096 字节。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 参数说明

## 返回值说明

## 约束说明

先调用 aclprofSetConfig 接口再调用 aclprofStart 接口，可根据需求选择调用该接口。
