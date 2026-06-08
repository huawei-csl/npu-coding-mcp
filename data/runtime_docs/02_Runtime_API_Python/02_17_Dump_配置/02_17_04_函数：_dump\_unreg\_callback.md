# 函数： dump\_unreg\_callback

> **Section**: 2.17.4


## 产品支持情况

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

Dump 数据回调函数取消注册接口。

2.17.1 函数： init\_dump 接口、 2.17.3 函数： dump\_reg\_callback 接口（通过该接口 注册的回调函数需由用户自行实现，回调函数实现逻辑中包括获取 Dump 数据及数据长 度）、 2.17.4 函数： dump\_unreg\_callback 接口、 2.17.5 函数：fi nalize\_dump 接口 配合使用，用于通过回调函数获取 Dump 数据。场景举例如下：

- 执行一个模型，通过回调获取 Dump 数据： 2.5.1 函数： init 接口 --&gt; 2.17.3 函数： dump\_reg\_callback 接口 --&gt; 2.17.1 函数： init\_dump 接口 --&gt; 模型加载 --&gt; 模型执行 --&gt; 2.17.5 函数：fi nalize\_dump 接口 --&gt; 2.17.4 函数： dump\_unreg\_callback 接口 --&gt; 模型卸载 --&gt; 2.5.2 函数：fi nalize 接口
- 执行两个不同的模型，通过回调获取 Dump 数据，该场景下，只要不调用 2.17.4 函数： dump\_unreg\_callback 接口取消注册回调函数，则可通过回调函数获取两 个模型的 dump 数据：

2.5.1 函数： init 接口 --&gt; 2.17.3 函数： dump\_reg\_callback 接口 --&gt; 2.17.1 函数： init\_dump 接口 --&gt; 模型 1 加载 --&gt; 模型 1 执行 --&gt;--&gt; 模型 2 加载 --&gt; 模型 2 执行 --&gt; 2.17.5 函数：fi nalize\_dump 接口 --&gt; 模型卸载 --&gt; 2.17.4 函数： dump\_unreg\_callback 接口 --&gt; 2.5.2 函数：fi nalize 接口

- C 函数原型

void acldumpUnregCallback()

- python 函数

acl.mdl.dump\_unreg\_callback()

无

无

## 约束说明

acl.mdl.dump\_unreg\_callback 需要和 acl.mdl.dump\_reg\_callback 配合使用，且必须在 acl.mdl.dump\_reg\_callback 调用后才有效。
