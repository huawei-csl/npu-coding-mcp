# 函数： mem\_get\_allocation\_granularity

> **Section**: 2.12.30


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

查询内存申请粒度。系统内部计算给定分配规范的最小粒度或建议粒度，并以 granularity 参数返回粒度。此粒度可用作对齐、地址大小或地址映射的倍数。

- C 函数原型 aclError aclrtMemGetAllocationGranularity(aclrtPhysicalMemProp *prop, aclrtMemGranularityOptions option, size\_t *granularity)
- python 函数
- granularity, ret = acl.rt.mem\_get\_allocation\_granularity(prop, option)

| 参数名    | 说明                                                        |
|--------|-----------------------------------------------------------|
| prop   | dict ，物理内存属性信息，具体请参见 2.19.42 aclrtPhysicalMemProp 。       |
| option | int ，最小粒度或推荐粒度，具体请参见 2.19.37 aclrtMemGranularityOptions 。 |

| 返回值         | 说明                               |
|-------------|----------------------------------|
| granularity | int ，内存申请粒度，单位为 Byte ，当前只支持 2M 。 |
| ret         | int ，错误码，返回 0 表示成功，返回其它值表示失败。    |

## 约束说明

Ascend RC 形态不支持调用本接口。
