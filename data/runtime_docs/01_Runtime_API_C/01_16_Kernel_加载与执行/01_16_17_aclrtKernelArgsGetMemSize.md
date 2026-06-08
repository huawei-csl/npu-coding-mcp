# aclrtKernelArgsGetMemSize

> **Section**: 1.16.17


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取 Kernel Launch 时参数列表所需内存的实际大小。

aclError aclrtKernelArgsGetMemSize(aclrtFuncHandle funcHandle, size\_t userArgsSize, size\_t *actualArgsSize)

| 参数名             | 输入 / 输 出   | 说明                                                                                         |
|-----------------|------------|--------------------------------------------------------------------------------------------|
| funcHandle      | 输入         | 核函数句柄。类型定义请参见 aclrtFuncHandle 。                                                            |
| userArgsSize    | 输入         | 在内存中存放参数列表数据所需的大小，单位为 Byte 。 每个参数数据的内存大小都需要 8 字节对齐，这里的 userArgsSize 是这些对齐后的参数数据内存大小相加的 总和。 |
| actualArgsSi ze | 输出         | Kernel Launch 时参数列表所需内存的实际大小，单位为 Byte 。                                                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
