# aclrtDeviceGetUuid

> **Section**: 1.6.30


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

获取 Device 的唯一标识 UUID （ Universally Unique Identifier ）。

aclError aclrtDeviceGetUuid(int32\_t deviceId, aclrtUuid *uuid)

| 参数名      | 输入 / 输 出   | 说明                                                |
|----------|------------|---------------------------------------------------|
| deviceId | 输入         | Device ID ，与 aclrtSetDevice 接口中的 Device ID 保持一 致。 |

## 返回值说明

| 参数名   | 输入 / 输 出   | 说明                               |
|-------|------------|----------------------------------|
| uuid  | 输出         | Device 的唯一标识。类型定义请参见 aclrtUuid 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
