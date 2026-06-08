# aclrtGetDevicesTopo

> **Section**: 1.6.24


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

须知：本接口不支持在 Atlas 200I/500 A2 推理产品的 Ascend RC 形态下调用。

获取两个 Device 之间的网络拓扑关系。

aclError aclrtGetDevicesTopo(uint32\_t deviceId, uint32\_t otherDeviceId, uint64\_t *value)

## 参数说明

## 返回值说明

| 参数名            | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| deviceId       | 输入         | 指定 Device 的 ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| otherDev iceId | 输入         | 指定 Device 的 ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量 后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| value          | 输出         | 两个 Device 之间互联的拓扑关系。 ● ACL_RT_DEVS_TOPOLOGY_HCCS ：通过 HCCS 连接。 HCCS 是 Huawei Cache Coherence System （华为缓存一 致性系统），用于 CPU/NPU 之间的高速互联。 ● ACL_RT_DEVS_TOPOLOGY_PIX ：通过同一个 PCIe Switch 连接。 ● ACL_RT_DEVS_TOPOLOGY_PHB ：通过 PCIe Host Bridge 连接。 ● ACL_RT_DEVS_TOPOLOGY_SYS ：通过 SMP （ Symmetric Multiprocessing ）连接， NUMA 节点之间 通过 SMP 互连。 ● ACL_RT_DEVS_TOPOLOGY_SIO ：片内连接方式，两个 DIE 之间通过该方式连接。 ● ACL_RT_DEVS_TOPOLOGY_HCCS_SW ：通过 HCCS Switch 连接。 ● ACL_RT_DEVS_TOPOLOGY_PIB ：预留值，暂不支持。 宏定义如下： #define ACL_RT_DEVS_TOPOLOGY_HCCS 0x01ULL #define ACL_RT_DEVS_TOPOLOGY_PIX 0x02ULL #define ACL_RT_DEVS_TOPOLOGY_PHB 0x08ULL #define ACL_RT_DEVS_TOPOLOGY_SYS 0x10ULL #define ACL_RT_DEVS_TOPOLOGY_SIO 0x20ULL #define ACL_RT_DEVS_TOPOLOGY_HCCS_SW 0x40ULL #define ACL_RT_DEVS_TOPOLOGY_PIB 0x04ULL |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
