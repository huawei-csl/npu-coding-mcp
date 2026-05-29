# GetAscendAntiQuantMaxMinTmpSize

> **Section**: 6.2.4.5.8  
> **PDF Pages**: 2699–2700  

---

<!-- page 2699 -->

// sharedTmpBuffer：开发者管理的临时缓冲区，用于存放内部计算中的中间变量// k：k轴长度// shapeInfo：offsetLocal和scaleLocal张量的shape信息AscendC::AntiQuantShapeInfo shapeInfo = {1, elementCountOfOffset, 1, elementCountOfOffset};AscendC::AscendAntiQuant<InputType, OutType, false>(dstLocal, srcLocal, offsetLocal, scaleLocal, sharedTmpBuffer, k, shapeInfo);

结果示例如下：输入数据src（shape为[2,64]，非转置场景）:  [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]offset（shape为[1,64]）:  [2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]scale（shape为[1,64]）:  [3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3.]输出数据dstLocal（shape为[2,64]）:  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]

PER_TOKEN/PER_GROUP b8场景调用示例如下。

// 注意m,n需从外部传入constexpr static bool isReuseSource = false;constexpr static AscendAntiQuantConfig config = {has_offset, has_transpose, -1};constexpr static AscendAntiQuantPolicy policy = AscendAntiQuantPolicy::PER_TOKEN;AscendAntiQuantParam para;para.m = m;para.n = n;para.calCount = calCount;AscendAntiQuant<dstType, srcType, scaleType, config, policy>(dstLocal, srcLocal, scaleLocal, offsetLocal, para);

## 6.2.4.5.8 GetAscendAntiQuantMaxMinTmpSize

功能说明

kernel侧AscendAntiQuant接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetAscendAntiQuantMaxMinTmpSize(const ge::Shape& srcShape, const ge::Shape& scaleShape, bool isTranspose, ge::DataType inputDataType, ge::DataType outputDataType, uint32_t& maxValue, uint32_t& minValue)uint32_t GetAscendAntiQuantMaxTmpSize(const ge::Shape& srcShape, const ge::Shape& scaleShape, bool isTranspose, ge::DataType inputDataType, ge::DataType outputDataType)uint32_t GetAscendAntiQuantMinTmpSize(const ge::Shape& srcShape, const ge::Shape& scaleShape, bool isTranspose, ge::DataType inputDataType, ge::DataType outputDataType)
```

<!-- page 2700 -->

参数说明

表6-1233接口参数列表

参数名输入/输出

描述

srcShape输入

输入src的shape信息。

scaleShape输入

输入scale的shape信息。

isTranspose输入

是否转置。

inputDataType

输入数据类型。ge::DataType类型。

输入

outputDataType

输出数据类型。ge::DataType类型。

输入

maxValue输出

AscendAntiQuant接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出

AscendAntiQuant接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

**GetAscendAntiQuantMaxMinTmpSize：无。**

**GetAscendAntiQuantMaxTmpSize：AscendAntiQuant接口能完成计算所需的最大临时空间大小。**

**GetAscendAntiQuantMinTmpSize：AscendAntiQuant接口能完成计算所需的最小临时空间大小。**

约束说明

无
