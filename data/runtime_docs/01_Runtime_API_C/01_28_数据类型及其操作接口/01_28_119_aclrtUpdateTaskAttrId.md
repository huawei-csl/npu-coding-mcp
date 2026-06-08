# aclrtUpdateTaskAttrId

> **Section**: 1.28.119


typedef enum { ACL\_RT\_UPDATE\_RANDOM\_TASK = 1, ACL\_RT\_UPDATE\_AIC\_AIV\_TASK, } aclrtUpdateTaskAttrId;

| 枚举项                         | 说明                                                                                                                                     |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| ACL_RT_UPDATE_RAND OM_TASK  | 随机数生成任务。 不同型号对该任务支持的情况不同： Atlas A3 训练系列产品 /Atlas A3 推理系列产品支持随机 数生成任务 Atlas A2 训练系列产品 /Atlas A2 推理系列产品支持随机 数生成任务 Atlas 推理系列产品不支持随机数生成任务 |
| ACL_RT_UPDATE_AIC_A IV_TASK | 在 Cube\Vector 计算单元上执行的计算任务。                                                                                                            |
