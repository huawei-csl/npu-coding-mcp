# LogSoftMax Tiling

> **Section**: 6.2.4.3.2.2  
> **PDF Pages**: 2537–2537  

---

<!-- page 2537 -->

```cpp
-0.7193291 ] [ -3.022131    -2.8049836   -2.3706892   -1.9363947   -1.5021002   -1.0678058   -0.6335113   -0.1992168 ] [-30.834908   -30.400614   -28.229141   -26.057669   -21.714724   -13.028834    -8.685889     0.        ]]
```

## 6.2.4.3.2.2 LogSoftMax Tiling

功能说明

kernel侧LogSoftMax接口的计算需要开发者预留/申请临时空间，以下接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小，并调用LogSoftMaxTilingFunc函数获取reduceSize，splitSize等参数，作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

●获取Kernel接口计算所需最大/最小临时空间的接口uint32_t GetLogSoftMaxMaxTmpSize(const ge::Shape srcShape, const uint32_t dataTypeSize, const bool isReuseSource)uint32_t GetLogSoftMaxMinTmpSize(const ge::Shape srcShape, const uint32_t dataTypeSize, const bool isReuseSource)

●Tiling计算接口void LogSoftMaxTilingFunc(const ge::Shape srcShape, const uint32_t dataTypeSize, const uint32_t localWorkSpaceSize, optiling::LogSoftMaxTiling& softmaxTiling)void LogSoftMaxTilingFunc(const ge::Shape srcShape, const uint32_t dataTypeSize, const uint32_t localWorkSpaceSize, AscendC::tiling::LogSoftMaxTiling& softmaxTiling)

参数说明

表6-1144 GetLogSoftMaxMaxTmpSize/GetLogSoftMaxMinTmpSize 接口参数列表

接口输入/输出

功能

srcShape输入输入的shape信息。

dataTypeSize

输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入是否复用源操作数输入的空间，与LogSoftMax接口一致。

表6-1145 LogSoftMaxTilingFunc 接口参数列表

接口输入/输出

功能

srcShape输入输入的shape信息。
