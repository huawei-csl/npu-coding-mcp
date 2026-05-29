# GetCoreMemSize

> **Section**: 6.4.2.1.11  
> **PDF Pages**: 3767–3767  

---

<!-- page 3767 -->

参数说明

参数输入/输出

说明

sliceNum输入数据切分的份数。

aicCoreNum

输入如果算子实现使用了矩阵计算API，请传入GetCoreNumAic返回的数量，否则传入0。

aivCoreNum

输入如果算子实现使用了矢量计算API，请传入GetCoreNumAiv返回的数量，否则传入0。

返回值说明

返回用于底层任务调度的核数。

约束说明

无

调用示例

ge::graphStatus TilingXXX(gert::TilingContext* context) {    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());    auto aicNum = ascendcPlatform.GetCoreNumAic();    auto aivNum = ascendcPlatform.GetCoreNumAiv();    // ..按照aivNum切分数据，并进行计算    uint32_t sliceNum = aivNum;    context->SetBlockDim(ascendcPlatform.CalcTschNumBlocks(sliceNum, aicNum, aivNum));    return ret;}

## 6.4.2.1.11 GetCoreMemSize

功能说明

获取硬件平台存储空间的内存大小，例如L1、L0_A、L0_B、L2等，支持的存储空间类型定义如下：

```cpp
enum class CoreMemType {L0_A = 0, // L0A BufferL0_B = 1, // L0B BufferL0_C = 2, // L0C BufferL1 = 3,   // L1 BufferL2 = 4,   // L2 CacheUB = 5,   // Unified BufferHBM = 6,  // GMFB = 7,   // Fixpipe BufferBT = 8,   // BiasTable BufferRESERVED};
```

函数原型

```cpp
void GetCoreMemSize(const CoreMemType &memType, uint64_t &size) const
```
