# acltdtStopChannel

> **Section**: 1.19.1.5


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | ☓      |
| Atlas 训练系列产品 | √      |

调用 acltdtSendTensor 接口发送数据时或调用 acltdtReceiveTensor 接口接收数据时，用 户线程可能在没有数据时会卡住，此时如果需要退出的话，需要先将线程唤醒，该接 口就是用来唤醒被卡住阻塞的线程用的。需要用户在发送、接收线程之外的一个线程 里调用这个函数，来唤醒处于阻塞状态的发送 / 接收线程。

aclError acltdtStopChannel(acltdtChannelHandle *handle)

| 参数名    | 输入 / 输 出   | 说明                                                                                                  |
|--------|------------|-----------------------------------------------------------------------------------------------------|
| handle | 输入         | 指定通道。 需提前调用 acltdtCreateChannel 接口或 acltdtCreateChannelWithCapacity 接口创建 acltdtChannelHandle 类型的数据。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
