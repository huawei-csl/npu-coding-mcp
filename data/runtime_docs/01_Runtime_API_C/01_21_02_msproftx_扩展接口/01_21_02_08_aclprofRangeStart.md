# aclprofRangeStart

> **Section**: 1.21.2.8


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |

## 功能说明

## 函数原型

## 返回值说明

## 约束说明

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | √      |
| Atlas 训练系列产品 | √      |

msproftx 用于记录事件发生的时间跨度的开始时间。

调用此接口后， Profiling 自动在 Stamp 指针记录采集开始的时间戳，将 Event type 设置 为 Start/Stop ，生成一个进程唯一的 id ，并将 Stamp 保存在以进程粒度维护的一个 map 中。

aclError aclprofRangeStart(void *stamp, uint32\_t *rangeId)

| 参数名     | 输入 / 输 出   | 说明                                                      |
|---------|------------|---------------------------------------------------------|
| stamp   | 输入         | Stamp 指针，指代 msproftx 事件标记。 指定 aclprofCreateStamp 接口的指针。 |
| rangeId | 输出         | msproftx 事件标记的唯一标识。用于在跨线程时区分。                           |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 与 1.21.2.9 aclprofRangeStop 接口成对使用，表示时间跨度的开始和结束。
- 在 1.21.2.2 aclprofCreateStamp 接口和 1.21.2.10 aclprofDestroyStamp 接口之 间调用。
- 可以跨线程调用。
