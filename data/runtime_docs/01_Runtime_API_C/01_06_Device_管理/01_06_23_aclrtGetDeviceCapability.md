# aclrtGetDeviceCapability

> **Section**: 1.6.23


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

查询支持的特性信息。

aclError aclrtGetDeviceCapability(int32\_t deviceId, aclrtDevFeatureType devFeatureType, int32\_t *value)

## 参数说明

## 返回值说明

| 参数名             | 输入 / 输出   | 说明                                                                                                                                                                                |
|-----------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| deviceId        | 输入        | Device ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数 量后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数 量 -1)] 。                                                                          |
| devFeatur eType | 输入        | 特性类型。类型定义请参见 aclrtDevFeatureType 。                                                                                                                                                |
| value           | 输出        | 特性是否支持。 ● ACL_DEV_FEATURE_NOT_SUPPORT(0) ：不支持 ● ACL_DEV_FEATURE_SUPPORT(1) ：支持 相关宏定义如下： #define ACL_DEV_FEATURE_SUPPORT 0x00000001 #define ACL_DEV_FEATURE_NOT_SUPPORT 0x00000000 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
