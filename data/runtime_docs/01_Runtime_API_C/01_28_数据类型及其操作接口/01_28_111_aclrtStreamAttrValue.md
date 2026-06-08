# aclrtStreamAttrValue

> **Section**: 1.28.111


typedef union {

uint64\_t failureMode;

uint32\_t overflowSwitch;

uint32\_t userCustomTag;

uint32\_t cacheOpInfoSwitch;

uint32\_t reserve[4];

} aclrtStreamAttrValue;

| 成员名称        | 说明                                                                                                                                                                                                                                       |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| failureMode | 设置 aclrtStreamAttr 中的 ACL_STREAM_ATTR_FAILURE_MODE （表示 Stream 的 任务调度模式）属性时，属性值的取值如下： ● 0 ：某个任务失败后，继续执行下一个任务。默认值 为 0 。 ● 1 ：某个任务失败后，停止执行后续的任务，通常称 作遇错即停。触发遇错即停之后，不支持再下发新任 务。 当 Stream 上设置了遇错即停模式，该 Stream 所在的 Context 下的其它 Stream 也是遇错即停。 |

| 成员名称              | 说明                                                                                                                       |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| overflowSwitch    | 设置 aclrtStreamAttr 中的 ACL_STREAM_ATTR_FLOAT_OVERFLOW_CHECK （表示 溢出检测开关）属性时，属性值的取值如下： ● 0 ：关闭溢出检测。默认值为 0 。 ● 1 ：打开溢出检测。    |
| userCustomTag     | 设置 aclrtStreamAttr 中的 ACL_STREAM_ATTR_USER_CUSTOM_TAG （表示溢出检 测分组标签）属性时，属性值的取值范围： 0~uint32_t 类型的最大值。                      |
| cacheOpInfoSwitch | 设置 aclrtStreamAttr 中的 ACL_STREAM_ATTR_CACHE_OP_INFO （表示算子信息 缓存开关）属性时，属性值的取值如下： ● 0 ：关闭算子信息缓存开关。默认值为 0 。 ● 1 ：开启算子信息缓存开关。 |
| reserve           | 预留值。                                                                                                                     |
