# vaddreluconv

> **Section**: 6.3.4.12


## 功能说明

对 src1 和 src2 进行元素级别的加法运算，然后执行 ReLU 操作并转换为另一种数据 类型，将结果写入 dst 。

该接口遵循双目向量模板，计算宽度取决于较大的数据元素，规则和 vconv 类似，在这 条接口中，数据宽度都是减半的，对应目标仅包含 4 个 block 而非 8 个，原因见 vmulconv 。因此，填写对应的参数时，如果希望 dst 连续存放， dstRepeatStride 应 该设为 4 （而不是常见的 8 ）。

## 计算公式如下：

[dst] = convert(ReLU([src0] + [src1]))

该接口支持通过 MASK 控制哪些元素参与计算。

// 相同接口的不同原型区别在于源地址和目的地址的数据类型不同。

void vaddreluconv\_f162s8(\_\_ubuf\_\_ int8\_t *dst, \_\_ubuf\_\_ half *src0, \_\_ubuf\_\_ half *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride, bool h);

void vaddreluconv\_s162s8(\_\_ubuf\_\_ int8\_t *dst, \_\_ubuf\_\_ int16\_t *src0, \_\_ubuf\_\_ int16\_t *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride, bool h);

void vaddreluconv\_f322f16(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ float *src0, \_\_ubuf\_\_ float *src1, uint8\_t repeat, uint8\_t dstBlockStride, uint8\_t src0BlockStride, uint8\_t src1BlockStride, uint8\_t dstRepeatStride, uint8\_t src0RepeatStride, uint8\_t src1RepeatStride, bool h);

参数含义见 表 2 双目运算参数说明。

PIPE\_V
