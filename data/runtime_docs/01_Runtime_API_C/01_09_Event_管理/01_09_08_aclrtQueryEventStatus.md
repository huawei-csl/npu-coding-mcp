# aclrtQueryEventStatus

> **Section**: 1.9.8


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

查询该 Event 捕获的所有任务的执行状态。具体见 aclrtRecordEvent 接口参考 Event 捕 获的细节。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

如果用户在不同线程上分别调用 aclrtRecordEvent 和 aclrtQueryEventStatus ，可能由 于多线程导致这两个 API 的执行时间乱序，进而导致查询到的 Event 对象的完成状态不 符合预期。
