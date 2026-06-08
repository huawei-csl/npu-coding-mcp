# aclrtCmoWaitBarrier

> **Section**: 1.13.52


## 产品支持情况

## 功能说明

函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

等待具有指定 barrierId 的 Invalid 内存操作任务执行完成。异步接口。

aclError aclrtCmoWaitBarrier(aclrtBarrierTaskInfo *taskInfo, aclrtStream stream, uint32\_t flag)

| 参数名      | 输入 / 输 出   | 说明                                                                                                 |
|----------|------------|----------------------------------------------------------------------------------------------------|
| taskInfo | 输入         | Cache 内存操作的任务信息。类型定义请参见 aclrtBarrierTaskInfo 。 任务信息中的 cmoType 当前仅支持 ACL_RT_CMO_TYPE_INVALID 。      |
| stream   | 输入         | 执行等待任务的 Stream 。类型定义请参见 aclrtStream 。 此处只支持与模型绑定过的 Stream ，绑定模型与 Stream 需调用 aclmdlRIBindStream 接口。 |
| flag     | 输入         | 预留参数。当前固定配置为 0 。                                                                                   |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
