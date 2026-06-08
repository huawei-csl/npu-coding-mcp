# aclrtCntNotifyWaitMode

> **Section**: 1.28.41


```
typedef enum { ACL_RT_CNT_NOTIFY_WAIT_LESS_MODE = 0,               // CntNotify 的当前计数值 < value ，则解除 Wait ACL_RT_CNT_NOTIFY_WAIT_EQUAL_MODE = 1,              // CntNotify 的当前计数值 = value ，则解除 Wait ACL_RT_CNT_NOTIFY_WAIT_BIGGER_MODE = 2,             // CntNotify 的当前计数值 > value ，则解除 Wait ACL_RT_CNT_NOTIFY_WAIT_BIGGER_OR_EQUAL_MODE = 3,    // CntNotify 的当前计数值 >= value ，则解 除 Wait ACL_RT_CNT_NOTIFY_WAIT_EQUAL_WITH_BITMASK_MODE = 4, // CntNotify 的当前计数值 & value = value ，则解除 Wait } aclrtCntNotifyWaitMode;
```
