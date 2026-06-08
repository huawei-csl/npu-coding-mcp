# aclprofMark

> **Section**: 1.21.2.4


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

msproftx 标记瞬时事件。

调用此接口后， Profiling 自动在 Stamp 指针中加上当前时间戳，将 Event type 设置为 Mark ，表示开始一次 msproftx 采集。

aclError aclprofMark(void *stamp)

| 参数名   | 输入 / 输 出   | 说明                                                      |
|-------|------------|---------------------------------------------------------|
| stamp | 输入         | Stamp 指针，指代 msproftx 事件标记。 指定 aclprofCreateStamp 接口的指针。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

在 1.21.2.2 aclprofCreateStamp 接口和 1.21.2.10 aclprofDestroyStamp 接口之间调 用。

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明
