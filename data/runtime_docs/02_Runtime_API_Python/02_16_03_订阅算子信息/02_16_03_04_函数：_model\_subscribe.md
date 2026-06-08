# 函数： model\_subscribe

> **Section**: 2.16.3.4


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

网络场景下，订阅算子的基本信息，包括算子名称、算子类型、算子执行耗时等。

- C 函数原型

aclError aclprofModelSubscribe(uint32\_t modelId, const aclprofSubscribeConfig *profSubscribeConfig)

- python 函数

ret = acl.prof.model\_subscribe(model\_id, subscribe\_config)

| 参数名               | 说明                                                                                                                                                                   |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| model_id          | int ，待订阅的网络模型的 ID 。调用 acl.mdl.load_from_file 接口 / acl.mdl.load_from_mem 接口 /acl.mdl.load_from_file_with_mem 接口 /acl.mdl.load_from_mem_with_mem 接口加载模型成功后， 会返回模型 ID 。 |
| subscribe_conf ig | int ，待订阅的配置信息。调用 acl.prof.create_subscribe_config 接口创建配置数据。                                                                                                          |

| 返回值   | 说明                                  |
|-------|-------------------------------------|
| ret   | int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。 |

## 约束说明

需要与 acl.prof.model\_unsubscribe 接口配对使用。
