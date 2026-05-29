# GetBitwiseXorTmpBufferFactorSize

> **Section**: 6.2.4.1.47.3  
> **PDF Pages**: 2245–2245  

---

<!-- page 2245 -->

参数名输入/输出

功能

minValue输出BitwiseXor接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;auto plat = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());AscendC::GetBitwiseXorMaxMinTmpSize(plat, shape, 2, false, maxValue, minValue);

## 6.2.4.1.47.3 GetBitwiseXorTmpBufferFactorSize

功能说明

该接口用于获取maxLivedNodeCount和extraBuf，在固定空间大小的情况下，通过maxLivedNodeCount和extraBuf可以推算算子单次最大计算元素数量。maxLivedNodeCount表示临时空间是单次计算数据量所占空间的多少倍；extraBuf表示使用的额外临时空间大小。

推算示例如下：

●算子实现需要调用BitwiseXor接口，开发者为其预留currBuff大小的空间，利用GetBitwiseXorTmpBufferFactorSize接口得到maxLivedNodeCount、extraBuf输出值，可推导算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuf) / maxLivedNodeCount / typeSize**

●算子实现需要调用两个kernel侧API KernelIntf1、KernelIntf2，利用两个GetXxxTmpBufferFactorSize（其中Xxx为需要调用的两个高阶API）接口的两组输出值(maxLivedNodeCount、extraBuf)以及当前现有的临时空间，推导单次最大计算元素数量currentShapeSize为：

**currentShapeSize1 = (currBuff - extraBuf1) / maxLivedNodeCount1 /typeSize**

**currentShapeSize2 = (currBuff - extraBuf2) / maxLivedNodeCount2 /typeSize**

**currentShapeSize = min(currentShapeSize1, currentShapeSize2)**
