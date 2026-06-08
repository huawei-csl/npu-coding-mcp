# aclrtKernelType

> **Section**: 1.28.65


```
typedef enum { Vector Core
```

```
ACL_KERNEL_TYPE_AICORE = 0,    // AI Core ACL_KERNEL_TYPE_CUBE = 1,      // Cube Core ACL_KERNEL_TYPE_VECTOR = 2,    // Vector Core ACL_KERNEL_TYPE_MIX = 3,       // 会同时启动 AI Core 上的 Cube Core 和 ACL_KERNEL_TYPE_AICPU = 100,   // AI CPU } aclrtKernelType;
```

不同产品上的 AI 数据处理核心单元不同，关于 Core 的定义及详细说明，请参见 1.28.45 aclrtDevAttr 。
