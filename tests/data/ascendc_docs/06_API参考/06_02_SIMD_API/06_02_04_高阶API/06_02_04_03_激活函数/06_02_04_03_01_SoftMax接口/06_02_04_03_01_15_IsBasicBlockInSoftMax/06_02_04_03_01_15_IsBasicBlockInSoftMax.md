# IsBasicBlockInSoftMax

> **Section**: 6.2.4.3.1.15  
> **PDF Pages**: 2530–2530  

---

<!-- page 2530 -->

表6-1140 SoftMaxFlashV3TilingFunc 接口参数列表

功能

接口输入/输出

srcShape输入

输入srcTensor的shape信息。

dataTypeSize1输入

输入srcTensor的数据类型大小，即对应SoftMaxFlashV3Kernel函数中模板参数T的数据类型大小。当前模板参数T仅支持half类型，故此参数只支持取值为2。

dataTypeSize2输入

输入inMeanTensor、inExpSumTensor、inMaxTensor的数据类型大小，即对应SoftMaxFlashV3 Kernel函数中模板参数U的数据类型大小。当前模板参数U仅支持float类型，故此参数只支持取值为4。

localWorkSpaceSize

剩余的可供SoftmaxFlashV3接口计算的空间大小。localWorkSpaceSize的取值必须大于GetSoftMaxFlashV3MaxMinTmpSize接口返回的计算所需的最小临时空间大小。

输入

isUpdate输入

是否使能SoftMaxFlashV3 update为true的公式计算。与SoftmaxFlashV3 Kernel接口的模板参数isUpdate保持一致。

isBasicBlock输入

预留参数，暂未启用，必须使用默认值false。

softmaxFlashV3Tiling

输出SoftMaxFlashV3接口所需的Tiling信息，支持optiling::SoftMaxTiling形式入参和AscendC::tiling::SoftMaxTiling形式入参。

输出

返回值说明

无

约束说明

无

## 6.2.4.3.1.15 IsBasicBlockInSoftMax

功能说明

用于判断SoftMaxTiling结构是否符合基本块特征。

函数原型

●AscendC::optiling命名空间下的计算接口bool IsBasicBlockInSoftMax(optiling::SoftMaxTiling& tiling, const uint32_t dataTypeSize = 2)
