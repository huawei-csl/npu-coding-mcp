# GetCeilTmpBufferFactorSize

> **Section**: 6.2.4.1.21.3  
> **PDF Pages**: 2110–2110  

---

<!-- page 2110 -->

参数名输入/输出

功能

maxValue输出Ceil接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Ceil接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetCeilMaxMinTmpSize(shape, 2, false, maxValue, minValue);

## 6.2.4.1.21.3 GetCeilTmpBufferFactorSize

功能说明

该接口用于获取maxLiveNodeCount和extraBuf，在固定空间大小的情况下，通过maxLiveNodeCount和extraBuf可以推算算子单次最大计算元素数量。maxLiveNodeCount表示临时空间是单次计算数据量所占空间的多少倍；extraBuf表示使用的额外临时空间大小。

推算示例如下：

●算子实现需要调用Ceil接口，开发者为其预留currBuff大小的空间，利用GetCeilTmpBufferFactorSize接口得到maxLiveNodeCount、extraBuf输出值，可推导算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuf) / maxLiveNodeCount / typeSize**

●算子实现需要调用两个kernel侧API KernelIntf1、KernelIntf2，利用两个GetXxxTmpBufferFactorSize（其中Xxx为需要调用的两个高阶API）接口的两组输
