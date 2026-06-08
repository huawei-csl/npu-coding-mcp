# acltdtTensorType

> **Section**: 1.28.135


```
enum acltdtTensorType { ACL_TENSOR_DATA_UNDEFINED = -1, ACL_TENSOR_DATA_TENSOR,           // 正常 tensor 数据标识 ACL_TENSOR_DATA_END_OF_SEQUENCE,  // end 数据标识 ACL_TENSOR_DATA_ABNORMAL,         // 异常数据标识 ACL_TENSOR_DATA_SLICE_TENSOR,     // tensor 分片场景下的 tensor 数据 ACL_TENSOR_DATA_END_TENSOR        // tensor 分片场景下标识最后一个 tensor };
```

废弃接口 / 返回码列表 同步 &amp; 异步 API 说明 pyACL 表达约定 util 模块 初始化 &amp; 去初始化 运行时配置 Device 管理 Context 管理 Stream 管理 Event 管理 Notify 管理 内存管理 执行控制 异常处理 Kernel 加载与执行 Profiling 数据采集 Dump 配置 其他接口 数据类型及其操作接口
