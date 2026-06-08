# aclrtSubscribeHostFunc

> **Section**: 1.27.16


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

调用本接口注册处理 Stream 上回调函数的线程（线程需由用户自行创建）。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

aclError aclrtSubscribeHostFunc(uint64\_t hostFuncThreadId, aclrtStream exeStream)

![Figure](../../images/figure_6129.png)

**[Image: figure_6129.png (106x102, 7.5KB)]**

| 参数名               | 输入 / 输出   | 说明                               |
|-------------------|-----------|----------------------------------|
| hostFuncThrea dId | 输入        | 指定线程的 ID 。                       |
| exeStream         | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 支持多次调用 aclrtSubscribeHostFunc 接口给多个 Stream （仅支持同一 Device 内 的多个 Stream ）注册同一个处理回调函数的线程。
- 为确保 Stream 内的任务按调用顺序执行，不支持调用 aclrtSubscribeHostFunc 接 口给同一个 Stream 注册多个处理回调函数的线程。
