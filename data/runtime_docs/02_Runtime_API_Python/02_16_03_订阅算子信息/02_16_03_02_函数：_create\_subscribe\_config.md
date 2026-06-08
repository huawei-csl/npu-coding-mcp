# 函数： create\_subscribe\_config

> **Section**: 2.16.3.2


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

创建 aclprofSubscribeConfig 类型的数据，表示创建订阅配置信息。 aclprofSubscribeConfig 类型的数据，请参见

如需销毁 acl.prof.destroy\_subscribe\_config 。

- C 函数原型 aclprofSubscribeConfig *aclprofCreateSubscribeConfig(int8\_t timeInfoSwitch, aclprofAicoreMetrics aicoreMetrics, void *fd)
- python 函数
- subscribe\_config = acl.prof.create\_subscribe\_config(time\_info\_switch, aicore\_metrics, fd)

## 参数说明

## 返回值说明

## 约束说明

| 参数名               | 说明                                                                                                 |
|-------------------|----------------------------------------------------------------------------------------------------|
| time_info_swit ch | int ，是否采集网络模型中算子的性能数据： ● 1 ：采集 ● 0 ：不采集                                                            |
| aicore_metrics    | int ，表示 AI Core 性能指标采集项，参考 aclprofAicoreMetrics 。 说明 订阅接口目前仅提供算子耗时统计的功能，暂时不支持 AicoreMetrics 采集 功能。 |
| fd                | int ，用户创建管道的写文件描述符。 用户在调用 acl.prof.model_unsubscribe 接口后，系统内部会在 数据发送结束后，关闭该模型的管道写文件描述符。            |

| 返回值               | 说明                                                                 |
|-------------------|--------------------------------------------------------------------|
| subscribe_conf ig | int 。 ● 返回非 0 值表示成功，返回 aclprofSubscribeConfig 的地址对 象。 ● 返回 0 表示失败。 |

- 使用 acl.prof.destroy\_subscribe\_config 接口销毁 aclprofSubscribeConfig 类型的 数据，如不销毁会导致内存未被释放。
- 与 acl.prof.destroy\_subscribe\_config 接口配对使用，先调用 acl.prof.create\_subscribe\_config 接口再调用 acl.prof.destroy\_subscribe\_config 接口。
