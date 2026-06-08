# acltdtQueueRouteQueryMode

> **Section**: 1.28.134


```
typedef enum { ACL_TDT_QUEUE_ROUTE_QUERY_SRC = 0,         // 指定为只根据源队列 ID 匹配查询 ACL_TDT_QUEUE_ROUTE_QUERY_DST = 1,         // 指定为只根据目标队列 ID 匹配查询 ACL_TDT_QUEUE_ROUTE_QUERY_SRC_AND_DST = 2,  // 指定为同时根据源、目标队列 ID 匹配查询 ACL_TDT_QUEUE_ROUTE_QUERY_ABNORMAL = 100   // 指定为查询异常路由 } acltdtQueueRouteQueryMode;
```
