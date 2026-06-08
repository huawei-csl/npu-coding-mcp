# aclrtHostMemMapCapabilities

> **Section**: 1.13.61


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

查询指定的硬件驱动加速器是否支持访问通过 aclrtHostRegister 接口注册的内存。

aclError aclrtHostMemMapCapabilities(uint32\_t deviceId, aclrtHacType hacType, aclrtHostMemMapCapability *capabilities)

| 参数名          | 输入 / 输 出   | 说明                                                                                                   |
|--------------|------------|------------------------------------------------------------------------------------------------------|
| deviceId     | 输入         | Device ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |
| hacType      | 输入         | HAC （ Hardware Accelerator Controller ，硬件加速控 制器）类型。类型定义请参见 aclrtHacType 。                            |
| capabilities | 输出         | 是否支持访问通过 aclrtHostRegister 接口注册的内存。 类型定义请参见 aclrtHostMemMapCapability 。                              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
