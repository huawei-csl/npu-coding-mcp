# GetMeanTmpBufferFactorSize

> **Section**: 6.2.4.6.2.3  
> **PDF Pages**: 2737–2737  

---

<!-- page 2737 -->

接口输入/输出

功能

maxSize输出Mean接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。

说明

maxSize仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minSize输出Mean接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。

返回值说明

无

约束说明

无

调用示例

// 算子输入的数据类型T为half，accType为float，isReuseSource传入默认值falseuint32_t n = 3;uint32_t srcTypeSize = 2;uint32_t accTypeSize = 4;uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetMeanMaxMinTmpSize(n, srcTypeSize, accTypeSize, false, maxValue, minValue);

## 6.2.4.6.2.3 GetMeanTmpBufferFactorSize

功能说明

该接口用于获取maxLiveNodeCnt和extraBuf，在固定空间大小的情况下，通过maxLiveNodeCnt和extraBuf可以推算算子单次最大计算元素数量。maxLiveNodeCnt表示临时空间是单次计算数据量所占空间的多少倍；extraBuf表示使用的额外临时空间大小。

推算示例如下：

●算子实现需要调用Mean接口，开发者为其预留currBuff大小的空间，利用GetMeanTmpBufferFactorSize接口得到maxLiveNodeCnt、extraBuf输出值，可推导算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuf) / maxLiveNodeCnt / typeSize**

●算子实现需要调用两个kernel侧API KernelIntf1、KernelIntf2，利用两个GetXxxTmpBufferFactorSize（其中Xxx为需要调用的两个高阶API）接口的两组输出值(maxLiveNodeCnt、extraBuf)以及当前现有的临时空间，推导单次最大计算元素数量currentShapeSize为：

**currentShapeSize1 = (currBuff - extraBuf1) / maxLiveNodeCnt1 / typeSize**

**currentShapeSize2 = (currBuff - extraBuf2) / maxLiveNodeCnt2 / typeSize**
