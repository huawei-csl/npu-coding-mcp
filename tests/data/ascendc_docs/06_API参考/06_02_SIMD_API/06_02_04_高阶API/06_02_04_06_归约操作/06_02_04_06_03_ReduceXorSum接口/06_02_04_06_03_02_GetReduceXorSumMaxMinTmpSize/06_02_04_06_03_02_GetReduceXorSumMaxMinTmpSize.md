# GetReduceXorSumMaxMinTmpSize

> **Section**: 6.2.4.6.3.2  
> **PDF Pages**: 2741–2741  

---

<!-- page 2741 -->

返回值说明

无

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●calCount需要保证小于或等于src0Tensor和src1Tensor的元素范围。

●当最终计算结果超出int16范围[-32768，32767]后，将输出-32768 或者 32767。

●对于Atlas 推理系列产品AI Core，中间计算数据会采用half类型存储，最终计算结果的误差相对于其他处理器较大。

调用示例

// 模板参数：操作数的数据类型为int16，false代表不允许修改源操作数// dstLocal输出数据的tensor，src0Local源操作数0，src1Local源操作数1// sharedTmpBuffer临时缓存，32个元素参与计算AscendC::ReduceXorSum<int16_t, false>(dstLocal, src0Local, src1Local, sharedTmpBuffer, 32);

结果示例如下：输入输出的数据类型为int16_t输入数据(src0Local): [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]输入数据(src1Local): [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]

输出数据(dstLocal): [32 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0] // 仅32为有效值

## 6.2.4.6.3.2 GetReduceXorSumMaxMinTmpSize

功能说明

kernel侧ReduceXorSum接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小。

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。该接口最大临时空间当前等于最小临时空间。

函数原型

```cpp
void GetReduceXorSumMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-1259接口参数列表

接口输入/输出

功能

srcShape输入输入的shape信息。
