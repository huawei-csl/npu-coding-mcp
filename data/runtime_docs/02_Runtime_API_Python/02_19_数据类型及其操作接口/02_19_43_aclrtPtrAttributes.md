# aclrtPtrAttributes

> **Section**: 2.19.43


| 成员名称     | 说明                                                                                          |
|----------|---------------------------------------------------------------------------------------------|
| location | dict ，内存所在位置，具体请参见 2.19.39 aclrtMemLocation 。 当 type 为 ACL_MEM_LOCATION_TYPE_HOST 时， id 无效。 |
| pageSize | int ，页表大小，单位 Byte 。                                                                         |
| rsv[4]   | list ，预留参数。                                                                                 |
