# aclprofSetStampTraceMessage

> **Section**: 1.21.2.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

为 msproftx 事件标记携带字符串描述，在 Profiling 解析并导出结果中 msprof\_tx summary 数据展示。

aclError aclprofSetStampTraceMessage(void *stamp, const char *msg, uint32\_t msgLen)

| 参数名    | 输入 / 输 出   | 说明                                                      |
|--------|------------|---------------------------------------------------------|
| stamp  | 输入         | Stamp 指针，指代 msproftx 事件标记。 指定 aclprofCreateStamp 接口的指针。 |
| msg    | 输入         | Stamp 信息字符串指针。                                          |
| msgLen | 输入         | 字符串长度。                                                  |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

在 1.21.2.2 aclprofCreateStamp 接口和 1.21.2.10 aclprofDestroyStamp 接口之间调 用。
