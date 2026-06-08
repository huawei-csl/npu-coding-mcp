# aclrtUnSubscribeHostFunc

> **Section**: 1.27.18


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

与 aclrtSubscribeHostFunc 接口配合使用，调用模型执行接口后，调用本接口取消线 程注册， Stream 上的回调函数不再由指定线程处理。

aclError aclrtUnSubscribeHostFunc(uint64\_t hostFuncThreadId, aclrtStream exeStream)

## 参数说明

## 返回值说明

| 参数名               | 输入 / 输 出   | 说明                               |
|-------------------|------------|----------------------------------|
| hostFuncThr eadId | 输入         | 指定线程的 ID 。                       |
| exeStream         | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
