# 函数： get\_devices\_topo

> **Section**: 2.7.23


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

## 须知

对于 Atlas 200I/500 A2 推理产品，本接口不支持在 Ascend RC 形态下调用。

获取两个 Device 之间的网络拓扑关系。

- C 函数原型

aclError aclrtGetDevicesTopo(uint32\_t deviceId, uint32\_t otherDeviceId, uint64\_t *value)

- python 函数

value, ret = acl.rt.get\_devices\_topo(device\_id, other\_device\_id)

| 参数名              | 说明                |
|------------------|-------------------|
| device_id        | int ， Device ID 。 |
| other_device_i d | int ， Device ID 。 |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其它值表示失败。 |

| 返回值   | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| value | int ，两个 Device 之间互联的拓扑关系。 #define ACL_RT_DEVS_TOPOLOGY_HCCS 0x01ULL # 通过 HCCS 连接， HCCS 是 Huawei Cache Coherence System （华为缓存一致性系统），用于 CPU/NPU 之间的高 速互联 #define ACL_RT_DEVS_TOPOLOGY_PIX 0x02ULL # 通过同一个 PCIe Switch 连接 #define ACL_RT_DEVS_TOPOLOGY_PIB 0x04ULL # 预留值 #define ACL_RT_DEVS_TOPOLOGY_PHB 0x08ULL # 通过 PCIe Host Bridge 连接 #define ACL_RT_DEVS_TOPOLOGY_SYS 0x10ULL # 通过 SMP （ Symmetric Multiprocessing ）连接， NUMA 节点之间通过 SMP 互连 #define ACL_RT_DEVS_TOPOLOGY_SIO 0x20ULL # 片内连接方式，两个 DIE 之 间通过该方式连接 #define ACL_RT_DEVS_TOPOLOGY_HCCS_SW 0x40ULL # 通过 HCCS Switch 连接 |
