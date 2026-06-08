# aclrtGetDeviceUtilizationRate

> **Section**: 1.6.8


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | √      |
| Atlas 训练系列产品 | √      |

查询 Device 上 Cube 、 Vector 、 AI CPU 等的利用率。

aclError aclrtGetDeviceUtilizationRate(int32\_t deviceId, aclrtUtilizationInfo *utilizationInfo)

| 参数名              | 输入 / 输 出   | 说明                                                                                                    |
|------------------|------------|-------------------------------------------------------------------------------------------------------|
| deviceId         | 输入         | Device ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |
| utilizatio nInfo | 输出         | 利用率信息结构体指针。类型定义参见 aclrtUtilizationInfo 。                                                              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 当使用本接口查询 Vector 利用率时，如果查询结果为 -1 ，则表示 Vector 不存在。
- 当前版本不支持查询 Device 内存利用率，若通过本接口查询内存利用率，返回的 利用率为 -1 。
- 开启 Profiling 功能时，不支持调用本接口查询利用率，接口返回值无实际意义。
- 昇 腾虚拟化实例场景下，不支持调用本接口查询利用率，接口返回值无实际意 义。
