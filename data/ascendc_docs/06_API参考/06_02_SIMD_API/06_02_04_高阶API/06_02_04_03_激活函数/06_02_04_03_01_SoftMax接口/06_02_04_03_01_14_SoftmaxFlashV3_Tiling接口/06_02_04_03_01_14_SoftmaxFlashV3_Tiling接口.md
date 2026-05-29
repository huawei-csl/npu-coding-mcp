# SoftmaxFlashV3 Tiling接口

> **Section**: 6.2.4.3.1.14  
> **PDF Pages**: 2528–2529  

---

<!-- page 2528 -->

功能

接口输入/输出

isBasicBlock

是否要使能基本块计算。isBasicBlock参数可以通过isBasicBlockInSoftmax接口获取，与kernel侧接口的模板参数保持一致，默认false。注意，若kernel侧API使能模板参数SoftmaxConfig，即shape常量化场景，isBasicBlock参数必须通过接口isBasicBlockInSoftmax获取。

输入

isFlashOutputBrc

是否使能输出shape的非拓展模式。非拓展模式为不对输出数据做Broadcast，输出shape为(m, 1)。参数取值如下：

输入

●false：不使能非拓展模式，默认值。输出为float数据类型时，shape为(m，8)；输出为half数据类型时，shape为(m,16)。

●true：使能非拓展模式，输出的shape均为(m, 1)。该参数取值为true时，kernel接口的模板参数SoftmaxConfig中的mode必须配置为SoftmaxMode::SOFTMAX_OUTPUT_WITHOUT_BRC。

softmaxFlashTiling

输出SoftmaxFlashV2接口所需的tiling信息，支持optiling::SoftMaxTiling形式入参和AscendC::tiling::SoftMaxTiling形式入参。

输出

返回值说明

GetSoftMaxFlashV2MinTmpSize返回SoftmaxFlashV2接口能完成计算所需最小临时空间大小，单位为Byte。

GetSoftMaxFlashV2MaxTmpSize返回SoftmaxFlashV2接口能完成计算所需最大临时空间大小，单位为Byte。

约束说明

无

## 6.2.4.3.1.14 SoftmaxFlashV3 Tiling 接口

功能说明

用于获取SoftmaxFlashV3接口所需的Tiling参数。

函数原型

●获取Kernel接口计算所需最小/最大临时空间的接口void GetSoftMaxFlashV3MaxMinTmpSize(const ge::Shape& srcShape, const uint32_t dataTypeSize1, const uint32_t dataTypeSize2, uint32_t& maxValue, uint32_t& minValue, const bool isUpdate, const bool isBasicBlock = false)

●Tiling计算接口

–AscendC::optiling命名空间下的计算接口

<!-- page 2529 -->

```cpp
void SoftMaxFlashV3TilingFunc(const ge::Shape& srcShape, const uint32_t dataTypeSize1, const uint32_t dataTypeSize2,const uint32_t localWorkSpaceSize, optiling::SoftMaxTiling& softmaxFlashV3Tiling, const bool isUpdate,const bool isBasicBlock = false)
```

–AscendC命名空间下的计算接口void SoftMaxFlashV3TilingFunc(const ge::Shape& srcShape, const uint32_t dataTypeSize1, const uint32_t dataTypeSize2,const uint32_t localWorkSpaceSize, AscendC::tiling::SoftMaxTiling& softmaxFlashV3Tiling, const bool isUpdate,const bool isBasicBlock = false)

参数说明

表6-1139 GetSoftMaxFlashV3MaxMinTmpSize 接口参数列表

功能

接口输入/输出

srcShape输入

输入srcTensor的shape信息。

dataTypeSize1

输入srcTensor的数据类型大小，即对应SoftMaxFlashV3Kernel函数中模板参数T的数据类型大小。当前模板参数T仅支持half类型，故此参数只支持取值为2。

输入

dataTypeSize2

输入inMeanTensor、inExpSumTensor、inMaxTensor的数据类型大小，即对应SoftMaxFlashV3 Kernel函数中模板参数U的数据类型大小。当前模板参数U仅支持float类型，故此参数只支持取值为4。

输入

maxValue输出

SoftMaxFlashV3接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出

SoftMaxFlashV3接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

isUpdate输入

是否使能SoftMaxFlashV3 update为true的公式计算。该参数取值与SoftmaxFlashV3 Kernel接口的模板参数isUpdate保持一致。

isBasicBlock

预留参数，暂未启用，必须使用默认值false。

输入
