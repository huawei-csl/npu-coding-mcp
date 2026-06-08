# aclrtSetTsDevice

> **Section**: 1.6.6


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

设置本次计算需要使用的 Task Schedule 。

aclError aclrtSetTsDevice(aclrtTsId tsId)

| 参数名   | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                          |
|-------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tsId  | 输入         | 指定本次计算需要使用的 Task Schedule 。如果 AI 处理器中 只有 AI CORE Task Schedule ，没有 VECTOR Core Task Schedule ，则设置该参数无效，默认使用 AI CORE Task Schedule 。 typedef enum aclrtTsId { ACL_TS_ID_AICORE = 0, // 使用 AI CORE Task Schedule ACL_TS_ID_AIVECTOR = 1, // 使用 VECTOR Core Task Schedule ACL_TS_ID_RESERVED = 2, } aclrtTsId; |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 功能说明

## 函数原型

## 参数说明

## 返回值说明
