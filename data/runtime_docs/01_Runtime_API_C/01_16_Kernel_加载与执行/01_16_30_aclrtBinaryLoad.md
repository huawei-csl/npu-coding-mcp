# aclrtBinaryLoad

> **Section**: 1.16.30


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

解析、加载算子二进制文件，输出指向算子二进制的 binHandle ，同时将算子二进制文 件数据拷贝至当前 Context 对应的 Device 上。此处的算子为使用 Ascend C 语言开发的自 定义算子。

aclError aclrtBinaryLoad(const aclrtBinary binary, aclrtBinHandle *binHandle)

| 参数名       | 输入 / 输 出   | 说明                                                           |
|-----------|------------|--------------------------------------------------------------|
| binary    | 输入         | 算子二进制信息。 此处需先调用 aclrtCreateBinary 接口，获取 aclrtBinary 类型数据的指针。 |
| binHandle | 输出         | 指向二进制的 handle 。类型定义请参见 aclrtBinHandle 。                      |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
