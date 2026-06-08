# aclrtMemPoolAttr

> **Section**: 1.28.90


typedef enum aclrtMemPoolAttr{

ACL\_RT\_MEM\_POOL\_REUSE\_FOLLOW\_EVENT\_DEPENDENCIES = 0x1, ACL\_RT\_MEM\_POOL\_REUSE\_ALLOW\_OPPORTUNISTIC = 0x2, ACL\_RT\_MEM\_POOL\_REUSE\_ALLOW\_INTERNAL\_DEPENDENCIES = 0x3, ACL\_RT\_MEM\_POOL\_ATTR\_RELEASE\_THRESHOLD = 0x4, ACL\_RT\_MEM\_POOL\_ATTR\_RESERVED\_MEM\_CURRENT = 0x5, ACL\_RT\_MEM\_POOL\_ATTR\_RESERVED\_MEM\_HIGH = 0x6, ACL\_RT\_MEM\_POOL\_ATTR\_USED\_MEM\_CURRENT = 0x7, ACL\_RT\_MEM\_POOL\_ATTR\_USED\_MEM\_HIGH = 0x8

} aclrtMemPoolAttr;

## 表 1-10 枚举项说明

| 枚举项                                                | 说明                                                                                                                                                                                                                                 |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_RT_MEM_POOL_REUSE_FOL LOW_EVENT_DEPENDENCIES   | 事件依赖内存复用开关。 在执行某个 Stream 的任务时，系统会查找与该 Stream 通过 Event 关联的其他 Stream ，并复用 这些关联 Stream 中的任务已归还到内存池中的 内存。此机制适用于用户应用程序中通过 Event 实现 Stream 间任务同步的场景。 属性值类型为 uint32_t ，取值如下： ● 1 ：启用事件依赖内存复用。 ● 0 ：关闭事件依赖内存复用。                            |
| ACL_RT_MEM_POOL_REUSE_ALL OW_OPPORTUNISTIC         | 机会主义内存复用开关。 在执行某个 Stream 的任务时，系统会检索内存 池中可复用的内存，但不保证内存复用一定成 功。当内存复用失败时，程序会报错停止。 属性值类型为 uint32_t ，取值如下： ● 1 ：启用机会主义内存复用。 ● 0 ：关闭机会主义内存复用。                                                                                            |
| ACL_RT_MEM_POOL_REUSE_ALL OW_INTERNAL_DEPENDENCIES | 隐式依赖内存复用开关。 在执行某个 Stream 的任务时，系统会检索内存 池中可复用的内存。若这些内存曾被其他 Stream 使用，但相关 Stream 之间不存在任务依 赖关系，则系统将自动在相关 Stream 之间增加 Event 同步等待逻辑，以确保前一个 Stream 中 的任务对内存的访问已经结束，从而实现安全 的内存复用。 属性值类型为 uint32_t ，取值如下： ● 1 ：启用隐式依赖内存复用。 ● 0 ：关闭隐式依赖内存复用。 |
| ACL_RT_MEM_POOL_ATTR_RELE ASE_THRESHOLD            | 释放空闲物理内存时，内存池中要保留的内存 大小阈值，单位 Byte 。默认值为 0 。 当内存池中的空闲物理内存超过该阈值时，在 下一次 Stream 同步（例如调用 aclrtSynchronizeStream 接口）时，系统将尝 试释放空闲内存。 属性值类型为 uint64_t 。                                                                                    |

| 枚举项                                        | 说明                                                         |
|--------------------------------------------|------------------------------------------------------------|
| ACL_RT_MEM_POOL_ATTR_RESE RVED_MEM_CURRENT | 内存池中当前被申请的内存总量，该属性只 读。 属性值类型为 uint64_t 。                   |
| ACL_RT_MEM_POOL_ATTR_RESE RVED_MEM_HIGH    | 内存池中当前被申请的内存总量的历史峰值。 属性值类型为 uint64_t 。 设置该属性时，属性值只能为 0 。   |
| ACL_RT_MEM_POOL_ATTR_USE D_MEM_CURRENT     | 内存池中实际正在使用的内存总量，该属性只 读。 属性值类型为 uint64_t 。                  |
| ACL_RT_MEM_POOL_ATTR_USE D_MEM_HIGH        | 内存池中实际正在使用的内存总量的历史峰 值。 属性值类型为 uint64_t 。 设置该属性时，属性值只能为 0 。 |
