# aclrtSynchronizeEvent

> **Section**: 1.9.10


## 产品支持情况

## 功能说明

## 函数原型

aclError aclrtQueryEventWaitStatus(aclrtEvent event, aclrtEventWaitStatus *status)

| 参数名    | 输入 / 输 出   | 说明                                         |
|--------|------------|--------------------------------------------|
| event  | 输入         | 指定待查询的 Event 。类型定义请参见 aclrtEvent 。         |
| status | 输出         | Event 状态的指针。类型定义请参见 aclrtEventWaitStatus 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

阻塞当前线程运行直到 Event 捕获的所有任务都执行完成。具体见 aclrtRecordEvent 接 口参考 Event 捕获的细节。

aclError aclrtSynchronizeEvent(aclrtEvent event)

## 参数说明

## 返回值说明

## 接口调用示例

| 参数名   | 输入 / 输 出   | 说明                               |
|-------|------------|----------------------------------|
| event | 输入         | 需等待的 Event 。类型定义请参见 aclrtEvent 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见 Event 同步。
