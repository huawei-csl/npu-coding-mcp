# aclrtPtrAttributes

> **Section**: 1.28.99


typedef struct aclrtPtrAttributes { aclrtMemLocation location; uint32\_t pageSize; uint32\_t rsv[4];

} aclrtPtrAttributes;

| 成员名称     | 说明                                                                               |
|----------|----------------------------------------------------------------------------------|
| location | 内存所在位置。类型定义请参见 aclrtMemLocation 。 当 type 为 ACL_MEM_LOCATION_TYPE_HOST 时， id 无 效。 |
| pageSize | 页表大小，单位 Byte 。                                                                   |
| rsv      | 预留参数。当前固定配置为 0 。                                                                 |
