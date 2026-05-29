# GetDigammaMaxMinTmpSize

> **Section**: 6.2.4.1.27.2  
> **PDF Pages**: 2144–2145  

---

<!-- page 2144 -->

参数名输入/输出

描述

srcTensor输入源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

源操作数的数据类型需要与目的操作数保持一致。

sharedTmpBuffer

输入临时缓存。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

用于Digamma内部复杂计算时存储中间变量，由开发者提供。

临时空间大小BufferSize的获取方式请参考GetDigammaMaxMinTmpSize。

calCount输入参与计算的元素个数。

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。

// dstLocal：输出Tensor// srcLocal：输入Tensor// sharedTmpBuffer：临时空间// 输入tensor长度为1024, 算子输入的数据类型为float, 实际计算个数为前1024AscendC::Digamma<float, false>(dstLocal, srcLocal, sharedTmpBuffer, 1024);

结果示例如下：输入数据(srcLocal): [5.3675685 0.26528683 -2.872628 ... 2.9387941 9.001339]输出数据(dstLocal): [1.5843406 -3.978809 -6.2081366 ... 0.8983184 2.1407988]

## 6.2.4.1.27.2 GetDigammaMaxMinTmpSize

功能说明

kernel侧Digamma接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

<!-- page 2145 -->

函数原型

```cpp
void GetDigammaMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-929参数列表

参数名输入/输出

功能

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入是否复用源操作数输入的空间，与Digamma接口一致。

maxValue输出Digamma接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Digamma接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;uint32_t typeSize = sizeof(half);

**AscendC::GetDigammaMaxMinTmpSize(shape, typeSize, false, maxValue, minValue);**
