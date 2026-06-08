# aclrtPhysicalMemProp

> **Section**: 1.28.98


typedef struct aclrtPhysicalMemProp {

aclrtMemHandleType handleType; aclrtMemAllocationType allocationType; aclrtMemAttr memAttr; aclrtMemLocation location; uint64\_t reserve; } aclrtPhysicalMemProp;

| 成员名称           | 描述                                                                                          |
|----------------|---------------------------------------------------------------------------------------------|
| handleType     | handle 类型。类型定义请参见 aclrtMemHandleType 。 当前仅支持 ACL_MEM_HANDLE_TYPE_NONE 。                     |
| allocationType | 内存分配类型。类型定义请参见 aclrtMemAllocationType 。 当前仅支持 ACL_MEM_ALLOCATION_TYPE_PINNED ，表示锁页 内存。      |
| memAttr        | 内存属性。类型定义请参见 aclrtMemAttr 。                                                                 |
| location       | 内存所在位置。类型定义请参见 aclrtMemLocation 。 当 type 为 ACL_MEM_LOCATION_TYPE_HOST 时， id 无效，固定设 置为 0 即可。 |
| reserve        | 预留。                                                                                         |
