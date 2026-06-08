# aclprofCreateSubscribeConfig

> **Section**: 1.28.21.1


## 产品支持情况

## 功能说明

## 约束说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

创建 aclprofSubscribeConfig 类型的数据，表示创建订阅配置信息。

如需销毁 aclprofSubscribeConfig 类型的数据，请参见 aclprofDestroySubscribeConfig 。

- 使用 aclprofDestroySubscribeConfig 接口销毁 aclprofSubscribeConfig 类型的数 据，如不销毁会导致内存未被释放。
- 与 aclprofDestroySubscribeConfig 接口配对使用，先调用 aclprofCreateSubscribeConfig 接口再调用 aclprofDestroySubscribeConfig 接口。

aclprofSubscribeConfig *aclprofCreateSubscribeConfig(int8\_t timeInfoSwitch, aclprofAicoreMetrics aicoreMetrics, void *fd)

| 参数名             | 输入 / 输 出   | 说明                                                                                         |
|-----------------|------------|--------------------------------------------------------------------------------------------|
| timeInfoSwit ch | 输入         | 是否采集网络模型中算子的性能数据： ● 1 ：采集 ● 0 ：不采集 类型定义请参见 aclprofSubscribeConfig 和 aclprofAicoreMetrics 。 |
| aicoreMetric s  | 输入         | 表示 AI Core 性能指标采集项。 说明 订阅接口目前仅提供算子耗时统计的功能，暂时不支持 AicoreMetrics 采集功能。                        |

## 返回值说明

| 参数名   | 输入 / 输 出   | 说明                                                                        |
|-------|------------|---------------------------------------------------------------------------|
| fd    | 输入         | 用户创建的管道写指针。 用户在调用 aclprofModelUnSubscribe 接口后，系统内部 会在数据发送结束后，关闭该模型的管道写指针。 |

- 返回 aclprofSubscribeConfig 类型的指针，表示成功。
- 返回 nullptr ，表示失败。
