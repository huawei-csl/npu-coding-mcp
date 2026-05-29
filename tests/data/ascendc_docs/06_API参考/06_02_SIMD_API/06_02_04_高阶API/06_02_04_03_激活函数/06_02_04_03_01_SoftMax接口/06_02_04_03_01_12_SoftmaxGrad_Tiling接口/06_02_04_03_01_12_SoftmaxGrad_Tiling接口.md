# SoftmaxGrad Tiling接口

> **Section**: 6.2.4.3.1.12  
> **PDF Pages**: 2524–2525  

---

<!-- page 2524 -->

功能

接口输入/输出

softmaxFlashTiling

输出SoftmaxFlash接口所需的tiling信息，支持optiling::SoftMaxTiling形式入参和AscendC::tiling::SoftMaxTiling形式入参。

输出

返回值说明

GetSoftMaxFlashMaxTmpSize返回SoftmaxFlash接口能完成计算所需最大临时空间大小，单位为Byte。

GetSoftMaxFlashMinTmpSize返回SoftmaxFlash接口能完成计算所需最小临时空间大小，单位为Byte。

约束说明

无

## 6.2.4.3.1.12 SoftmaxGrad Tiling 接口

功能说明

用于获取SoftmaxGrad Tiling参数。

函数原型

●获取Kernel接口计算所需最小/最大临时空间的接口uint32_t GetSoftMaxGradMaxTmpSize(const ge::Shape& srcShape, const uint32_t dataTypeSize, const bool isFront, const bool isReuseSource)uint32_t GetSoftMaxGradMinTmpSize(const ge::Shape& srcShape, const uint32_t dataTypeSize, const bool isFront, const bool isReuseSource)

●Tiling计算接口

–AscendC::optiling命名空间下的计算接口void SoftMaxGradTilingFunc(const ge::Shape& srcShape, const uint32_t dataTypeSize, const uint32_t localWorkSpaceSize, optiling::SoftMaxTiling& softmaxGradTiling, const bool isFront = false)

–AscendC命名空间下的计算接口void SoftMaxGradTilingFunc(const ge::Shape& srcShape, const uint32_t dataTypeSize, const uint32_t localWorkSpaceSize, AscendC::tiling::SoftMaxTiling& softmaxGradTiling, const bool isFront = false)

<!-- page 2525 -->

参数说明

表6-1135 SoftmaxGrad GetSoftMaxGradMaxTmpSize/GetSoftMaxGradMinTmpSize 接口参数列表

接口输入/输出

功能

srcShape输入

输入srcTensor的shape信息。

dataTypeSize

计算的数据类型，比如half=2。

输入

isFront输入

![p2525_img001.png](../../../../images/p2525_img001.png)

，和kernel侧的SoftmaxGrad接口一致，默认false。

是否只计算

isReuseSource

与kernel侧接口配置保持一致。

输入

表6-1136 SoftmaxGrad SoftMaxGradTilingFunc 接口参数列表

接口输入/输出

功能

srcShape输入

输入srcTensor的shape信息。

localWorkSpaceSize

剩余的可供SoftmaxGrad接口计算的临时空间大小，单位为Byte。localWorkSpaceSize的取值必须大于GetSoftMaxGradMinTmpSize接口返回的计算所需的最小临时空间大小。

输入

dataTypeSize

计算的数据类型，比如half=2。

输入

isFront输入

[IMAGE_1]

，和kernel侧的SoftmaxGrad接口一致，默认false。

是否只计算

softmaxGradTiling

输出SoftmaxGrad接口所需的tiling信息，支持optiling::SoftMaxTiling形式入参和AscendC::tiling::SoftMaxTiling形式入参。

输出
