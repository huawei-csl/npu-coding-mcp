# aclprofModelSubscribe

> **Section**: 1.21.3.2


## 产品支持情况

![Figure](../../images/figure_5413.png)

**[Image: figure_5413.png (87x48, 2.1KB)]**

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

网络场景下，订阅算子的基本信息，包括算子名称、算子类型、算子执行耗时等。

aclError aclprofModelSubscribe(uint32\_t modelId, const aclprofSubscribeConfig *profSubscribeConfig)

| 参数名                  | 输入 / 输 出   | 说明                                                                                                                                            |
|----------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| modelId              | 输入         | 待订阅的网络模型的 ID 。 调用 aclmdlLoadFromFile 接口 /aclmdlLoadFromMem 接 口 /aclmdlLoadFromFileWithMem 接口 / aclmdlLoadFromMemWithMem 接口加载模型成功后， 会返回模型 ID 。 |
| profSubscrib eConfig | 输入         | 待订阅的配置信息。 需提前调用 aclprofCreateSubscribeConfig 接口创建 aclprofSubscribeConfig 类型的数据。                                                               |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

与 aclprofModelUnSubscribe 接口配对使用。
