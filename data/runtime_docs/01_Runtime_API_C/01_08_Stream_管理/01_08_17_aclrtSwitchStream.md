# aclrtSwitchStream

> **Section**: 1.8.17


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

根据条件在 Stream 之间跳转。异步接口。

跳转成功后，只执行所跳转的 Stream 上的任务，当前 Stream 上的任务停止执行。

aclError aclrtSwitchStream(void *leftValue, aclrtCondition cond, void *rightValue, aclrtCompareDataType dataType, aclrtStream trueStream, aclrtStream falseStream, aclrtStream stream)

![Figure](../../images/figure_1360.png)

**[Image: figure_1360.png (210x59, 8.5KB)]**

## 返回值说明

| 参数名          | 输入 / 输 出   | 说明                                                             |
|--------------|------------|----------------------------------------------------------------|
| leftValue    | 输入         | 左值数据的 Device 内存地址。                                             |
| cond         | 输入         | 左值数据与右值数据的比较条件。类型定义请参见 aclrtCondition 。                        |
| rightValu e  | 输入         | 右值数据的 Device 内存地址。                                             |
| dataType     | 输入         | 左值数据、右值数据的数据类型。类型定义请参见 aclrtCompareDataType 。                  |
| trueStrea m  | 输入         | 根据 cond 处指定的条件，条件成立时，则执行 trueStream 上的任务。类型定义请参见 aclrtStream 。 |
| falseStre am | 输入         | 预留参数，当前固定传 NULL 。                                              |
| stream       | 输入         | 执行跳转任务的 Stream 。类型定义请参见 aclrtStream 。                          |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
