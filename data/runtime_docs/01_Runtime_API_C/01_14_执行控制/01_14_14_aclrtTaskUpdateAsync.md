# aclrtTaskUpdateAsync

> **Section**: 1.14.14


## 产品支持情况

## 功能说明

## 函数原型

| 参数名      | 输入 / 输 出   | 说明                                         |
|----------|------------|--------------------------------------------|
| taskInfo | 输入         | 随机数生成任务信息。类型定义请参见 aclrtRandomNumTaskInfo 。 |
| stream   | 输入         | 执行随机数生成任务的 Stream 。类型定义请参见 aclrtStream 。   |
| reserve  | 输入         | 预留参数。当前固定传 NULL 。                          |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

刷新目标任务的信息。异步接口。

aclError aclrtTaskUpdateAsync(aclrtStream taskStream, uint32\_t taskId, aclrtTaskUpdateInfo *info, aclrtStream execStream)

## 参数说明

## 返回值说明

## 约束说明

Atlas 350 加速卡产品不支持更新 ACL\_RT\_UPDATE\_RANDOM\_TASK( 随机数生成任 务 ) 。
