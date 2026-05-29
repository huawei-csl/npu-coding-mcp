# GetLogicalXorMaxMinTmpSize

> **Section**: 6.2.4.1.43.2  
> **PDF Pages**: 2226–2226  

---

<!-- page 2226 -->

uint32_t count = 512; // 参与计算的元素个数AscendC::LogicalXor(dst, src0, src1, count);

结果示例如下：

输入数据（src0）:[-4, 4, 1, -8, 0, ... 3]输入数据（src1）:[-1, 3, 1, 5, 1, ... -3]输出数据（dst）:[False, False, False, False, True, ... False]

## 6.2.4.1.43.2 GetLogicalXorMaxMinTmpSize

功能说明

Kernel侧LogicalXor接口的计算需要开发者预留/申请临时空间，本接口用于在Host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到Kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，Kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetLogicalXorMaxMinTmpSize(const platform_ascendc::PlatformAscendC& ascendcPlatform, const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-993接口参数列表

参数名输入/输出

功能

ascendcPlatform

输入输入的平台信息。PlatformAscendC的定义请参见6.4.2.1.2 构造及析构函数。

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入该参数预留，传入默认值false即可。
