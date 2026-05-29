# GetAsinhTmpBufferFactorSize

> **Section**: 6.2.4.1.18.3  
> **PDF Pages**: 2095–2095  

---

<!-- page 2095 -->

参数名输入/输出

功能

isReuseSource

输入是否复用源操作数输入的空间，与Asinh接口一致。

maxValue输出Asinh接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Asinh接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetAsinhMaxMinTmpSize(shape, 2, false, maxValue, minValue);

## 6.2.4.1.18.3 GetAsinhTmpBufferFactorSize

功能说明

kernel侧Asinh接口的计算需要开发者预留/申请临时空间，最大临时空间（maxTmpBuffer）和输入所占空间（inputSize * typeSize）存在以下关系：

**maxTmpBuffer = maxLiveNodeCount * inputSize * typeSize + extraBuffer**

其中maxLiveNodeCount表示最大临时空间是输入所占空间的多少倍；extraBuffer表示使用的额外临时空间大小。

该接口用于获取maxLiveNodeCount和extraBuffer，在固定空间大小的情况下，通过maxLiveNodeCount和extraBuffer可以推算算子单次最大计算元素数量；另外，接口获取的maxLiveNodeCount值可能为0，计算时需要判断该值非0，避免除零错误。
