# GetFracMaxMinTmpSize

> **Section**: 6.2.4.1.13.2  
> **PDF Pages**: 2068–2069  

---

<!-- page 2068 -->

参数名输入/输出

描述

srcTensor输入源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

源操作数的数据类型需要与目的操作数保持一致。

sharedTmpBuffer

输入临时缓存。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

用于Frac内部复杂计算时存储中间变量，由开发者提供。

临时空间大小BufferSize的获取方式请参考 GetFracMaxMinTmpSize。

calCount输入参与计算的元素个数。

返回值说明

无

约束说明

●针对Atlas 推理系列产品AI Core，输入数据限制在[-2147483647.0,2147483647.0]范围内。

●不支持源操作数与目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

完整的调用样例请参考Frac样例。

// dstLocal: 存放计算结果的Tensor// srcLocal: 参与计算的输入TensorAscendC::Frac<srcType, false>(dstLocal, srcLocal);

结果示例如下：

输入数据(srcLocal): [9.33 -8.07 -6.38 8.45 5.83 6.46 4.18 1.93]输出数据(dstLocal): [0.33 -0.07 -0.38 0.45 0.83 0.46 0.18 0.93]

## 6.2.4.1.13.2 GetFracMaxMinTmpSize

功能说明

kernel侧Frac接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

<!-- page 2069 -->

函数原型

```cpp
void GetFracMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-869接口参数列表

参数名输入/输出

功能

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入是否允许修改源操作数输入的空间。

maxValue输出Frac接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Frac接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t minValue;uint32_t maxValue;AscendC::GetFracMaxMinTmpSize(shape, 2, false, maxValue, minValue);
