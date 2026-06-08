# aclrtStreamGetPriority

> **Section**: 1.8.21


## 产品支持情况

## 功能说明

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

查询指定 Stream 的优先级。

aclError aclrtStreamGetPriority(aclrtStream stream, uint32\_t *priority)

| 参数名      | 输入 / 输 出   | 说明                                                                              |
|----------|------------|---------------------------------------------------------------------------------|
| stream   | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 若此处传入 NULL ，则获取的是默认 Stream 的优先级。               |
| priority | 输出         | 优先级，数字越小代表优先级越高。 关于优先级的取值范围请参见 aclrtCreateStreamWithConfig 接口中的 priority 参数说 明。 |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
