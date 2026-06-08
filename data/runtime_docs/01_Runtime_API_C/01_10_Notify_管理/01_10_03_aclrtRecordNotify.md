# aclrtRecordNotify

> **Section**: 1.10.3


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

在指定 Stream 上记录一个 Notify 。异步接口。

aclrtRecordNotify 接口与 aclrtWaitAndResetNotify 接口配合使用时，主要用于多 Stream 之间同步等待的场景。

aclError aclrtRecordNotify(aclrtNotify notify, aclrtStream stream)

| 参数名    | 输入 / 输出   | 说明                                                                                           |
|--------|-----------|----------------------------------------------------------------------------------------------|
| notify | 输入        | 待记录的 Notify 。类型定义请参见 aclrtNotify 。                                                           |
| stream | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。 多 Stream 同步等待场景下，例如， Stream2 等 Stream1 的 场景，此处配置为 Stream1 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 接口调用示例

接口调用示例，参见基于 Notify 同步。
