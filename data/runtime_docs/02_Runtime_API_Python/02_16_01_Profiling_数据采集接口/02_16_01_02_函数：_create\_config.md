# 函数： create\_config

> **Section**: 2.16.1.2


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

创建 aclprofConfig 类型的数据，表示创建 Profiling 配置数据。

aclProfConfig 类型数据可以只创建一次、多处使用，用户需要保证数据的一致性和准 确性。

如需销毁 aclprofConfig 类型的数据，请参见 2.16.1.4 函数： destroy\_config 。

## ● C 函数原型

aclprofConfig *aclprofCreateConfig(uint32\_t *deviceIdlist, uint32\_t deviceNums, aclprofAicoreMetrics aicoreMetrics, aclprofAicoreEvents *aicoreEvents, uint64\_t dataTypeConfig)

## ● python 函数

prof\_config = acl.prof.create\_config(device\_list, aicore\_metrics, aicore\_events, data\_type\_config)

| 参数名            | 说明                                         |
|----------------|--------------------------------------------|
| device_list    | list ， Device ID 列表。须根据实际环境的 Device ID 配置。 |
| aicore_metrics | int ，表示 aclprofAicoreMetrics 。             |
| aicore_events  | int ，表示 AI Core 事件，目前配置为 0 。               |

## 返回值说明

## 约束说明

| 参数名               | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data_type_conf ig | int ，用户选择如下多个 2.19.14 aclproftype 的值进行逻辑或（例 如： ACL_PROF_ACL_API&#124;ACL_PROF_AICORE_METRICS ），作为 data_type_config 参数值。每个值表示某一类性能数据，详细说明 如下： ● ACL_PROF_ACL_API ：表示采集接口的性能数据，包括 Host 与 Device 之间的同步异步内存复制时延等。 ● ACL_PROF_TASK_TIME ：采集算子下发耗时、算子执行耗时数 据以及算子基本信息数据，提供更全面的性能分析数据。 ● ACL_PROF_TASK_TIME_L0 ：采集算子下发耗时、算子执行耗 时数据。与 ACL_PROF_TASK_TIME 相比，由于不采集算子基本 信息数据，采集时性能开销较小，可更精准统计相关耗时数 据。 ● ACL_PROF_AICORE_METRICS ：表示采集 AI Core 性能指标数 据，逻辑或时必须包括该宏， aicore_metrics 入参处配置的性能 指标采集项才有效。 ● ACL_PROF_TASK_MEMORY ：控制 CANN 算子的内存占用情况 采集开关。仅采集 GE 组件算子。 ● ACL_PROF_AICPU ：表示采集 AI CPU 任务的开始、结束数据。 ● ACL_PROF_L2CACHE ：表示采集 L2 Cache 数据。 ● ACL_PROF_HCCL_TRACE ：控制通信数据采集开关。 ● ACL_PROF_MSPROFTX ：获取用户和上层框架程序输出的性能 数据。需要先在应用程序脚本中添加如下其中一套接口： - mstx API （ MindStudio Tools Extension API ）接口详细操 作请参见《性能调优工具》中的'附录 > mstx API 使用示 例'。 - 2.16.2 msproftx 扩展接口。 ● ACL_PROF_TRAINING_TRACE ：控制迭代轨迹数据采集开关。 ● ACL_PROF_RUNTIME_API ：控制 runtime api 性能数据采集开 关。 |

| 返回值         | 说明                                                              |
|-------------|-----------------------------------------------------------------|
| prof_config | int 。 ● 返回非 0 值表示成功，返回值为返回 aclprofConfig 类型的指针 地址。 ● 返回 0 表示失败。 |

- 使用 acl.prof.destroy\_config 接口销毁 aclprofConfig 类型的数据，如不销毁会导 致内存未被释放。

## 功能说明

## 函数原型

- 与 acl.prof.destroy\_config 接口配对使用，先调用 acl.prof.create\_config 接口再调 用 acl.prof.destroy\_config 接口。
