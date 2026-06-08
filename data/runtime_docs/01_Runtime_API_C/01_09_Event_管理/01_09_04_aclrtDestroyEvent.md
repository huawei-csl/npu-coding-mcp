# aclrtDestroyEvent

> **Section**: 1.9.4


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

销毁 Event ，支持在 Event 未完成前调用本接口销毁 Event 。此时，本接口不会阻塞线程 等 Event 完成， Event 相关资源会在 Event 完成时被自动释放。

aclError aclrtDestroyEvent(aclrtEvent event)

| 参数名   | 输入 / 输 出   | 说明                               |
|-------|------------|----------------------------------|
| event | 输入         | 待销毁的 Event 。类型定义请参见 aclrtEvent 。 |

## 返回值说明

## 约束说明

## 接口调用示例

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

在调用 aclrtDestroyEvent 接口销毁指定 Event 时，需确保其它接口没有正在使用该 Event 。

接口调用示例，参见 Event 的创建与销毁。
