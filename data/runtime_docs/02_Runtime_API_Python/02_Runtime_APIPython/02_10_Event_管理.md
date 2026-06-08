# Event 管理

> **Section**: 2.10


获取 Stream 属性值。

- C 函数原型

aclError aclrtGetStreamAttribute(aclrtStream stream, aclrtStreamAttr stmAttrType, aclrtStreamAttrValue *value)

- python 函数

value, ret = acl.rt.get\_stream\_attribute(stream, stm\_attr\_type)

| 参数名           | 说明                                                                                                                                                                                                              |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| stream        | int ，指定 Stream 。 各产品型号对默认 Stream （即该参数传入 0 ）的支持情况不 同，如下： Atlas 350 加速卡，不支持 Atlas A3 训练系列产品 /Atlas A3 推理系列产品，支持 Atlas A2 训练系列产品 /Atlas A2 推理系列产品，支持 Atlas 200I/500 A2 推理产品，不支持 Atlas 推理系列产品，不支持 Atlas 训练系列产品，不支持 |
| stm_attr_type | int ，属性类型。具体请参见新增数据结构 aclrtStreamAttr 。                                                                                                                                                                         |
