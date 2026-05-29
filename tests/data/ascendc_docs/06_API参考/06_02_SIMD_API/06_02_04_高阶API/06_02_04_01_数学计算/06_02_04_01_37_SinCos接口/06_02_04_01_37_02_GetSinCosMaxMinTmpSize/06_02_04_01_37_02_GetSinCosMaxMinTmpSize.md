# GetSinCosMaxMinTmpSize

> **Section**: 6.2.4.1.37.2  
> **PDF Pages**: 2197–2197  

---

<!-- page 2197 -->

●接口框架申请临时空间AscendC::TPipe pipe;AscendC::TQue<AscendC::TPosition::VECCALC, 1> tmpQue;pipe.InitBuffer(tmpQue, 1, bufferSize); // bufferSize 通过Host侧tiling参数获取// 输入tensor长度为1024, 算子输入的数据类型为half, 实际计算个数为512static constexpr AscendC::SinCosConfig sincosConfig = { false };  // 不修改源操作数// dst0、dst1、src为half类型的LocalTensorAscendC::SinCos<sincosConfig, half>(dst0, dst1, src, 512);

结果示例如下：输入数据(src0):[ -360, -270, -180, -90, 0, 90, 180, 270, 360 ]输出数据(dst0):[ 0, 1, 0, -1, 0, 1, 0, -1, 0]输出数据(dst1):[ 1, 0, -1, 0, 1, 0, -1, 0, 1]

## 6.2.4.1.37.2 GetSinCosMaxMinTmpSize

功能说明

Kernel侧SinCos接口的计算需要开发者预留/申请临时空间，本接口用于在Host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到Kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，Kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetSinCosMaxMinTmpSize(const platform_ascendc::PlatformAscendC& ascendcPlatform, const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-969接口参数列表

参数名输入/输出

描述

ascendcPlatform

输入的平台信息。PlatformAscendC的定义请参见6.4.2.1.2 构造及析构函数。

输入

srcShape输入

输入的shape信息。

typeSize输入

输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

是否复用源操作数输入的空间，与SinCos接口的isReuseSource参数保持一致。对于float数据类型的输入支持开启该参数，half数据类型的输入不支持开启该参数。

输入
