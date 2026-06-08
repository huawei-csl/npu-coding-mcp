# aclrtKernelArgsFinalize

> **Section**: 1.16.23


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

在所有参数追加完成后，调用本接口以标识参数组装完毕。

aclError aclrtKernelArgsFinalize(aclrtArgsHandle argsHandle)

## 参数说明

## 返回值说明

| 参数名        | 输入 / 输 出   | 说明                               |
|------------|------------|----------------------------------|
| argsHandle | 输入         | 参数列表句柄。类型定义请参见 aclrtArgsHandle 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
