# aclrtCntNotifyWaitWithTimeout

> **Section**: 1.11.3


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

阻塞指定 Stream 的运行，直到指定的 CntNotify 完成。异步接口。

aclError aclrtCntNotifyWaitWithTimeout(aclrtCntNotify cntNotify, aclrtStream stream, aclrtCntNotifyWaitInfo *info)

| 参数名       | 输入 / 输 出   | 说明                                                                                                                      |
|-----------|------------|-------------------------------------------------------------------------------------------------------------------------|
| cntNotify | 输入         | 需等待的 CntNotify 。类型定义请参见 aclrtCntNotify 。                                                                                |
| stream    | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 如果使用默认 Stream ，此处设置为 NULL 。 多 Stream 同步等待场景下，例如， Stream2 等 Stream1 的场景，此处配置为 Stream2 。 |
| info      | 输入         | 控制 Wait 的行为模式。类型定义请参见 aclrtCntNotifyWaitInfo 。                                                                          |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
