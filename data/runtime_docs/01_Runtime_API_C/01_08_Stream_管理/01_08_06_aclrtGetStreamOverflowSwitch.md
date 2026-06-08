# aclrtGetStreamOverflowSwitch

> **Section**: 1.8.6


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

针对指定 Stream ，获取其当前溢出检测开关是否打开。

aclError aclrtGetStreamOverflowSwitch(aclrtStream stream, uint32\_t *flag)

## 参数说明

## 返回值说明

| 参数名    | 输入 / 输 出   | 说明                                |
|--------|------------|-----------------------------------|
| stream | 输入         | 待操作 Stream 。类型定义请参见 aclrtStream 。 |
| flag   | 输出         | 溢出检测开关，取值范围如下： ● 0 ：关闭 ● 1 ：打开    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
