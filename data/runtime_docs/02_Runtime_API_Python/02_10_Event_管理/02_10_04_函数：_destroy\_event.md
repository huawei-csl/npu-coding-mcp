# 函数： destroy\_event

> **Section**: 2.10.4


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

销毁一个 Event ，支持在 Event 未完成前调用本接口销毁 Event 。此时，本接口不会阻塞 线程等 Event 完成， Event 相关资源会在 Event 完成时被自动释放。

- C 函数原型 aclError aclrtDestroyEvent(aclrtEvent event)

## 参数说明

## 返回值说明

## 约束说明

## 资源参考

接口调用示例，参见关于 Event 的同步等待、关于 Stream 间任务的同步等待（通过 Event 实现）。
