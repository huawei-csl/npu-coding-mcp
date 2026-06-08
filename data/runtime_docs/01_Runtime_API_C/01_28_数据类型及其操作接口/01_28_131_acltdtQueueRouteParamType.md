# acltdtQueueRouteParamType

> **Section**: 1.28.131


typedef enum {

ACL\_TDT\_QUEUE\_ROUTE\_SRC\_UINT32 = 0,  // 源队列 ID

ACL\_TDT\_QUEUE\_ROUTE\_DST\_UINT32,      //

目标队列 ID

ACL\_TDT\_QUEUE\_ROUTE\_STATUS\_INT32     //

路由绑定状态， 0 表示未绑定， 1 表示绑定， 2 表示绑定异常

} acltdtQueueRouteParamType;
