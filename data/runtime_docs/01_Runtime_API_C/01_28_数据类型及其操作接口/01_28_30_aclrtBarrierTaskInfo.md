# aclrtBarrierTaskInfo

> **Section**: 1.28.30


typedef struct { size\_t barrierNum; aclrtBarrierCmoInfo cmoInfo[ACL\_RT\_CMO\_MAX\_BARRIER\_NUM]; } aclrtBarrierTaskInfo;

| 成员名称       | 说明                                                                                  |
|------------|-------------------------------------------------------------------------------------|
| barrierNum | cmoInfo 数组的长度。                                                                      |
| cmoInfo    | Cache 内存操作的任务信息。类型定义请参见 aclrtBarrierCmoInfo 。 #define ACL_RT_CMO_MAX_BARRIER_NUM 6U |
