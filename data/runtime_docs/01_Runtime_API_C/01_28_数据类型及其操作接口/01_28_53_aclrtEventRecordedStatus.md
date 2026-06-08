# aclrtEventRecordedStatus

> **Section**: 1.28.53


```
typedef enum aclrtEventRecordedStatus { ACL_EVENT_RECORDED_STATUS_NOT_READY = 0,  //Event 未被记录到 Stream 中，或记录到 Stream 中的 Event 未被执行或执行失败 ACL_EVENT_RECORDED_STATUS_COMPLETE = 1,   // 记录到 Stream 中的 Event 执行成功 } aclrtEventRecordedStatus;
```
