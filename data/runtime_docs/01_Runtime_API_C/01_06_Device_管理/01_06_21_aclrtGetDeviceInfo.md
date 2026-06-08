# aclrtGetDeviceInfo

> **Section**: 1.6.21


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

获取指定 Device 的信息。

aclError aclrtGetDeviceInfo(uint32\_t deviceId, aclrtDevAttr attr, int64\_t *value)

| 参数名      | 输入 / 输出   | 说明                                                                                                       |
|----------|-----------|----------------------------------------------------------------------------------------------------------|
| deviceId | 输入        | Device ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数 量后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数 量 -1)] 。 |
| attr     | 输入        | 属性。类型定义请参见 aclrtDevAttr 。                                                                                |
| value    | 输出        | 属性值。                                                                                                     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
