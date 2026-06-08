# aclprofGetStepTimestamp

> **Section**: 1.21.4.1


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

利用单算子模型执行接口实现训练的场景下，使用本接口用于标记迭代开始与结束时 间，为后续 Profiling 解析提供迭代标识，以便以迭代为粒度展示性能数据。

aclError aclprofGetStepTimestamp(aclprofStepInfo* stepInfo, aclprofStepTag tag, aclrtStream stream)

## 参数说明

## 返回值说明

| 参数名      | 输入 / 输 出   | 说明                                                                                                                       |
|----------|------------|--------------------------------------------------------------------------------------------------------------------------|
| stepInfo | 输入         | 指定迭代信息。需提前调用 aclprofCreateStepInfo 接口 创建 aclprofStepInfo 类型的数据。 类型定义请参见 aclprofStepInfo 、 aclprofStepTag 和 aclrtStream 。 |
| tag      | 输入         | 用于标记迭代开始或结束。在迭代开始时传入枚举值 ACL_STEP_START ，迭代结束时需传入枚举值 ACL_STEP_END 。                                                       |
| stream   | 输入         | 指定 Stream 。                                                                                                              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
