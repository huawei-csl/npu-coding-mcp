# aclrtEventElapsedTime

> **Section**: 1.9.12


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

统计两个 Event 之间的耗时。

本接口需与其它关键接口配合使用，接口调用顺序：调用 aclrtCreateEvent / aclrtCreateEventWithFlag 接口创建 Event --&gt; 调用 aclrtRecordEvent 接口在同一个 Stream 中记录起始 Event 、结尾 Event --&gt; 调用 aclrtSynchronizeStream 接口阻塞应用 程序运行，直到指定 Stream 中的所有任务都完成 --&gt; 调用 aclrtEventElapsedTime 接口 统计两个 Event 之间的耗时

aclError aclrtEventElapsedTime(float *ms, aclrtEvent startEvent, aclrtEvent endEvent)

## 参数说明

## 返回值说明

## 接口调用示例

| 参数名         | 输入 / 输 出   | 说明                             |
|-------------|------------|--------------------------------|
| ms          | 输出         | 表示两个 Event 之间耗时的指针，单位为毫秒。      |
| startEven t | 输入         | 起始 Event 。类型定义请参见 aclrtEvent 。 |
| endEvent    | 输入         | 结尾 Event 。类型定义请参见 aclrtEvent 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见记录 Event 时间戳。
