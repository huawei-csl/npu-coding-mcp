# load\_cbuf\_to\_cb\_transpose

> **Section**: 6.5.5.3


## 功能说明

## 接口原型

## 参数说明

## 流水类型

实现数据从 L1 搬运到 L0B ，这条接口在完成搬运时将同时实现简单的分形矩阵转置，相 较 6.5.4.3 load\_cbuf\_to\_cb ，其区别在于：本类接口始终带有转置操作，而 6.5.4.3 load\_cbuf\_to\_cb 的转置操作由参数 transpose 控制；并且本类接口对数据类型的支持 范围更广（支持 {b4, b8, b16, b32} ）， 6.5.4.3 load\_cbuf\_to\_cb 若需实现分形的转置 仅支持 b16 数据类型。

// 相同接口的不同原型区别在于源地址和目的地址的数据类型不同 void load\_cbuf\_to\_cb\_transpose(\_\_ca\_\_ bfloat16\_t *dst, \_\_cbuf\_\_ bfloat16\_t *src, uint16\_t indexID, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, bool addrmode, uint16\_t dstFracGap);

void load\_cbuf\_to\_cb\_transpose(\_\_ca\_\_ half *dst, \_\_cbuf\_\_ half *src, uint16\_t indexID, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, bool addrmode, uint16\_t dstFracGap);

void load\_cbuf\_to\_cb\_transpose(\_\_ca\_\_ float *dst, \_\_cbuf\_\_ float *src, uint16\_t indexID, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, bool addrmode, uint16\_t dstFracGap);

void load\_cbuf\_to\_cb\_transpose(\_\_ca\_\_ int32\_t *dst, \_\_cbuf\_\_ int32\_t *src, uint16\_t indexID, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, bool addrmode, uint16\_t dstFracGap);

void load\_cbuf\_to\_cb\_transpose(\_\_ca\_\_ int8\_t *dst, \_\_cbuf\_\_ int8\_t *src, uint16\_t indexID, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, bool addrmode, uint16\_t dstFracGap);

void load\_cbuf\_to\_cb\_transpose(\_\_ca\_\_ uint32\_t *dst, \_\_cbuf\_\_ uint32\_t *src, uint16\_t indexID, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, bool addrmode, uint16\_t dstFracGap);

void load\_cbuf\_to\_cb\_transpose(\_\_ca\_\_ uint8\_t *dst, \_\_cbuf\_\_ uint8\_t *src, uint16\_t indexID, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, bool addrmode, uint16\_t dstFracGap);

## // void * 为 s4

void load\_cbuf\_to\_cb\_transpose\_s4(\_\_cb\_\_ void *dst, \_\_cbuf\_\_ void *src, uint16\_t indexID, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, bool addrmode, uint16\_t dstFracGap);

参数含义见表 1 具备转置的矩阵输入搬运参数说明。

PIPE\_MTE1
