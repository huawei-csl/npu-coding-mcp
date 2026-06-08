# aclrtGetStreamAttribute

> **Section**: 1.8.15


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

获取 Stream 属性值。

aclError aclrtGetStreamAttribute(aclrtStream stream, aclrtStreamAttr stmAttrType, aclrtStreamAttrValue *value)

## 参数说明

## 返回值说明

| 参数名         | 输入 / 输出   | 说明                                                                                                                                                                                                                                  |
|-------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| stream      | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。 各产品型号对默认 Stream （即该参数传入 NULL ）的支持情况不同，如下： Atlas 350 加速卡，不支持 Atlas A3 训练系列产品 /Atlas A3 推理系列产品， 支持 Atlas A2 训练系列产品 /Atlas A2 推理系列产品， 支持 Atlas 200I/500 A2 推理产品，不支持 Atlas 推理系列产品，不支持 Atlas 训练系列产品，不支持 |
| stmAttrType | 输入        | 属性类型。类型定义请参见 aclrtStreamAttr 。                                                                                                                                                                                                      |
| value       | 输出        | 属性值。类型定义请参见 aclrtStreamAttrValue 。                                                                                                                                                                                                  |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
