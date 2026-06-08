# aclmdlRIGetName

> **Section**: 1.17.20


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

获取模型运行实例的名称。如果没有调用 aclmdlRISetName 接口，调用本接口获取到 的为空字符串。

## 函数原型

## 参数说明

## 返回值说明

aclError aclmdlRIGetName(aclmdlRI modelRI, uint32\_t maxLen, char *name)

| 参数名     | 输入 / 输 出   | 说明                                                      |
|---------|------------|---------------------------------------------------------|
| modelRI | 输入         | 模型运行实例。类型定义请参见 aclmdlRI 。                               |
| maxLen  | 输入         | 用户申请的用于存放 name 的最大内存长度，单位 Byte 。                        |
| name    | 输出         | 模型运行实例的名称。 name 的最大长度为 512Byte ，超过 512Byte 的部分将被截断 并返回。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
