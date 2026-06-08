# aclrtCmoType

> **Section**: 1.28.36


typedef enum aclrtCmoType {

```
ACL_RT_CMO_TYPE_PREFETCH = 0,     // 内存预取，从内存预取到 Cache ACL_RT_CMO_TYPE_WRITEBACK,        // 把 Cache 中的数据刷新到内存中，并在 Cache 中保留副本 ACL_RT_CMO_TYPE_INVALID,          // 丢弃 Cache 中的数据 ACL_RT_CMO_TYPE_FLUSH,            // 把 Cache 中的数据刷新到内存中，不保留 Cache 中的副本 } aclrtCmoType;
```
