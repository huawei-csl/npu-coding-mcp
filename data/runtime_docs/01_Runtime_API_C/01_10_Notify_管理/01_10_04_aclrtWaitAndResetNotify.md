# aclrtWaitAndResetNotify

> **Section**: 1.10.4


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

阻塞指定 Stream 的运行，直到指定的 Notify 完成，再复位 Notify 。异步接口。

aclError aclrtWaitAndResetNotify(aclrtNotify notify, aclrtStream stream, uint32\_t timeout)

| 参数名     | 输入 / 输出   | 说明                                                                                           |
|---------|-----------|----------------------------------------------------------------------------------------------|
| notify  | 输入        | 需等待的 Notify 。类型定义请参见 aclrtNotify 。                                                           |
| stream  | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。 多 Stream 同步等待场景下，例如， Stream2 等 Stream1 的 场景，此处配置为 Stream2 。 |
| timeout | 输入        | 等待的超时时间。 取值说明如下： ● 0 ：表示永久等待； ● >0 ：配置具体的超时时间，单位是秒。                                          |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 接口调用示例

接口调用示例，参见基于 Notify 同步。
