# aclprofRangePushEx

> **Section**: 1.21.2.12


## 产品支持情况

## 功能说明

msproftx 用于将字符串转换为哈希 ID 。

uint64\_t aclprofStr2Id(const char *message)

| 参数名     | 输入 / 输 出   | 说明          |
|---------|------------|-------------|
| message | 输入         | 字符信息，例如算子名。 |
| hashId  | 输出         | 哈希 ID 。     |

返回哈希 ID ，如果是 uint64\_t 类型的最大值则表示失败，其他表示成功。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

在 Torch 场景下， msproftx 上报 Tensor 信息。

调用此接口后， Profiling 判断 messageType 为 MESSAGE\_TYPE\_TENSOR\_INFO 时，缓 存 Tensor 信息。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

与 1.21.2.13 aclprofRangePop 接口配对使用，先调用 aclprofRangePushEx 接口再调 用 aclprofRangePop 接口。
