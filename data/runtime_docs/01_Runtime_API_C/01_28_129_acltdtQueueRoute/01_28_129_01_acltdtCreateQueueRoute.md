# acltdtCreateQueueRoute

> **Section**: 1.28.129.1


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |
| Atlas 推理系列产品           | √      |
| Atlas 训练系列产品           | √      |

创建 acltdtQueueRoute 类型的数据，表示创建队列路由配置。

acltdtQueueRoute* acltdtCreateQueueRoute(uint32\_t srcId, uint32\_t dstId)

| 参数名   | 输入 / 输 出   | 说明        |
|-------|------------|-----------|
| srcId | 输入         | 源队列 ID 。  |
| dstId | 输入         | 目的队列 ID 。 |

- 返回 acltdtQueueRoute 类型的指针，表示成功。
- 返回 nullptr ，表示失败。
