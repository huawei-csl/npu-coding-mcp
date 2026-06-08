# aclGetRecentErrMsg

> **Section**: 1.15.1


## 产品支持情况

## 功能说明

| 参数名         | 输入 / 输 出   | 说明                                                                                                  |
|-------------|------------|-----------------------------------------------------------------------------------------------------|
| taskStrea m | 输入         | 目标任务所在的 Stream 。类型定义请参见 aclrtStream 。 此处只支持与模型绑定过的 Stream ，绑定模型与 Stream 需 调用 aclmdlRIBindStream 接口。 |
| taskId      | 输入         | 目标任务 ID 。 可调用 aclrtGetThreadLastTaskId 接口获取任务 ID 。                                                  |
| info        | 输入         | 配置信息。类型定义请参见 aclrtTaskUpdateInfo 。                                                                  |
| execStre am | 输入         | 执行刷新任务的 Stream 。类型定义请参见 aclrtStream 。                                                               |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取并清空与本接口在同一个进程或线程中的其它 acl 接口调用失败时的错误描述信 息。

## 函数原型

参数说明

## 返回值说明

## 接口调用示例

接口调用示例，参见获取 Runtime 错误码。
