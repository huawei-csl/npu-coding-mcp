# UnaryRepeatParams

> **Section**: 6.2.6.4  
> **PDF Pages**: 3093–3093  

---

<!-- page 3093 -->

功能说明

将数据指针置于GlobalTensor中并返回该GlobalTensor。

函数原型

```cpp
GlobalTensor<T> GetDataObj()
```

参数说明

无

返回值说明

返回设置了数据指针的GlobalTensor。

约束说明

无

## 6.2.6.4 UnaryRepeatParams

UnaryRepeatParams为用于控制操作数地址步长的数据结构。结构体内包含操作数相邻迭代间相同DataBlock的地址步长，操作数同一迭代内不同DataBlock的地址步长等参数。

相邻迭代间的地址步长参数说明请参考repeatStride；同一迭代内DataBlock的地址步长参数说明请参考dataBlockStride。

结构体具体定义为：

```cpp
const int32_t DEFAULT_BLK_NUM = 8;const int32_t DEFAULT_BLK_STRIDE = 1;const uint8_t DEFAULT_REPEAT_STRIDE = 8;
struct UnaryRepeatParams {    __aicore__ UnaryRepeatParams() {}    __aicore__ UnaryRepeatParams(const uint16_t dstBlkStrideIn, const uint16_t srcBlkStrideIn,        const uint8_t dstRepStrideIn, const uint8_t srcRepStrideIn)        : dstBlkStride(dstBlkStrideIn),          srcBlkStride(srcBlkStrideIn),          dstRepStride(dstRepStrideIn),          srcRepStride(srcRepStrideIn)    {}    __aicore__ UnaryRepeatParams(const uint16_t dstBlkStrideIn, const uint16_t srcBlkStrideIn,        const uint8_t dstRepStrideIn, const uint8_t srcRepStrideIn, const bool halfBlockIn)        : dstBlkStride(dstBlkStrideIn),          srcBlkStride(srcBlkStrideIn),          dstRepStride(dstRepStrideIn),          srcRepStride(srcRepStrideIn),          halfBlock(halfBlockIn)    {}    uint32_t blockNumber = DEFAULT_BLK_NUM;
    uint16_t dstBlkStride = DEFAULT_BLK_STRIDE;
    uint16_t srcBlkStride = DEFAULT_BLK_STRIDE;
    uint8_t dstRepStride = DEFAULT_REPEAT_STRIDE;
    uint8_t srcRepStride = DEFAULT_REPEAT_STRIDE;
    bool repeatStrideMode = false;
    bool strideSizeMode = false;
```
