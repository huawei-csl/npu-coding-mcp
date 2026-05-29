# GetAntiQuantizeTmpBufferFactorSize

> **Section**: 6.2.4.5.18  
> **PDF Pages**: 2726–2726  

---

<!-- page 2726 -->

```cpp
bool isTranspose = false;AscendC::GetAntiQuantizeMaxMinTmpSize(srcShape, scaleShape, isTranspose, ge::DT_INT8, ge::DT_BF16, maxValue, minValue);
```

## 6.2.4.5.18 GetAntiQuantizeTmpBufferFactorSize

功能说明

该接口用于获取maxLiveNodeCount和extraBuf，在固定空间大小的情况下，通过maxLiveNodeCount和extraBuf可以推算算子单次最大计算元素数量。maxLiveNodeCount表示临时空间是单次计算数据量所占空间的多少倍；extraBuf表示使用的额外临时空间大小。

推算示例如下：

●算子实现需要调用AntiQuantize接口，开发者为其预留currBuff大小的空间，利用GetAntiQuantizeTmpBufferFactorSize接口得到maxLiveNodeCount、extraBuf输出值，可推导算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuf) / maxLiveNodeCount / typeSize**

●算子实现需要调用两个kernel侧API KernelIntf1、KernelIntf2，利用两个GetXxxTmpBufferFactorSize（其中Xxx为需要调用的两个高阶API）接口的两组输出值(maxLiveNodeCount、extraBuf)以及当前现有的临时空间，推导单次最大计算元素数量currentShapeSize为：

**currentShapeSize1 = (currBuff - extraBuf1) / maxLiveNodeCount1 /typeSize**

**currentShapeSize2 = (currBuff - extraBuf2) / maxLiveNodeCount2 /typeSize**

**currentShapeSize = min(currentShapeSize1, currentShapeSize2)**

注意上文中的currBuff表示接口计算可用的空间，需要去除用户输入输出等空间；另外，接口获取的maxLiveNodeCount值可能为0，计算时需要判断该值非0，避免除零错误。

函数原型

```cpp
void GetAntiQuantizeTmpBufferFactorSize(const ge::Shape& srcShape, const ge::Shape& scaleShape, ge::DataType inputDataType, ge::DataType outputDataType, uint32_t& maxLiveNodeCount, uint32_t& extraBuf)
```

参数说明

表6-1249参数列表

参数名输入/输出

功能

srcShape输入输入srcTensor的shape信息。

scaleShape输入输入scale的shape信息。

inputDataType

输入输入数据类型。ge::DataType类型。
