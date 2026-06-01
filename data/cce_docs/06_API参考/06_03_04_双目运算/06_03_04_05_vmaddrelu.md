# vmaddrelu

> **Section**: 6.3.4.5


## 功能说明

计算源数据和目的数据逐元素相乘后再与另一个源数据相加后施加 ReLU 函数，计算 公式如下：

[dst] = ReLU([src0] * [dst] + [src1])

以 block （ 32Byte ）为单位完成计算，一次完成 8 个 block 的计算。

该接口支持通过 MASK 控制哪些元素参与计算。

// 相同接口的不同原型区别在于源地址和目的地址的数据类型不同。 void vmaddrelu(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src0, \_\_ubuf\_\_ half *src1, uint8\_t repeat, uint8\_t

## 参数说明

## 流水类型

## 接口原型

## 参数说明

dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

void vmaddrelu(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src0, \_\_ubuf\_\_ float *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

参数含义见 表 2 双目运算参数说明。

PIPE\_V
