# aclrtEventGetTimestamp

> **Section**: 1.9.16


## 产品支持情况

## 功能说明

## 函数原型

| 参数名     | 输入 / 输 出   | 说明                              |
|---------|------------|---------------------------------|
| timeout | 输入         | 设置超时时间，单位为秒。 将该参数设置为 0 时，表示不超时。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取 Event 的执行结束时间点（表示从 AI 处理器系统启动以来的时间）。

本接口需与其它关键接口配合使用，接口调用顺序：调用 aclrtCreateEvent / aclrtCreateEventWithFlag 接口创建 Event --&gt; 调用 aclrtRecordEvent 接口在 Stream 中 记录 Event &gt; 调用 aclrtSynchronizeStream 接口阻塞应用程序运行，直到指定 Stream 中 的所有任务都完成 --&gt; 调用 aclrtEventGetTimestamp 接口获取 Event 的执行时间。

aclError aclrtEventGetTimestamp(aclrtEvent event, uint64\_t *timestamp)

## 参数说明

## 返回值说明

| 参数名        | 输入 / 输 出   | 说明                              |
|------------|------------|---------------------------------|
| event      | 输入         | 查询的 Event 。类型定义请参见 aclrtEvent 。 |
| timesta mp | 输出         | Event 执行结束的时间点，单位为微秒。           |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
