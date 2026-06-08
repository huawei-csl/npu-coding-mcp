# 函数： destroy\_step\_info

> **Section**: 2.16.4.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

销毁通过 acl.prof.create\_step\_info 接口创建的 aclprofStepInfo 类型的数据。

## ● C 函数原型

void aclprofDestroyStepInfo (aclprofStepInfo * stepinfo)

- python 函数

acl.prof.destroy\_step\_info(stepinfo)

| 参数名      | 说明                                                                       |
|----------|--------------------------------------------------------------------------|
| stepinfo | int ，指定迭代信息，需提前调用 acl.prof.create_step_info 接口创 建 aclprofStepInfo 类型的数据。 |

无

- 与 acl.prof.create\_step\_info 接口配对使用，先调用 acl.prof.create\_step\_info 接口 再调用 acl.prof.destroy\_step\_info 接口。
- 同一 aclprofStepInfo 数据重复调用 acl.prof.destroy\_step\_info 接口，会出现重复释 放内存的报错。
