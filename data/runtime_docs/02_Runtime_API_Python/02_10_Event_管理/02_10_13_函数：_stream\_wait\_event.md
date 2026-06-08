# 函数： stream\_wait\_event

> **Section**: 2.10.13


## 产品支持情况

## 功能说明

## 函数原型

| 返回值   | 说明                               |
|-------|----------------------------------|
| ms    | float ，表示的是两个 Event 之间的耗时，单位是毫秒。 |
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。    |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

阻塞指定 Stream 的运行，直到指定的 Event 完成，支持多个 Stream 等待同一个 Event 的 场景。异步接口。

提交到 Stream 上的所有后续任务都需要等待 Event 捕获的任务都完成后才能开始执行。 具体见 acl.rt.record\_event 接口了解 Event 捕获的细节。

- C 函数原型 aclError aclrtStreamWaitEvent(aclrtStream stream, aclrtEvent event)
- python 函数
- ret = acl.rt.stream\_wait\_event(stream, event)

## 参数说明

## 返回值说明

## 约束说明

## 资源参考

接口调用示例，参见关于 Event 的同步等待、关于 Stream 间任务的同步等待（通过 Event 实现）。
