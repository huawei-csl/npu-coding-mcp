# GetAscendDequantTmpBufferFactorSize

> **Section**: 6.2.4.5.6  
> **PDF Pages**: 2687–2687  

---

<!-- page 2687 -->

约束说明

无

调用示例

// 输入shape信息为(2,1024)// AscendDequant接口中传入的dequantParams中m = 2, n = 1024;算子输入的数据类型为int32_tstd::vector<int64_t> shape_vec = {2, 1024};ge::Shape srcShape(shape_vec);uint32_t typeSize = 4;uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetAscendDequantMaxMinTmpSize(srcShape, typeSize, maxValue, minValue);

## 6.2.4.5.6 GetAscendDequantTmpBufferFactorSize

功能说明

该接口用于获取maxLiveNodeCount和extraBuf，在固定空间大小的情况下，通过maxLiveNodeCount和extraBuf可以推算算子单次最大计算元素数量。maxLiveNodeCount表示临时空间是单次计算数据量所占空间的多少倍；extraBuf表示使用的额外临时空间大小。

推算示例如下：

●算子实现需要调用AscendDequant接口，开发者为其预留currBuff大小的空间，利用GetAscendDequantTmpBufferFactorSize接口得到maxLiveNodeCount、extraBuf输出值，可推导算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuf) / maxLiveNodeCount / typeSize**

●算子实现需要调用两个kernel侧API KernelIntf1、KernelIntf2，利用两个GetXxxTmpBufferFactorSize（其中Xxx为需要调用的两个高阶API）接口的两组输出值(maxLiveNodeCount、extraBuf)以及当前现有的临时空间，推导单次最大计算元素数量currentShapeSize为：

**currentShapeSize1 = (currBuff - extraBuf1) / maxLiveNodeCount1 /typeSize**

**currentShapeSize2 = (currBuff - extraBuf2) / maxLiveNodeCount2 /typeSize**

**currentShapeSize = min(currentShapeSize1, currentShapeSize2)**

注意上文中的currBuff表示接口计算可用的空间，需要去除用户输入输出等空间；另外，接口获取的maxLiveNodeCount值可能为0，计算时需要判断该值非0，避免除零错误。

函数原型

```cpp
void GetAscendDequantTmpBufferFactorSize(const ge::Shape& srcShape, uint32_t& maxLiveNodeCount, uint32_t& extraBuf)
```
