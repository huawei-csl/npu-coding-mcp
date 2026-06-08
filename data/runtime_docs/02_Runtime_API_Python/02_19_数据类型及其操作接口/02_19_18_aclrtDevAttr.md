# aclrtDevAttr

> **Section**: 2.19.18


| 数据格式                                           | 说明                                                                                                                                  |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ACL_DEV_ATTR_AICPU_CORE_N UM = 1               | AI CPU 数量。                                                                                                                          |
| ACL_DEV_ATTR_AICORE_CORE_ NUM = 101            | AI Core 数量。                                                                                                                         |
| ACL_DEV_ATTR_VECTOR_CORE_ NUM = 201            | Vector Core 数量。                                                                                                                     |
| ACL_DEV_ATTR_WARP_SIZE = 202                   | 一个 Warp 里的线程数，在 SIMT （单指令多线 程， Single Instruction Multiple Thread ）编程 模型中， Warp 是指执行相同指令的线程集合。 仅 Atlas 350 加速卡支持该类型其它产品型号当 前不支持该类型。 |
| ACL_DEV_ATTR_MAX_THREAD_ PER_VECTOR_CORE = 203 | 每个 VECTOR_CORE 上可同时驻留的最大线程 数。 仅 Atlas 350 加速卡支持该类型其它产品型号当 前不支持该类型。                                                                  |
| ACL_DEV_ATTR_LOCAL_MEM_P ER_VECTOR_CORE = 204  | 每个 VECTOR_CORE 上可以使用的最大本地内 存，单位 Byte 。 仅 Atlas 350 加速卡支持该类型其它产品型号当 前不支持该类型。                                                         |
| ACL_DEV_ATTR_TOTAL_GLOBAL _MEM_SIZE = 301      | Device 上的可用总内存，单位 Byte 。                                                                                                            |
| ACL_DEV_ATTR_L2_CACHE_SIZE = 302               | L2 Cache （二级缓存）大小，单位 Byte 。                                                                                                         |
| ACL_DEV_ATTR_SMP_ID = 401                      | SMP （ Symmetric Multiprocessing ） ID ，用于 标识设备是否运行在同一操作系统上。                                                                          |
| ACL_DEV_ATTR_PHY_CHIP_ID = 402                 | 芯片物理 ID 。                                                                                                                           |
| ACL_DEV_ATTR_SUPER_POD_DE VICE_ID = 403        | SuperPOD Device ID 表示超节点产品中的 Device 标识。                                                                                             |
| ACL_DEV_ATTR_SUPER_POD_SE RVER_ID = 404        | SuperPOD Server ID 表示超节点产品中的服务 器标识。                                                                                                 |
| ACL_DEV_ATTR_SUPER_POD_ID = 405                | SuperPOD ID 表示集群中的超节点 ID 。                                                                                                          |

| 数据格式                                  | 说明                                                                                                                     |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ACL_DEV_ATTR_CUST_OP_PRIVI LEGE = 406 | 表示查询自定义算是否可以执行更多的系统调 用权限。 取值如下： ● 0 ：自定义算子执行系统调用权限受控（例如 不能执行 Write 操作）。 ● 1 ：自定义算子可以执行更多的系统调用权 限。 Atlas 350 加速卡不支持该选项。 |
| ACL_DEV_ATTR_MAINBOARD_I D = 407      | 主板 ID 。                                                                                                                |
| ACL_DEV_ATTR_IS_VIRTUAL = 501         | 是否为 昇 腾虚拟化实例。 ● 0 ：不是 昇 腾虚拟化实例，是物理机。 ● 1 ：是 昇 腾虚拟化实例，可能是虚拟机或容 器。                                                       |
