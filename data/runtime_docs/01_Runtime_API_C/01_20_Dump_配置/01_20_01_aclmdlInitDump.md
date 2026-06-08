# aclmdlInitDump

> **Section**: 1.20.1


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

Dump 初始化。

本接口需与其它接口配合使用实现以下功能：

- Dump 数据落盘到文件

aclmdlInitDump 接口、 aclmdlSetDump 接口、 aclmdlFinalizeDump 接口配合 使用，用于将 Dump 数据记录到文件中。一个进程内，可以根据需求多次调用这 些接口，基于不同的 Dump 配置信息，获取 Dump 数据。场景举例如下：

- -执行两个不同的模型，需要设置不同的 Dump 配置信息，接口调用顺序： aclInit 接口 --&gt; aclmdlInitDump 接口 --&gt; aclmdlSetDump 接口 --&gt; 模型 1 加

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

## 参考资源

载 --&gt; 模型 1 执行 --&gt; aclmdlFinalizeDump 接口 --&gt; 模型 1 卸载 --&gt; aclmdlInitDump 接口 --&gt; aclmdlSetDump 接口 --&gt; 模型 2 加载 --&gt; 模型 2 执 行 --&gt; aclmdlFinalizeDump 接口 --&gt; 模型 2 卸载 --&gt; 执行其它任务 --&gt; aclFinalize 接口

- -同一个模型执行两次，第一次需要 Dump ，第二次无需 Dump ，接口调用顺 序： aclInit 接口 --&gt; aclmdlInitDump 接口 --&gt; aclmdlSetDump 接口 --&gt; 模型加 载 --&gt; 模型执行 --&gt; aclmdlFinalizeDump 接口 --&gt; 模型卸载 --&gt; 模型加载 --&gt; 模型 执行 --&gt; 执行其它任务 --&gt; aclFinalize 接口

● Dump 数据不落盘到文件，直接通过回调函数获取 aclmdlInitDump 接口、 acldumpRegCallback 接口（通过该接口注册的回调函 数需由用户自行实现，回调函数实现逻辑中包括获取 Dump 数据及数据长度）、 acldumpUnregCallback 接口、 aclmdlFinalizeDump 接口配合使用，用于通过 回调函数获取 Dump 数据。场景举例如下：

- -执行一个模型，通过回调获取 Dump 数据： aclInit 接口 --&gt; acldumpRegCallback 接口 --&gt; aclmdlInitDump 接口 --&gt; 模型 加载 --&gt; 模型执行 --&gt; aclmdlFinalizeDump 接口 --&gt; acldumpUnregCallback 接口 --&gt; 模型卸载 --&gt; aclFinalize 接口
- -执行两个不同的模型，通过回调获取 Dump 数据，该场景下，只要不调用 acldumpUnregCallback 接口取消注册回调函数，则可通过回调函数获取两 个模型的 Dump 数据： aclInit 接口 --&gt; acldumpRegCallback 接口 --&gt; aclmdlInitDump 接口 --&gt; 模型 1 加载 --&gt; 模型 1 执行 --&gt;--&gt; 模型 2 加载 --&gt; 模型 2 执行 --&gt; aclmdlFinalizeDump 接 口 --&gt; 模型卸载 --&gt; acldumpUnregCallback 接口 --&gt; aclFinalize 接口

aclError aclmdlInitDump()

无

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 对于模型 Dump 配置、单算子 Dump 配置、溢出算子 Dump 配置，如果已经通过 aclInit 接口配置了 dump 信息，则调用 aclmdlInitDump 接口时会返回失败。
- 必须在调用 aclInit 接口之后、模型加载接口之前调用 aclmdlInitDump 接口。

当前还提供了 aclInit 接口，在初始化阶段，通过 *.json 文件传入 Dump 配置信息，运行 应用后获取 Dump 数据的方式。该种方式，一个进程内，只能调用一次 aclInit 接口， 如果要修改 Dump 配置信息，需修改 *.json 文件中的配置。
