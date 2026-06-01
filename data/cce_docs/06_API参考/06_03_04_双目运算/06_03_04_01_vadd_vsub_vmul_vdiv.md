# vadd/vsub/vmul/vdiv

> **Section**: 6.3.4.1


## 功能说明

## 接口原型

## 接口原型

## 流水类型

计算每个向量元素的加法、减法、乘法或除法，计算公式如下：

// vadd

[dst] = [src0] + [src1]

// vsub

[dst] = [src0] - [src1]

// vmul

[dst] = [src0] * [src1]

// vdiv

[dst] = [src0] / [src1]

vdiv 中的 src1 不应该为零，否则结果未知，产生异常。

以 block （ 32Byte ）为单位完成计算，一次完成 8 个 block 的计算。

上述接口均支持通过 MASK 控制哪些元素参与计算。

## // 相同接口的不同原型区别在于源地址和目的地址的数据类型不同

void vadd(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src0, \_\_ubuf\_\_ half *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

// vadd

void vadd(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src0, \_\_ubuf\_\_ float *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

void vadd(\_\_ubuf\_\_ int16\_t *dst, \_\_ubuf\_\_ int16\_t *src0, \_\_ubuf\_\_ int16\_t *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

void vadd(\_\_ubuf\_\_ int32\_t *dst, \_\_ubuf\_\_ int32\_t *src0, \_\_ubuf\_\_ int32\_t *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

## // vsub

void vsub(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src0, \_\_ubuf\_\_ half *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

## 参数说明

## 流水类型

void vsub(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src0, \_\_ubuf\_\_ float *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

void vsub(\_\_ubuf\_\_ int16\_t *dst, \_\_ubuf\_\_ int16\_t *src0, \_\_ubuf\_\_ int16\_t *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

void vsub(\_\_ubuf\_\_ int32\_t *dst, \_\_ubuf\_\_ int32\_t *src0, \_\_ubuf\_\_ int32\_t *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

## // vmul

void vmul(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src0, \_\_ubuf\_\_ half *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

void vmul(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src0, \_\_ubuf\_\_ float *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

void vmul(\_\_ubuf\_\_ int16\_t *dst, \_\_ubuf\_\_ int16\_t *src0, \_\_ubuf\_\_ int16\_t *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

void vmul(\_\_ubuf\_\_ int32\_t *dst, \_\_ubuf\_\_ int32\_t *src0, \_\_ubuf\_\_ int32\_t *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

## // vdiv

void vdiv(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src0, \_\_ubuf\_\_ half *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

void vdiv(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src0, \_\_ubuf\_\_ float *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride);

参数含义见 表 2 双目运算参数说明。

PIPE\_V
