# aclrtStreamConfigAttr

> **Section**: 1.28.112


typedef enum {

ACL\_RT\_STREAM\_WORK\_ADDR\_PTR = 0, ACL\_RT\_STREAM\_WORK\_SIZE, ACL\_RT\_STREAM\_FLAG, ACL\_RT\_STREAM\_PRIORITY, } aclrtStreamConfigAttr;

表 1-13 枚举项说明

| 枚举项                          | 说明                                                                                                                                                                                                                                                                                                                           |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_RT_STREAM_WORK _ADDR_PTR | 某一个 Stream 上的模型所需工作内存（ Device 上存放模 型执行过程中的临时数据）的指针，由用户管理工作内 存。该配置主要用于多模型在同一个 Stream 上串行执行 时想共享工作内存的场景，此时需按多个模型中最大的 工作内存来申请内存，可提前使用 aclmdlQuerySize 查 询各模型所需的工作内存大小。 如果同时配置 ACL_RT_STREAM_WORK_ADDR_PTR 以 及 aclmdlExecConfigAttr 中的 ACL_MDL_WORK_ADDR_PTR （表示某个模型的工作内 存），则以 aclmdlExecConfigAttr 中的 ACL_MDL_WORK_ADDR_PTR 优先。 |
| ACL_RT_STREAM_WORK _SIZE     | 模型所需工作内存的大小，单位为 Byte 。                                                                                                                                                                                                                                                                                                       |
| ACL_RT_STREAM_FLAG           | 预留配置，默认值为 0 。                                                                                                                                                                                                                                                                                                                |

| 枚举项                     | 说明                                        |
|-------------------------|-------------------------------------------|
| ACL_RT_STREAM_PRIORI TY | Stream 的优先级，数字越小优先级越高，取值 [0,7] 。 默认值为 0 。 |
