# aclMemType

> **Section**: 2.19.11


| 内存类型                                      | 含义         |
|-------------------------------------------|------------|
| ACL_MEMTYPE_DEVICE = 0                    | Device 内存。 |
| ACL_MEMTYPE_HOST = 1                      | Host 内存。   |
| ACL_MEMTYPE_HOST_COMPI LE_INDEPENDENT = 2 | Host 内存。   |

## 说明

ACL\_MEMTYPE\_HOST 和 ACL\_MEMTYPE\_HOST\_COMPILE\_INDEPENDENT 都标识 Host 内存， 但在使用上有区别：

- ACL\_MEMTYPE\_HOST\_COMPILE\_INDEPENDENT ：设置该选项时，算子输入或输出的值 的变化，都不会触发算子重新编译。若算子编译时依赖其输入或输出的值，此时如果设置 为 ACL\_MEMTYPE\_HOST\_COMPILE\_INDEPENDENT ，则可能会导致编译失败。
