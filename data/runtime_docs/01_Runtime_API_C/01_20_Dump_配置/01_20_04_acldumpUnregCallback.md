# acldumpUnregCallback

> **Section**: 1.20.4


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

Dump 数据回调函数取消注册接口。 acldumpUnregCallback 需要和 acldumpRegCallback 配合使用，且必须在 acldumpRegCallback 调用后才有效。

aclmdlInitDump 接口、 acldumpRegCallback 接口（通过该接口注册的回调函数需 由用户自行实现，回调函数实现逻辑中包括获取 Dump 数据及数据长度）、 acldumpUnregCallback 接口、 aclmdlFinalizeDump 接口配合使用，用于通过回调 函数获取 Dump 数据。场景举例如下：

- 执行一个模型，通过回调获取 Dump 数据：
- aclInit 接口 --&gt; acldumpRegCallback 接口 --&gt; aclmdlInitDump 接口 --&gt; 模型加载 --&gt; 模型执行 --&gt; aclmdlFinalizeDump 接口 --&gt; acldumpUnregCallback 接口 --&gt; 模型 卸载 --&gt; aclFinalize 接口
- 执行两个不同的模型，通过回调获取 Dump 数据，该场景下，只要不调用 acldumpUnregCallback 接口取消注册回调函数，则可通过回调函数获取两个模 型的 Dump 数据：

aclInit 接口 --&gt; acldumpRegCallback 接口 --&gt; aclmdlInitDump 接口 --&gt; 模型 1 加 载 --&gt; 模型 1 执行 --&gt;--&gt; 模型 2 加载 --&gt; 模型 2 执行 --&gt; aclmdlFinalizeDump 接口 --&gt; 模 型卸载 --&gt; acldumpUnregCallback 接口 --&gt; aclFinalize 接口

void acldumpUnregCallback()

无

无
