# 函数： set\_stream\_attribute

> **Section**: 2.9.14


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

设置 Stream 属性值。

## ● C 函数原型

aclError aclrtSetStreamAttribute(aclrtStream stream, aclrtStreamAttr stmAttrType, aclrtStreamAttrValue *value)

- python 函数

ret = acl.rt.set\_stream\_attribute(stream, stm\_attr\_type, value)

| 参数名           | 说明                                                                                                                                                                                                              |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| stream        | int ，指定 Stream 。 各产品型号对默认 Stream （即该参数传入 0 ）的支持情况不 同，如下： Atlas 350 加速卡，不支持 Atlas A3 训练系列产品 /Atlas A3 推理系列产品，支持 Atlas A2 训练系列产品 /Atlas A2 推理系列产品，支持 Atlas 200I/500 A2 推理产品，不支持 Atlas 推理系列产品，不支持 Atlas 训练系列产品，不支持 |
| stm_attr_type | int ，属性类型。具体请参见新增数据结构 aclrtStreamAttr 。                                                                                                                                                                         |

## 返回值说明

## 约束说明

| 参数名   | 说明                                           |
|-------|----------------------------------------------|
| value | dict ，属性值。具体请参见新增数据结构 aclrtStreamAttrValue 。 |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |

- 溢出检测属性：调用该接口打开或关闭溢出检测开关后，仅对后续新下的任务生 效，已下发的任务仍维持原样。
- Failure Mode ：不支持对 Context 默认 Stream 设置 Failure Mode 。
- stm\_attr\_type 设置为 ACL\_STREAM\_ATTR\_FAILURE\_MODE 时，支持如下产品型 号：
- -Atlas 推理系列产品
- -Atlas 200I/500 A2 推理产品
- -Atlas 训练系列产品
- -Atlas A2 训练系列产品 /Atlas A2 推理系列产品
- -Atlas A3 训练系列产品 /Atlas A3 推理系列产品
- stm\_attr\_type 设置为 ACL\_STREAM\_ATTR\_FLOAT\_OVERFLOW\_CHECK 、 ACL\_STREAM\_ATTR\_USER\_CUSTOM\_TAG 时，支持如下产品型号：
- -Atlas A2 训练系列产品 /Atlas A2 推理系列产品
- -Atlas A3 训练系列产品 /Atlas A3 推理系列产品
