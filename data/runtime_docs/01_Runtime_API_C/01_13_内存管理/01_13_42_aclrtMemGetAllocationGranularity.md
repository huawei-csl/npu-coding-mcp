# aclrtMemGetAllocationGranularity

> **Section**: 1.13.42


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

查询内存申请粒度。

系统内部会根据用户指定的内存属性信息计算最小粒度或建议粒度，并以 granularity 参数返回粒度。此粒度可用作对齐、地址大小或地址映射的倍数。

aclError aclrtMemGetAllocationGranularity(aclrtPhysicalMemProp *prop, aclrtMemGranularityOptions option, size\_t *granularity)

## 参数说明

## 返回值说明

## 约束说明

## 接口调用示例

| 参数名          | 输入 / 输出   | 说明                                             |
|--------------|-----------|------------------------------------------------|
| prop         | 输入        | 物理内存属性信息。类型定义请参见 aclrtPhysicalMemProp 。        |
| option       | 输入        | 最小粒度或推荐粒度。类型定义请参见 aclrtMemGranularityOptions 。 |
| granularit y | 输出        | 内存申请粒度，单位为 Byte 。                              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

Atlas 200I/500 A2 推理产品上， Ascend RC 形态不支持调用本接口。

接口调用示例，参见进程间通信。
