# BinaryRepeatParams

> **Section**: 6.2.6.5  
> **PDF Pages**: 3094–3094  

---

<!-- page 3094 -->

```cpp
bool halfBlock = false;};
```

其中，blockNumber，repeatStrideMode，strideSizeMode为保留参数，用户无需关心，使用默认值即可。halfBlock表示CastDeq指令的结果写入对应UB的上半（halfBlock = true）还是下半（halfBlock = false）部分。用户需要自行定义DataBlock Stride参数，包含dstBlkStride，srcBlkStride，以及Repeat Stride参数，包含dstRepStride，srcRepStride。

## 6.2.6.5 BinaryRepeatParams

BinaryRepeatParams为用于控制操作数地址步长的数据结构。结构体内包含操作数相邻迭代间相同DataBlock的地址步长，操作数同一迭代内不同DataBlock的地址步长等参数。

相邻迭代间的地址步长参数说明请参考repeatStride；同一迭代内DataBlock的地址步长参数说明请参考dataBlockStride。

结构体具体定义为：

```cpp
const int32_t DEFAULT_BLK_NUM = 8;const int32_t DEFAULT_BLK_STRIDE = 1;const uint8_t DEFAULT_REPEAT_STRIDE = 8;
struct BinaryRepeatParams {    __aicore__ BinaryRepeatParams() {}    __aicore__ BinaryRepeatParams(const uint8_t dstBlkStrideIn, const uint8_t src0BlkStrideIn,        const uint8_t src1BlkStrideIn, const uint8_t dstRepStrideIn, const uint8_t src0RepStrideIn,        const uint8_t src1RepStrideIn)        : dstBlkStride(dstBlkStrideIn),          src0BlkStride(src0BlkStrideIn),          src1BlkStride(src1BlkStrideIn),          dstRepStride(dstRepStrideIn),          src0RepStride(src0RepStrideIn),          src1RepStride(src1RepStrideIn)    {}    uint32_t blockNumber = DEFAULT_BLK_NUM;
    uint8_t dstBlkStride = DEFAULT_BLK_STRIDE;
    uint8_t src0BlkStride = DEFAULT_BLK_STRIDE;
    uint8_t src1BlkStride = DEFAULT_BLK_STRIDE;
    uint8_t dstRepStride = DEFAULT_REPEAT_STRIDE;
    uint8_t src0RepStride = DEFAULT_REPEAT_STRIDE;
    uint8_t src1RepStride = DEFAULT_REPEAT_STRIDE;
    bool repeatStrideMode = false;
    bool strideSizeMode = false;};
```

其中，blockNumber，repeatStrideMode和strideSizeMode为保留参数，用户无需关心，使用默认值即可。用户需要自行定义DataBlock Stride参数，包含dstBlkStride，src0BlkStride和src1BlkStride，以及Repeat Stride参数，包含dstRepStride，src0RepStride和src1RepStride。

## 6.2.6.6 complex32/complex64

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x
