# aclrtIpcOpenEventHandle

> **Section**: 1.9.20


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

在本进程中获取 handle 的信息，并返回本进程可以使用的 Event 指针。

本接口需与其它接口配合使用，以便实现不同进程间的任务同步，请参见 1.9.19 aclrtIpcGetEventHandle 接口处的说明。

aclError aclrtIpcOpenEventHandle(aclrtIpcEventHandle handle, aclrtEvent *event)

| 参数名    | 输入 / 输出   | 说明                                                                                            |
|--------|-----------|-----------------------------------------------------------------------------------------------|
| handle | 输入        | Event 句柄。类型定义请参见 aclrtIpcEventHandle 。 必须先调用 aclrtIpcGetEventHandle 接口获取指定 Event 的句柄，再作为入参传入。 |
| event  | 输出        | Event 指针。类型定义请参见 aclrtEvent 。                                                                 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见进程间通信。
