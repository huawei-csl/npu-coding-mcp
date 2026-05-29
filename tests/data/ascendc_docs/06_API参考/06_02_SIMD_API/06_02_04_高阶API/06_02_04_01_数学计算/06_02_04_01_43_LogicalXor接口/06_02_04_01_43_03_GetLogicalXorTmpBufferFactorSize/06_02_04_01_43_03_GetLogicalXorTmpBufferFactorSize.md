# GetLogicalXorTmpBufferFactorSize

> **Section**: 6.2.4.1.43.3  
> **PDF Pages**: 2227–2228  

---

<!-- page 2227 -->

参数名输入/输出

功能

maxValue输出LogicalXor接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，Kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出LogicalXor接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;auto plat = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());AscendC::GetLogicalXorMaxMinTmpSize(plat, shape, 2, false, maxValue, minValue);

## 6.2.4.1.43.3 GetLogicalXorTmpBufferFactorSize

功能说明

该接口用于获取maxLivedNodeCount和extraBuf，在固定空间大小的情况下，通过maxLivedNodeCount和extraBuf可以推算算子单次最大计算元素数量。maxLivedNodeCount表示临时空间是单次计算数据量所占空间的多少倍；extraBuf表示使用的额外临时空间大小。

推算示例如下：

●算子实现需要调用LogicalXor接口，开发者为其预留currBuff大小的空间，利用GetLogicalXorTmpBufferFactorSize接口得到maxLivedNodeCount、extraBuf输出值，可推导算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuf) / maxLivedNodeCount / typeSize**

<!-- page 2228 -->

●算子实现需要调用两个kernel侧API KernelIntf1、KernelIntf2，利用两个GetXxxTmpBufferFactorSize（其中Xxx为需要调用的两个高阶API）接口的两组输出值(maxLivedNodeCount、extraBuf)以及当前现有的临时空间，推导单次最大计算元素数量currentShapeSize为：

**currentShapeSize1 = (currBuff - extraBuf1) / maxLivedNodeCount1 /typeSize**

**currentShapeSize2 = (currBuff - extraBuf2) / maxLivedNodeCount2 /typeSize**

**currentShapeSize = min(currentShapeSize1, currentShapeSize2)**

注意上文中的currBuff表示接口计算可用的空间，需要去除用户输入输出等空间；另外，接口获取的maxLivedNodeCount值可能为0，计算时需要判断该值非0，避免除零错误。

函数原型

```cpp
void GetLogicalXorTmpBufferFactorSize(const platform_ascendc::PlatformAscendC& ascendcPlatform,const uint32_t typeSize, uint32_t& maxLivedNodeCount, uint32_t& extraBuf)
```

参数说明

表6-994参数列表

参数名输入/输出

功能

ascendcPlatform

输入输入的平台信息。PlatformAscendC的定义请参见6.4.2.1.2 构造及析构函数。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

maxLivedNodeCount

输出最大存活节点数，表示临时空间是单次计算数据量所占空间的多少倍。

extraBuf输出使用的额外临时空间大小，单位为字节。

返回值说明

无

约束说明

当利用maxLivedNodeCount、extraBuf反推出的currentShapeSize * typeSize < 256B时，currentShapeSize按照256B/typeSize的值向上取整。

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。uint32_t maxLivedNodeCount = 0;uint32_t extraBuf = 0;auto plat = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());AscendC::GetLogicalXorTmpBufferFactorSize(plat, typeSize, maxLivedNodeCount, extraBuf);
