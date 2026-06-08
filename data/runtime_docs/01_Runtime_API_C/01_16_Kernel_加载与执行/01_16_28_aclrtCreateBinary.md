# aclrtCreateBinary

> **Section**: 1.16.28


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

创建 aclrtBinary 类型的数据，该数据类型用于描述算子二进制信息。此处的算子为使 用 Ascend C 语言开发的自定义算子。

如需销毁 aclrtBinary 类型的数据，请参见 aclrtDestroyBinary 。

aclrtBinary aclrtCreateBinary(const void *data, size\_t dataLen)

| 参数名     | 输入 / 输 出   | 说明                                                                                                               |
|---------|------------|------------------------------------------------------------------------------------------------------------------|
| data    | 输入         | 存放算子二进制文件（ *.o 文件）数据的内存地址指针。 Ascend EP 标准形态下，此处需申请 Host 上的内存； Ascend RC 形态或 Control CPU 开放形态下，此处需申请 Device 上的内存。 |
| dataLen | 输入         | 内存大小，单位 Byte 。                                                                                                   |

## 返回值说明

返回 aclrtBinary 类型的指针。
