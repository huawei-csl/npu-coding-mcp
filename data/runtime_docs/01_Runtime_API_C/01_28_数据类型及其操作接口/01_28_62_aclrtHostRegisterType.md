# aclrtHostRegisterType

> **Section**: 1.28.62


```
typedef enum { ACL_HOST_REGISTER_MAPPED = 0, ACL_HOST_REGISTER_IOMEMORY = 0x04,
```

ACL\_HOST\_REGISTER\_READONLY = 0x08 }aclrtHostRegisterType;

| 枚举项                         | 说明                                                                                                                          |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ACL_HOST_REGISTER_ MAPPED   | Host 内存映射注册为 Device 可访问，包括读写。                                                                                               |
| ACL_HOST_REGISTER_I OMEMORY | 将 Host 上第三方 PCIe 设备的 IO space( 寄存器、缓存 ) 映 射注册为 Device 可访问，包括读写。 对于 Atlas A3 训练系列产品 /Atlas A3 推理系列产品，仅 支持 X86 架构，不支持 ARM 架构。 |
| ACL_HOST_REGISTER_R EADONLY | Host 内存映射注册为 Device 只读。预留选项，当前不支 持。                                                                                         |
