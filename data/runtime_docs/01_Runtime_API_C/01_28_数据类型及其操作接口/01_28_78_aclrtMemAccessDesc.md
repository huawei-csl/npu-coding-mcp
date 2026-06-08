# aclrtMemAccessDesc

> **Section**: 1.28.78


```
typedef struct { aclrtMemAccessFlags flags; aclrtMemLocation location; uint8_t rsv[12]; } aclrtMemAccessDesc;
```

| 成员名称     | 描述                                                                                                                                                                                                                       |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| flags    | 内存访问保护标志。类型定义请参见 aclrtMemAccessFlags 。 当前仅支持 ACL_RT_MEM_ACCESS_FLAGS_READWRITE ，表示地 址范围可读可写。                                                                                                                             |
| location | 内存所在位置。类型定义请参见 aclrtMemLocation 。 当前仅支持将 aclrtMemLocation.type 设置为 ACL_MEM_LOCATION_TYPE_HOST 或 ACL_MEM_LOCATION_TYPE_DEVICE 。当 aclrtMemLocation.type 为 ACL_MEM_LOCATION_TYPE_HOST 时， aclrtMemLocation.id 无效，固定设置为 0 即可。 |
| rsv      | 预留参数，当前固定配置为 0 。                                                                                                                                                                                                         |
