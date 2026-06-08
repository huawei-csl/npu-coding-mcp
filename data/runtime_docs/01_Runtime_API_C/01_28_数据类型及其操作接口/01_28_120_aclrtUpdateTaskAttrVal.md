# aclrtUpdateTaskAttrVal

> **Section**: 1.28.120


typedef union { aclrtRandomTaskUpdateAttr randomTaskAttr; aclrtAicAivTaskUpdateAttr aicAivTaskAttr; } aclrtUpdateTaskAttrVal;

| 成员名称           | 说明                                                                                                                                                                        |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| randomTaskAttr | 随机数生成任务。类型定义请参见 aclrtRandomTaskUpdateAttr 。 不同型号对该任务支持的情况不同： Atlas A3 训练系列产品 /Atlas A3 推理系列产品支持随机 数生成任务 Atlas A2 训练系列产品 /Atlas A2 推理系列产品支持随机 数生成任务 Atlas 推理系列产品不支持随机数生成任务 |
| aicAivTaskAttr | 在 Cube\Vector 计算单元上执行的计算任务。类型定义请 参见 aclrtAicAivTaskUpdateAttr 。                                                                                                           |
