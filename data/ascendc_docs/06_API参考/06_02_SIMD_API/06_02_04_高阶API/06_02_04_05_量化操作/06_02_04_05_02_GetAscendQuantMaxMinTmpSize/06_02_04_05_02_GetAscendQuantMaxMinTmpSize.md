# GetAscendQuantMaxMinTmpSize

> **Section**: 6.2.4.5.2  
> **PDF Pages**: 2671–2671  

---

<!-- page 2671 -->

```cpp
LocalTensor<uint8_t> sharedTmpBuffer = inQueue.AllocTensor<uint8_t>();AscendQuantParam para;para.m = m;para.n = n;para.calCount = calCount;AscendQuant<dstType, srcType, scaleType, isReuseSource, config, policy>(dstLocal, srcLocal, sharedTmpBuffer, scaleLocal, offsetLocal, para);
```

●主动配置参数AscendQuantConfig的舍入模式roundMode。// 注意m,n需从外部传入constexpr static bool isReuseSource = false;constexpr static AscendQuantConfig config = {has_offset, 1, RoundMode::CAST_ROUND};constexpr static AscendQuantPolicy policy = AscendQuantPolicy::PER_TOKEN; // 可修改枚举值以使能PER_GROUPLocalTensor<uint8_t> sharedTmpBuffer = inQueue.AllocTensor<uint8_t>();AscendQuantParam para;para.m = m;para.n = n;para.calCount = calCount;AscendQuant<dstType, srcType, scaleType, isReuseSource, config, policy>(dstLocal, srcLocal, sharedTmpBuffer, scaleLocal, offsetLocal, para);

## 6.2.4.5.2 GetAscendQuantMaxMinTmpSize

功能说明

kernel侧AscendQuant接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetAscendQuantMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-1217接口参数列表

参数名输入/输出

描述

srcShape输入

输入的shape信息。

typeSize输入

输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。
