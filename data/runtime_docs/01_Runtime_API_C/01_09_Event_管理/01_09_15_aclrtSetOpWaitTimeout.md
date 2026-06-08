# aclrtSetOpWaitTimeout

> **Section**: 1.9.15


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | √      |

本接口用于设置等待 Event 完成的超时时间。

不调用本接口，则默认不超时；一个进程内多次调用本接口，则以最后一次设置的时 间为准。

aclError aclrtSetOpWaitTimeout(uint32\_t timeout)

## 参数说明

## 返回值说明

## 约束说明

一个进程内，调用 aclInit 接口初始化后，若再调用 aclrtSetOpWaitTimeout 接口设置 超时时间，那么本进程内后续调用 aclrtStreamWaitEvent 接口下发的任务支持在所设 置的超时时间内等待，若等待的时间超过所设置的超时时间，则在调用同步等待接口 （例如， aclrtSynchronizeStream ）后，会返回报错。
