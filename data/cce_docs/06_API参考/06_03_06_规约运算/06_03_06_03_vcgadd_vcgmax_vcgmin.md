# vcgadd/vcgmax/vcgmin

> **Section**: 6.3.6.3


## 功能说明

## 接口原型

以 block （ 32Byte ）为单位完成向量的累加（或计算其中的最大值 / 最小值），每次迭 代计算 8 个 block ，输出为每个 block 的计算结果，共 8 个值，连续写入 dst 地址（ half 类 型输出占 16Byte ，fl oat 类型输出占 32Byte ）。

上述接口均支持通过 MASK 控制哪些元素参与计算。 MASK 应用于输入元素。如果某个 块 / 组的掩码全部为 0 ，则该接口不会写入对应的目标元素。

// 相同接口的不同原型区别在于源地址和目的地址的数据类型不同 // vcgadd

void vcgadd(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src, uint8\_t repeat, uint16\_t dstRepeatStride, uint16\_t srcBlockStride, uint16\_t srcRepeatStride);

void vcgadd(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src, uint8\_t repeat, uint16\_t dstRepeatStride, uint16\_t srcBlockStride, uint16\_t srcRepeatStride);

// vcgmax

void vcgmax(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src, uint8\_t repeat, uint16\_t dstRepeatStride, uint16\_t srcBlockStride, uint16\_t srcRepeatStride);

void vcgmax(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src, uint8\_t repeat, uint16\_t dstRepeatStride, uint16\_t srcBlockStride, uint16\_t srcRepeatStride);

// vcgmin

void vcgmin(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src, uint8\_t repeat, uint16\_t dstRepeatStride, uint16\_t srcBlockStride, uint16\_t srcRepeatStride);

## 参数说明

## 流水类型

PIPE\_V
