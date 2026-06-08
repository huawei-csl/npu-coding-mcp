# aclmdlRIBuildBegin

> **Section**: 1.17.11


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

开始构建一个模型运行实例。

在 aclmdlRIBuildBegin 接口之后，先调用 aclmdlRIBindStream 接口将模型运行实例 与 Stream 绑定，接着在指定的 Stream 上下发任务，所有任务下发完成后，调用 aclmdlRIEndTask 接口在 Stream 上标记任务下发结束，随后调用 aclmdlRIBuildEnd 接口结束模型构建。此时，所有在指定 Stream 上下发的任务不会立即执行，只有在调 用 aclmdlRIExecute 或 aclmdlRIExecuteAsync 接口执行模型推理时，这些任务才会被 真正执行。

所有任务执行完毕后，如果不再使用模型运行实例，可调用 aclmdlRIUnbindStream 接口解除模型运行实例与 Stream 的绑定关系。可调用 aclmdlRIDestroy 接口及时销毁 该资源。

aclError aclmdlRIBuildBegin(aclmdlRI *modelRI, uint32\_t flag)

## 参数说明

## 返回值说明

| 参数名     | 输入 / 输出   | 说明                                       |
|---------|-----------|------------------------------------------|
| modelRI | 输入        | 模型运行实例，该模型用于暂存所编译的任务。类型定义 请参见 aclmdlRI 。 |
| flag    | 输入        | 预留参数。当前固定配置为 0 。                         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
