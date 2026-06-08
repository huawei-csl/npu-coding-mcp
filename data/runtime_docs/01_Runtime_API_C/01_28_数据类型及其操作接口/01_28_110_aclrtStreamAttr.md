# aclrtStreamAttr

> **Section**: 1.28.110


typedef enum {

```
ACL_STREAM_ATTR_FAILURE_MODE         = 1, ACL_STREAM_ATTR_FLOAT_OVERFLOW_CHECK = 2, ACL_STREAM_ATTR_USER_CUSTOM_TAG      = 3, ACL_STREAM_ATTR_CACHE_OP_INFO        = 4, } aclrtStreamAttr;
```

| 枚举项                           | 说明                                                                                                                                           |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_STREAM_ATTR_FAI LURE_MODE | 当 Stream 上的任务执行出错时，可通过该属性设置 Stream 的任务调度模式，以便控制某个任务失败后是否 继续执行下一个任务 默认 Stream 不支持设置任务调度模式。 通过该属性设置任务调度模式，与 aclrtSetStreamFailureMode 接口的功能一致。 |

| 枚举项                                    | 说明                                                                                                                                                                                     |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_STREAM_ATTR_FL OAT_OVERFLOW_CHEC K | 饱和模式下，当与上层训练框架（例如 PyTorch ）对接 时，针对指定 Stream ，可通过该属性打开或关闭溢出检 测开关。关闭后，将无法通过溢出检测算子获取任务是 否溢出。 打开或关闭溢出检测开关后，仅对后续新下的任务生 效，已下发的任务仍维持原样。 通过该属性设置溢出检测开关，与 aclrtSetStreamOverflowSwitch 接口的功能一致。 |
| ACL_STREAM_ATTR_US ER_CUSTOM_TAG       | 设置 Stream 上的溢出检测分组标签，以确定溢出发生时 检测的粒度。如果不设置分组标签，默认为进程粒度。 如果设置了分组标签，则仅检测与发生溢出的 Stream 具 有相同分组标签的 Stream 。                                                                                 |
| ACL_STREAM_ATTR_CA CHE_OP_INFO         | 基于捕获方式构建模型运行实例场景下，通过该属性设 置 Stream 的算子信息缓存开关，以便于控制后续采集性 能数据时是否附带算子信息。 该属性需与其它接口配合使用，请参见 aclrtCacheLastTaskOpInfo 中的接口调用流程。 跨 Stream 的任务捕获时，与主流关联的其他 Stream ，其 算子信息缓存开关状态与主流一致。          |
