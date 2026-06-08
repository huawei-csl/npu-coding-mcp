# aclrtPhysicalMemProp

> **Section**: 2.19.42


| 成员名称           | 描述                                               |
|----------------|--------------------------------------------------|
| handleType     | handle 类型，当前仅支持 ' ACL_MEM_HANDLE_TYPE_NONE '。    |
| allocationType | 内存分配类型，当前仅支持 ' ACL_MEM_ALLOCATION_TYPE_PINNED '。 |
| memAttr        | 内存属性，具体请参见 2.19.36 aclrtMemAttr 。                |

| 成员名称     | 描述                                                                                                                            |
|----------|-------------------------------------------------------------------------------------------------------------------------------|
| location | 设置内存所在位置。请参考以下方式传入，其中' id '表 示 Device 的 ID ，' type '为内存所在位置类型。 location = { 'id' : 0, 'type' : ACL_MEM_LOCATION_TYPE_DEVICE } |
| reserve  | 预留。                                                                                                                           |
