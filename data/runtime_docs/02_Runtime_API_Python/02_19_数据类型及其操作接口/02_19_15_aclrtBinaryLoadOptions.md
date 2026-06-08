# aclrtBinaryLoadOptions

> **Section**: 2.19.15


## 说明

## 定义

## 成员

加载算子二进制文件的可选参数。

options = [{"type": option\_type, "value": option\_value}]

说明： options 中可同时包含多个 dict ，每个 dict 中包含一对 type 和 value 。

| 成员名称         | 说明                                          |
|--------------|---------------------------------------------|
| option_type  | int ，参数类型，取值参考 aclrtBinaryLoadOptionType 。  |
| option_value | int ，参数取值，取值参考 aclrtBinaryLoadOptionValue 。 |

说明： option\_type 和 option\_value 配对使用， option\_value 随着 option\_type 的取值来 配置不同的值。
