# 函数： get\_cann\_attribute\_list

> **Section**: 2.18.8


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

查询运行环境中 CANN 软件和对应芯片支持的特性列表。

## ● C 函数原型

aclError aclGetCannAttributeList(const aclCannAttr **cannAttrList, size\_t *num)

- python 函数
- cann\_attr\_list, num, ret = acl.get\_cann\_attribute\_list()

无

| 返回值             | 说明                                                                            |
|-----------------|-------------------------------------------------------------------------------|
| cann_attr_l ist | list ，用于保存运行环境支持的特性枚举列表，具体请参见 2.19.2 aclCannAttr 。 用户无需提前申请内存，应用进程退出时，内存自动释放。 |
| num             | int ，用于保存支持的特性数量，与' cann_attr_list '列表长度保持一 致。                                |
| ret             | int ，错误码，返回 0 表示成功，返回其它值表示失败。                                                 |
