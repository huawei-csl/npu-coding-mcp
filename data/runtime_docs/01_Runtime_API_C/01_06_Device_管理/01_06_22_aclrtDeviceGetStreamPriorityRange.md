# aclrtDeviceGetStreamPriorityRange

> **Section**: 1.6.22


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

查询硬件支持的 Stream 最低、最高优先级。

aclError aclrtDeviceGetStreamPriorityRange(int32\_t *leastPriority, int32\_t *greatestPriority)

## 参数说明

## 返回值说明

## 接口调用示例

| 参数名               | 输入 / 输 出   | 说明     |
|-------------------|------------|--------|
| leastPriority     | 输出         | 最低优先级。 |
| greatestPrio rity | 输出         | 最高优先级。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见配置 Stream 优先级。
