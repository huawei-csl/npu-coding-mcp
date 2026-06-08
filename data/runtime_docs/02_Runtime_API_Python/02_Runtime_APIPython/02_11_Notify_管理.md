# Notify 管理

> **Section**: 2.11


| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

查询当前 Device 上可用的 Event 数量。

- C 函数原型

aclError aclrtGetEventAvailNum(uint32\_t *eventCount)

- python 函数
- event\_count, ret = acl.rt.get\_event\_avail\_num()

无
