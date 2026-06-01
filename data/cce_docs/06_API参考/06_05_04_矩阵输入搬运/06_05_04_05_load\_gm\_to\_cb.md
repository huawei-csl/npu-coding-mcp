# load\_gm\_to\_cb

> **Section**: 6.5.4.5


## 功能说明

实现数据从 GM 搬运到 L0B ，该接口不具备分形矩阵转置的能力，仅做简单搬运。

## // 相同接口的不同原型区别在于源地址和目的地址的数据类型不同

void load\_gm\_to\_cb(\_\_cb\_\_ bfloat16\_t *dst, \_\_gm\_\_ bfloat16\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_gm\_to\_cb(\_\_cb\_\_ half *dst, \_\_gm\_\_ half *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_gm\_to\_cb(\_\_cb\_\_ float *dst, \_\_gm\_\_ float *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_gm\_to\_cb(\_\_cb\_\_ int32\_t *dst, \_\_gm\_\_ int32\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_gm\_to\_cb(\_\_cb\_\_ int8\_t *dst, \_\_gm\_\_ int8\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_gm\_to\_cb(\_\_cb\_\_ uint32\_t *dst, \_\_gm\_\_ uint32\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

void load\_gm\_to\_cb(\_\_cb\_\_ uint8\_t *dst, \_\_gm\_\_ uint8\_t *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

// void * 为 s4

void load\_gm\_to\_cb\_s4(\_\_cb\_\_ void *dst, \_\_gm\_\_ void *src, uint16\_t baseIdx, uint8\_t repeat, uint16\_t srcStride, uint16\_t dstGap, uint8\_t sid, \_\_cce\_scalar::addr\_cal\_mode\_t addr\_cal\_mode);

参数含义见表 1 矩阵输入搬运参数说明。

PIPE\_MTE2
