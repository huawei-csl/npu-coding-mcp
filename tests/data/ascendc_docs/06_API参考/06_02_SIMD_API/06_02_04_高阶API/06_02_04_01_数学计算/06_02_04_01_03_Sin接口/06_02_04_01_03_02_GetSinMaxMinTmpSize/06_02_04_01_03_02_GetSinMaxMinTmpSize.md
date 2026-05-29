# GetSinMaxMinTmpSize

> **Section**: 6.2.4.1.3.2  
> **PDF Pages**: 2012–2012  

---

<!-- page 2012 -->

// 通过sharedTmpBuffer入参传入临时空间，部分参与计算, 需要参与计算的元素个数为512AscendC::Sin(dstLocal, srcLocal, sharedTmpBuffer, 512);constexpr AscendC::SinAlgo algo = AscendC::SinAlgo::RADIAN_REDUCTION;constexpr AscendC::SinConfig config = { algo };AscendC::Sin<half, false, config>(dstLocal, srcLocal, sharedTmpBuffer, 512);

结果示例如下：输入数据(srcLocal): [-2.56 -2.55 -2.54 ... 0. ... 2.53  2.54  2.55]输出数据(dstLocal): [-0.54889839 -0.55703507 -0.56672889 ... 0. 0.57474768 0.56672889 0.55703507]

## 6.2.4.1.3.2 GetSinMaxMinTmpSize

功能说明

kernel侧Sin接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetSinMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
void GetSinMaxMinTmpSize(const SinConfig& config, const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-829接口参数列表

参数名输入/输出

描述

config输入

该参数仅支持Atlas 350 加速卡。

Sin接口的相关配置信息。该参数的配置必须与Sin Kernel接口模板参数config的配置保持一致。

srcShape输入

输入的shape信息。

typeSize输入

输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

是否复用源操作数输入的空间，与Sin接口的isReuseSource参数保持一致。对于float数据类型的输入支持开启该参数，half数据类型的输入不支持开启该参数。

输入
