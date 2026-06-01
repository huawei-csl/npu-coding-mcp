# vadds/vmuls

> **Section**: 6.3.4.6


## 功能说明

## 计算源数据逐元素加上或乘标量 a ，计算公式如下：

// vadds

// vmuls

each\_element\_of([dst]) = a + each\_element\_of([src])

each\_element\_of([dst]) = a * each\_element\_of([src])

以 block （ 32Byte ）为单位完成计算，一次完成 8 个 block 的计算。

上述接口均支持通过 MASK 控制哪些元素参与计算。

## // 相同接口的不同原型区别在于源地址和目的地址的数据类型不同。

void vadds(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src, half a, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

// vadds

void vadds(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src, float a, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vadds(\_\_ubuf\_\_ int16\_t *dst, \_\_ubuf\_\_ int16\_t *src, int16\_t a, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vadds(\_\_ubuf\_\_ int32\_t *dst, \_\_ubuf\_\_ int32\_t *src, int32\_t a, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

## // vmuls

void vmuls(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src0, half src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vmuls(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src0, float src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vmuls(\_\_ubuf\_\_ int16\_t *dst, \_\_ubuf\_\_ int16\_t *src0, int16\_t src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

void vmuls(\_\_ubuf\_\_ int32\_t *dst, \_\_ubuf\_\_ int32\_t *src0, int32\_t src1, uint8\_t repeat, uint16\_t dstBlockStride, uint16\_t srcBlockStride, uint16\_t dstRepeatStride, uint16\_t srcRepeatStride);

参数含义见 表 2 双目运算参数说明。

## 流水类型
