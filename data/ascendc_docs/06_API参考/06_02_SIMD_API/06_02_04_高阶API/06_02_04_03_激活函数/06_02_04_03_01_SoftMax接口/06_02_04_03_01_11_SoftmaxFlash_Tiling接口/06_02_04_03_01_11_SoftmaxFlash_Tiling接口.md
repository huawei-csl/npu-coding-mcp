# SoftmaxFlash Tiling接口

> **Section**: 6.2.4.3.1.11  
> **PDF Pages**: 2522–2523  

---

<!-- page 2522 -->

接口输入/输出

功能

isReuseSource

输入与kernel侧接口配置保持一致。

表6-1132 SoftMax/SimpleSoftMax SoftMaxTilingFunc 接口参数列表

接口输入/输出

功能

srcShape输入输入srcTensor的shape信息。

dataTypeSize

输入参与计算的max和sum的数据类型，比如half=2。

localWorkSpaceSize

输入剩余的可供SoftMax接口计算的空间大小，单位为Byte。localWorkSpaceSize的取值必须大于GetSoftMaxMinTmpSize接口返回的计算所需的最小临时空间大小。

softmaxTiling

输出输出SoftMax接口所需的tiling信息，支持optiling::SoftMaxTiling形式入参和AscendC::tiling::SoftMaxTiling形式入参。

返回值说明

GetSoftMaxMaxTmpSize返回SoftMax/SimpleSoftMax接口能完成计算所需最大临时空间大小，单位为Byte。

GetSoftMaxMinTmpSize返回SoftMax/SimpleSoftMax接口能完成计算所需最小临时空间大小，单位为Byte。

约束说明

无

## 6.2.4.3.1.11 SoftmaxFlash Tiling 接口

功能说明

注意：该接口后续即将废弃，新开发内容不要使用该接口。

用于获取SoftmaxFlash Tiling参数。

函数原型

●获取Kernel接口计算所需最小/最大临时空间的接口uint32_t GetSoftMaxFlashMaxTmpSize(const ge::Shape& srcShape, const uint32_t dataTypeSize, const bool isUpdate, const bool isReuseSource)uint32_t GetSoftMaxFlashMinTmpSize(const ge::Shape& srcShape, const uint32_t dataTypeSize, const bool isUpdate, const bool isReuseSource)

<!-- page 2523 -->

●Tiling计算接口

–AscendC::optiling命名空间下的计算接口void SoftMaxFlashTilingFunc(const ge::Shape& srcShape, const uint32_t dataTypeSize, const uint32_t localWorkSpaceSize, optiling::SoftMaxTiling& softmaxFlashTiling, const bool isUpdate = false)

–AscendC命名空间下的计算接口void SoftMaxFlashTilingFunc(const ge::Shape& srcShape, const uint32_t dataTypeSize, const uint32_t localWorkSpaceSize, AscendC::tiling::SoftMaxTiling& softmaxFlashTiling, const bool isUpdate = false)

参数说明

表6-1133 SoftmaxFlash GetSoftMaxFlashMaxTmpSize/GetSoftMaxFlashMinTmpSize 接口参数列表

功能

接口输入/输出

srcShape输入

输入srcTensor的shape信息。

dataTypeSize

参与计算的maxTensor和sumTensor的数据类型，比如half=2。

输入

isUpdate输入

是否使能刷新功能，和kernel侧SoftmaxFlash接口一致，默认false。

isReuseSource

与kernel侧接口配置保持一致。

输入

表6-1134 SoftmaxFlash SoftMaxFlashTilingFunc 接口参数列表

接口输入/输出

功能

srcShape输入

输入srcTensor的shape信息。

dataTypeSize

参与计算的maxTensor和sumTensor的数据类型，比如half=2。

输入

localWorkSpaceSize

剩余的可供SoftmaxFlash接口计算的空间大小，单位为Byte。localWorkSpaceSize的取值必须大于GetSoftMaxFlashMinTmpSize接口返回的计算所需的最小临时空间大小。

输入

isUpdate输入

是否使能刷新功能，和kernel侧SoftmaxFlash接口一致，默认false。
