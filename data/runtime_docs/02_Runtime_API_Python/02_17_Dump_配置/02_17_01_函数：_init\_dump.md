# 函数： init\_dump

> **Section**: 2.17.1


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

Dump 初始化。

- C 函数原型 aclError aclmdlInitDump()
- python 函数
- ret = acl.mdl.init\_dump()

无

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- acl.mdl.init\_dump 接口需要与 acl.mdl.set\_dump 接口、 acl.mdl.finalize\_dump 接口配合使用，用于将 Dump 数据记录到文件中。一个进程内，可以根据需求多 次调用这些接口，基于不同的 Dump 配置信息，获取 Dump 数据。

## 资源参考

还提供了 acl.init 接口，在初始化阶段，通过 *.json 文件传入 Dump 配置信息，运行应用 后获取 Dump 数据的方式。该种方式，一个进程内，只能调用一次 acl.init 接口，如果 要修改 Dump 配置信息，需修改 *.json 文件中的配置。
