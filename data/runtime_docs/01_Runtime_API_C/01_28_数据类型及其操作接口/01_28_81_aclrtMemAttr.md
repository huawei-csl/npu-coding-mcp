# aclrtMemAttr

> **Section**: 1.28.81


```
typedef enum aclrtMemAttr { ACL_DDR_MEM,             // 大页内存 + 普通内存 ACL_HBM_MEM,             // 大页内存 + 普通内存 ACL_DDR_MEM_HUGE,        // 大页内存 ACL_DDR_MEM_NORMAL,      // 普通内存 ACL_HBM_MEM_HUGE,        // 大页内存，内存申请粒度为 2M ，不足 2M 的倍数，向上 2M 对齐 ACL_HBM_MEM_NORMAL,      // 普通内存 ACL_DDR_MEM_P2P_HUGE,    // 用于 Device 间数据复制的大页内存 ACL_DDR_MEM_P2P_NORMAL,  // 用于 Device 间数据复制的普通内存 ACL_HBM_MEM_P2P_HUGE,    // 用于 Device 间数据复制的大页内存，内存申请粒度为 2M ，不足 2M 的倍数， 向上 2M 对齐 ACL_HBM_MEM_P2P_NORMAL,  // 用于 Device 间数据复制的普通内存 ACL_HBM_MEM_HUGE1G,      // 大页内存，内存申请粒度为 1G ，不足 1G 的倍数，向上 1G 对齐 ACL_HBM_MEM_P2P_HUGE1G   // 用于 Device 间数据复制的大页内存，内存申请粒度为 1G ，不足 1G 的倍 数，向上 1G 对齐 /* 以上选项兼容旧版本，需由用户根据硬件内存（ DDR 、 HBM ）选择相应的内存属性选项 */ /* 以下选项由接口内部根据底层硬件内存自动选择 DDR 或 HBM ，用户无需关注硬件细节，建议使用以下选项 */ ACL_MEM_NORMAL,          // 普通内存
```

| ACL_MEM_HUGE,                               | // 大页内存，内存申请粒度为 2M ，不足 2M 的倍数，向上 2M 对齐          |
|---------------------------------------------|-------------------------------------------------|
| ACL_MEM_HUGE1G,                             | // 大页内存，内存申请粒度为 1G ，不足 1G 的倍数，向上 1G 对齐          |
| ACL_MEM_P2P_NORMAL,                         | // 用于 Device 间数据复制的普通内存                         |
| ACL_MEM_P2P_HUGE, 上 2M 对齐                   | // 用于 Device 间数据复制的大页内存，内存申请粒度为 2M ，不足 2M 的倍数，向 |
| ACL_MEM_P2P_HUGE1G, 上 1G 对齐 } aclrtMemAttr; | // 用于 Device 间数据复制的大页内存，内存申请粒度为 1G ，不足 1G 的倍数，向 |

对于申请大页内存的场景，当内存申请粒度为 2M 时，如果要申请 1G 大小的大页内存， 会占用 1024/2=512 个页表，当内存申请粒度为 1G 时， 1G 大页内存只占用 1 个页表，能 有效降低页表数量，有效扩大 TLB （ Translation Lookaside Buffer ）缓存的地址范围， 从而提升离散访问的性能。 TLB 是 AI 处理器中用于高速缓存的硬件模块，用于存储最近 使用的虚拟地址到物理地址的映射。

HUGE1G 相关选项仅 Atlas A3 训练系列产品 /Atlas A3 推理系列产品、 Atlas A2 训练系 列产品 /Atlas A2 推理系列产品支持。

其它型号当前不支持 HUGE1G 相关选项。
