# load\_cbuf\_to\_ca

> **Section**: 6.5.4.2


## 功能说明

## 接口原型

## 参数说明

## 流水类型

实现数据从 L1 搬运到 L0A ，这条接口在完成搬运时可以通过 transpose 参数实现简单的 分形矩阵转置，但仅对 b16 类型有效。如果数据类型为 b4 、 b8 、 b32 需要转置，请参考 6.5.5.2 load\_cbuf\_to\_ca\_transpose 接口。

## // 相同接口的不同原型区别在于源地址和目的地址的数据类型不同

void load\_cbuf\_to\_ca(\_\_ca\_\_ bfloat16\_t *dst, \_\_cbuf\_\_ bfloat16\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, bool transpose, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_cbuf\_to\_ca(\_\_ca\_\_ half *dst, \_\_cbuf\_\_ half *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, bool transpose, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_cbuf\_to\_ca(\_\_ca\_\_ float *dst, \_\_cbuf\_\_ float *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, bool transpose, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_cbuf\_to\_ca(\_\_ca\_\_ int32\_t *dst, \_\_cbuf\_\_ int32\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, bool transpose, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_cbuf\_to\_ca(\_\_ca\_\_ int8\_t *dst, \_\_cbuf\_\_ int8\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, bool transpose, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_cbuf\_to\_ca(\_\_ca\_\_ uint32\_t *dst, \_\_cbuf\_\_ uint32\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, bool transpose, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_cbuf\_to\_ca(\_\_ca\_\_ uint8\_t *dst, \_\_cbuf\_\_ uint8\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, bool transpose, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

## // void * 为 s4

void load\_cbuf\_to\_ca\_s4(\_\_ca\_\_ void *dst, \_\_cbuf\_\_ void *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, bool transpose, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

参数含义见表 1 矩阵输入搬运参数说明。

PIPE\_MTE1
