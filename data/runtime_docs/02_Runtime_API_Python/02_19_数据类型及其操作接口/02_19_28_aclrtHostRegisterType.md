# aclrtHostRegisterType

> **Section**: 2.19.28


| 数据格式                            | 说明                                                                                                                        |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ACL_HOST_REGISTER_ MAPPED = 0   | Host 内存映射注册为 Device 可访问，包括读写。                                                                                             |
| ACL_HOST_REGISTER_I OMEMORY = 4 | 将 Host 上第三方 PCIe 设备的 IO space （寄存器、缓存） 映射注册为 Device 可访问，包括读写。 对于 Atlas A3 训练系列产品 /Atlas A3 推理系列产品，仅 支持 X86 架构，不支持 ARM 架构。 |
| ACL_HOST_REGISTER_R EADONLY = 8 | Host 内存映射注册为 Device 只读。预留选项，当前不支 持。                                                                                       |
