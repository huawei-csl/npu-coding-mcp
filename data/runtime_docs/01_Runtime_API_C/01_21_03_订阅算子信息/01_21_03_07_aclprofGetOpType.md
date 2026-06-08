# aclprofGetOpType

> **Section**: 1.21.3.7


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取指定算子的算子类型名称。

## 函数原型

## 参数说明

## 返回值说明

建议用户新建一个线程，在新线程内调用该接口，否则可能阻塞主线程中的其它任务 调度。

aclError aclprofGetOpType(const void *opInfo, size\_t opInfoLen, uint32\_t index, char *opType, size\_t opTypeLen)

| 参数名       | 输入 / 输 出   | 说明                                                                                  |
|-----------|------------|-------------------------------------------------------------------------------------|
| opInfo    | 输入         | 包含算子信息的地址。                                                                          |
| opInfoLen | 输入         | 算子信息的长度。                                                                            |
| index     | 输入         | 指定获取第几个算子的算子类型名称。 用户调用 aclprofGetOpNum 接口获取算子数量后，这 个 index 的取值范围： [0, ( 算子数量 -1)] 。 |
| opType    | 输出         | 算子类型名称。                                                                             |
| opTypeLen | 输入         | opType 的实际内存申请长度。取值范围建议不小于 aclprofGetOpTypeLen ，否则内容会有截断。                           |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
