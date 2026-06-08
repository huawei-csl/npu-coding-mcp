# aclrtMemLocationType

> **Section**: 2.19.40


| 数据格式                                    | 说明                                              |
|-----------------------------------------|-------------------------------------------------|
| ACL_MEM_LOCATION_TYPE_H OST = 0         | 通过 acl 接口（例如 aclrtMallocHost ）申请的 Host 内存。      |
| ACL_MEM_LOCATION_TYPE_D EVICE = 1       | 通过 acl 接口（例如 aclrtMalloc ）申请的 Device 内 存。       |
| ACL_MEM_LOCATION_TYPE_U NREGISTERED = 2 | 未通过 acl 接口申请的内存。                                |
| ACL_MEM_LOCATION_TYPE_H OST_NUMA = 4    | 通过 aclrtMallocPhysical 接口按照 NUMA ID 申请 Host 内存。 |
