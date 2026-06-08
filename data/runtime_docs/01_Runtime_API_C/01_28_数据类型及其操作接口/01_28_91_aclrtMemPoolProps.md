# aclrtMemPoolProps

> **Section**: 1.28.91


typedef struct {

aclrtMemAllocationType allocType; aclrtMemHandleType handleType; aclrtMemLocation location; size\_t maxSize; unsigned char reserved[32]; } aclrtMemPoolProps;

| 成员名称       | 描述                                                                                     |
|------------|----------------------------------------------------------------------------------------|
| allocType  | 内存分配类型。类型定义请参见 aclrtMemAllocationType 。 当前仅支持 ACL_MEM_ALLOCATION_TYPE_PINNED ，表示锁页 内存。 |
| handleType | handle 类型。类型定义请参见 aclrtMemHandleType 。                                                 |
| location   | 内存所在位置。类型定义请参见 aclrtMemLocation 。 type 当前仅支持设置为 ACL_MEM_LOCATION_TYPE_DEVICE 。         |
| maxSize    | 内存池大小，单位 Byte 。                                                                        |
| reserved   | 保留字段，当前必须为全 0 字符串。                                                                     |
