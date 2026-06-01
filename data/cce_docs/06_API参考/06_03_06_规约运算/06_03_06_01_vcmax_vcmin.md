# vcmax/vcmin

> **Section**: 6.3.6.1


## 功能说明

vcmax ：获取 256Byte 向量的元素最大值及其索引，其中 half 类型有 128 个元素， float 类型有 64 个元素。最大值及其索引的输出由 order 控制。

## 接口原型

## 参数说明

vcmin ：获取 256Byte 向量的元素最小值及其索引，其中 half 类型有 128 个元素， float 类型有 64 个元素。最小值及其索引的输出由 order 控制。

上述接口均支持通过 MASK 控制哪些元素参与计算。

表 6-4 地址与步长对齐单位

| 数据类 型   | order 参 数   | 描述目的数据参数   | 描述目的数据参数        | 描述目的数据参数         | 描述源数据参数   | 描述源数据参数         | 描述源数据参数          |
|---------|-------------|------------|-----------------|------------------|-----------|-----------------|------------------|
| 数据类 型   | order 参 数   | 地址大 小      | dstBloc kStride | dstRepe atStride | 地址大 小     | srcBlock Stride | srcRepe atStride |
| f16     | 2 ' b00     | 4B         | /               | 4B               | 32B       | 32B             | 32B              |
| f16     | 2 ' b01     | 4B         | /               | 4B               | 32B       | 32B             | 32B              |
| f16     | 2 ' b10     | 2B         | /               | 2B               | 32B       | 32B             | 32B              |
| f16     | 2 ' b11     | 4B         | /               | 4B               | 32B       | 32B             | 32B              |
| f32     | 2 ' b00     | 8B         | /               | 8B               | 32B       | 32B             | 32B              |
| f32     | 2 ' b01     | 8B         | /               | 8B               | 32B       | 32B             | 32B              |
| f32     | 2 ' b10     | 4B         | /               | 4B               | 32B       | 32B             | 32B              |
| f32     | 2 ' b11     | 4B         | /               | 4B               | 32B       | 32B             | 32B              |

补充说明：以 order 为 2 ' b00 为例，地址大小为 4B 的含义是：最大值及其索引各占 2B 。 dstRepeatStride 含义是：单位是 4B 。

## // 相同接口的不同原型区别在于源地址和目的地址的数据类型不同

void vcmax(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src, uint8\_t repeat, uint16\_t dstRepeatStride, uint16\_t srcBlockStride, uint16\_t srcRepeatStride, Order\_t order);

// vcmax

void vcmax(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src, uint8\_t repeat, uint16\_t dstRepeatStride, uint16\_t srcBlockStride, uint16\_t srcRepeatStride, Order\_t order);

## // vcmin

void vcmin(\_\_ubuf\_\_ float *dst, \_\_ubuf\_\_ float *src, uint8\_t repeat, uint16\_t dstRepeatStride, uint16\_t srcBlockStride, uint16\_t srcRepeatStride, Order\_t order);

void vcmin(\_\_ubuf\_\_ half *dst, \_\_ubuf\_\_ half *src, uint8\_t repeat, uint16\_t dstRepeatStride, uint16\_t srcBlockStride, uint16\_t srcRepeatStride, Order\_t order);

参数含义见表 1 单目运算参数说明表。

## 流水类型
