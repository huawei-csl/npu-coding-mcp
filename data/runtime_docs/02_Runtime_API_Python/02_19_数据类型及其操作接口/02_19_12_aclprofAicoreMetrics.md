# aclprofAicoreMetrics

> **Section**: 2.19.12


| AI Core 性能指标采集项                        | 含义             |
|----------------------------------------|----------------|
| ACL_AICORE_ARITHMETI C_UTILIZATION = 0 | 各种计算类指标占比统计。   |
| ACL_AICORE_PIPE_UTILIZ ATION = 1       | 计算单元和搬运单元耗时占比。 |
| ACL_AICORE_MEMORY_B ANDWIDTH = 2       | 外部内存读写类指令占比。   |

| 参数名   | 说明                                                       |
|-------|----------------------------------------------------------|
| data  | int ，存放数据内存地址的指针地址。                                      |
| size  | int ，内存大小，单位 Byte 。如需使用空 Tensor ，在申请内存时， 内存大小最小为 1Byte 。 |

| AI Core 性能指标采集项                          | 含义                                                                                                  |
|------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ACL_AICORE_L0B_AND_ WIDTH = 3            | 内部内存读写类指令占比。                                                                                        |
| ACL_AICORE_RESOURCE_ CONFLICT_RATIO = 4  | 流水线队列类指令占比。                                                                                         |
| ACL_AICORE_MEMORY_U B = 5                | 内部内存读写指令占比。                                                                                         |
| ACL_AICORE_L2_CACHE = 6                  | 读写 cache 命中次数和缺失后重新分配次数，支持的产 品型号： Atlas A2 训练系列产品 /Atlas A2 推理系列产品 Atlas A3 训练系列产品 /Atlas A3 推理系列产品 |
| ACL_AICORE_L2_CACHE = 6                  | 读写 cache 命中次数和缺失后重新分配次数，支持的产 品型号： Atlas 200I/500 A2 推理产品                                            |
| ACL_AICORE_PIPE_EXECU TE_UTILIZATION = 7 | 计算单元和搬运单元耗时占比，支持的产品型号： Atlas 200I/500 A2 推理产品                                                       |
| ACL_AICORE_MEMORY_A CCESS = 8            | 算子在核上访存的带宽数据量，支持的产品型号： Atlas A2 训练系列产品 /Atlas A2 推理系列产品 Atlas A3 训练系列产品 /Atlas A3 推理系列产品            |
| ACL_AICORE_NONE = 0xFF                   | 表示不采集数据。                                                                                            |
