# aclrtMemLocationType

> **Section**: 1.28.87


typedef enum aclrtMemLocationType {

```
ACL_MEM_LOCATION_TYPE_HOST = 0,      // 通过 acl 接口（例如 aclrtMallocHost ）申请的 Host 内存 ACL_MEM_LOCATION_TYPE_DEVICE,        // 通过 acl 接口（例如 aclrtMalloc ）申请的 Device 内存 ACL_MEM_LOCATION_TYPE_UNREGISTERED,  // 未通过 acl 接口申请的内存 ACL_MEM_LOCATION_TYPE_HOST_NUMA =4,  // 通过 aclrtMallocPhysical 接口按照 NUMA ID 申请 Host 内存 } aclrtMemLocationType;
```
