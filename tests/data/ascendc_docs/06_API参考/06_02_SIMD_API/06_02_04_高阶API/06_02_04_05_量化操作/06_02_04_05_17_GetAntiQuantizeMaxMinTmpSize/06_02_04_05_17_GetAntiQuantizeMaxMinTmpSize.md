# GetAntiQuantizeMaxMinTmpSize

> **Section**: 6.2.4.5.17  
> **PDF Pages**: 2724–2725  

---

<!-- page 2724 -->

调用示例

●PER_CHANNEL、PER_TOKEN、PER_GROUP模式constexpr static AntiQuantizePolicy tokenPolicy = AntiQuantizePolicy::PER_TOKEN;constexpr static AntiQuantizePolicy channelPolicy = AntiQuantizePolicy::PER_CHANNEL;constexpr static AntiQuantizePolicy groupPolicy = AntiQuantizePolicy::PER_GROUP;// 此处以PER_TOKEN模式为例，使能offset；kDim仅PER_GROUP场景有效，表示group计算方向为n方向constexpr static AntiQuantizeConfig config = {tokenPolicy, true, 1};AntiQuantizeParams params;// m,n为外部传入参数，表示srcLocal实际参与的m、n方向的元素个数params.m = m;params.n = n;params.groupSize = n; // 仅PER_GROUP场景有效，此处表示n方向所有元素共享一组scale和offset// srcLocal为int8_t类型的LocalTensor，dstLocal、scale、offset为half类型的LocalTensorAntiQuantize<config>(dstLocal, srcLocal, scale, offset, params);

●PER_TENSOR模式constexpr static AntiQuantizePolicy tensorPolicy = AntiQuantizePolicy::PER_TENSOR;// 使能offsetconstexpr static AntiQuantizeConfig config = {tensorPolicy, true, -1};AntiQuantizeParams params;// m,n为外部传入参数，表示srcLocal实际参与的m、n方向的元素个数params.m = m;params.n = n;params.groupSize = 0; // 仅PER_GROUP场景有效// srcLocal为int8_t类型的LocalTensor，dstLocal为half类型的LocalTensor，scale、offset为half类型的标量AntiQuantize<config>(dstLocal, srcLocal, scale, offset, params);

结果示例如下：

输入数据（srcLocal）: [-4, 2, -2, -3, -1, -4, 1, 3, 4, 1, -2, 0, ... 1]输入数据（scale矢量）: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ... 1]输入数据（scale标量）:[1]输入数据（offset矢量）: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ... 0]输入数据（offset标量）: [0]输出数据（dstLocal），此时dstLocal = srcLocal: [-4, 2, -2, -3, -1, -4, 1, 3, 4, 1, -2, 0, ... 1]

## 6.2.4.5.17 GetAntiQuantizeMaxMinTmpSize

功能说明

kernel侧AntiQuantize接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetAntiQuantizeMaxMinTmpSize(const ge::Shape& srcShape, const ge::Shape& scaleShape, bool isTranspose, ge::DataType inputDataType, ge::DataType outputDataType, uint32_t& maxValue, uint32_t& minValue)
```

<!-- page 2725 -->

参数说明

表6-1248接口参数列表

参数名输入/输出

描述

srcShape输入

AntiQuantize接口的输入srcTensor的shape信息。

scaleShape输入

AntiQuantize接口的输入scale的shape信息。

isTranspose输入

预留参数。当前仅支持配置为false。

inputDataType

输入srcTensor数据类型。

输入

outputDataType

输出dstTensor数据类型。

输入

maxValue输出

AntiQuantize接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出

AntiQuantize接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

```cpp
uint32_t maxValue = 0;uint32_t minValue = 0;std::vector<int64_t> srcDims = { 64, 512 };auto srcShape = ge::Shape(srcDims);std::vector<int64_t> scaleDims = { 1, 512 };auto scaleShape = ge::Shape(scaleDims);
```
