# 函数： set\_stamp\_trace\_message

> **Section**: 2.16.2.3


## 产品支持情况

## 功能说明

## 函数原型

| 参数名   | 说明                                             |
|-------|------------------------------------------------|
| stamp | int ，指针地址。 ● 返回 0 表示失败。 ● 返回 void 类型的指针地址表示成功。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

为 msproftx 事件标记携带字符串描述，在 Profiling 解析并导出结果中 msprof\_tx summary 数据展示。

- C 函数原型 aclError aclprofSetStampTraceMessage(void *stamp, const char *msg, uint32\_t msgLen)
- python 函数

ret = acl.prof.set\_stamp\_trace\_message(stamp, msg, msg\_len)

## 参数说明

## 返回值说明

## 约束说明

在 2.16.2.2 函数： create\_stamp 接口和 2.16.2.10 函数： destroy\_stamp 接口之间调 用。

2.16.2.4

## 函数： mark

## 产品支持情况

## 功能说明

| 参数名     | 说明                                                                       |
|---------|--------------------------------------------------------------------------|
| stamp   | int ， Stamp 指针地址，指代 msproftx 事件标记。指定 2.16.2.2 函 数： create_stamp 接口的指针地址。 |
| msg     | int ，字符串内容地址。                                                            |
| msg_len | int ，字符串长度。                                                              |

| 返回值   | 说明                                  |
|-------|-------------------------------------|
| ret   | int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

msproftx 标记瞬时事件。

调用此接口后， Profiling 自动在 Stamp 中加上当前时间戳，将 Event type 设置为 Mark ，表示开始一次 msproftx 采集。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

在函数： create\_stamp 接口和函数： destroy\_stamp 接口之间调用。
