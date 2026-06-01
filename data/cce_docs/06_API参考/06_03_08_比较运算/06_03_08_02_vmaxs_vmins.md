# vmaxs/vmins

> **Section**: 6.3.8.2


## 功能说明

将一个向量与标量逐元素比较，并将两者中较大或较小的值写入目标向量。

each\_element\_of([dst]) = max(each\_element\_of([src0]), src1) //src1 为标量 each\_element\_of([dst]) = min(each\_element\_of([src0]), src1) //src1 为标量

上述接口均支持通过 MASK 控制哪些元素参与计算。

## // 相同接口的不同原型区别在于源地址和目的地址的数据类型不同

void vmaxs(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src0, half src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

// vmaxs

void vmaxs(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src0, float src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vmaxs(\_\_ubuf\_\_ int16\_t *dst, \_\_ubuf\_\_ int16\_t *src0, int16\_t src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vmaxs(\_\_ubuf\_\_ int32\_t *dst, \_\_ubuf\_\_ int32\_t *src0, int32\_t src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

## // vmins

void vmins(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src0, half src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vmins(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src0, float src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vmins(\_\_ubuf\_\_ int16\_t *dst, \_\_ubuf\_\_ int16\_t *src0, int16\_t src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vmins(\_\_ubuf\_\_ int32\_t *dst, \_\_ubuf\_\_ int32\_t *src0, int32\_t src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

参数含义见 表 2 双目运算参数说明。

注意：接口中的 src1 是标量。

PIPE\_V

逐元素比较向量 src0 与向量 src1 的每个元素，如果比较后的结果为真，则输出结果 的对应比特位为 1 ，否则为 0 。

元素类型为 f16 时，向量中元素个数为 128 ，因此结果是一个连续的 128bit ，写入 CMPMASK 。

元素类型为 f32 时，向量中元素个数为 64 ，因此结果是一个连续的 64bit ，写入 CMPMASK 的低 64 位。

## 接口原型

## 参数说明

## 流水类型
