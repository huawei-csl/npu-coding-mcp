# aclrtGetOverflowStatus

> **Section**: 1.6.17


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取当前 Device 下所有 Stream 上任务的溢出状态，并将状态值拷贝到用户申请的 Device 内存中。异步接口。

aclError aclrtGetOverflowStatus(void *outputAddr, size\_t outputSize, aclrtStream stream)

| 参数名         | 输入 / 输 出   | 说明                                             |
|-------------|------------|------------------------------------------------|
| outputA ddr | 输入 & 输 出   | 用户申请的 Device 内存，例如通过 aclrtMalloc 接口申请。         |
| outputSi ze | 输入         | 需申请的 Device 内存大小，单位 Byte ，固定大小为 64Byte 。       |
| stream      | 输入         | 指定 Stream ，用于下发溢出状态查询任务。类型定义请参 见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

对于以下产品型号，调用本接口查询出来的溢出状态是进程级别的：

- Atlas 350 加速卡
- Atlas A3 训练系列产品 /Atlas A3 推理系列产品

- Atlas A2 训练系列产品 /Atlas A2 推理系列产品
